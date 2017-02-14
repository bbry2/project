from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import json
import traceback
from io import StringIO
import sys
import csv
import os
from operator import and_
from election_analysis import find_data
from functools import reduce

NOPREF_STR = 'No preference'
RES_DIR = os.path.join(os.path.dirname(__file__), '..', 'res')
COLUMN_NAMES = dict(
        state='State',
        county='County',
        total_2008='Total Votes 2008',
        dem_2008='Democratic Votes 2008',
        gop_2008='Republican Votes 2008',
        oth_2008='Third Party Votes 2008',
        dem_08_perc='Democratic Vote Percentage 2008',
        gop_08_perc='Republican Votes Percentage 2008',
        oth_08_perc='Third Party Votes Percentage 2008',
        win_marg_08='2008 Winning Margin',
        winner_08='2008 Winner',
        total_2012='Total Votes 2012',
        dem_2012='Democratic Votes 2012',
        gop_2012='Republican Votes 2012',
        oth_2012='Third Party Votes 2012',
        dem_12_perc='Democratic Vote Percentage 2012',
        gop_12_perc='Republican Votes Percentage 2012',
        oth_12_perc='Third Party Votes Percentage 2012',
        win_marg_12='2012 Winning Margin',
        winner_12='2012 Winner',
        total_2016='Total Votes 2016',
        dem_2016='Democratic Votes 2016',
        gop_2016='Republican Votes 2016',
        oth_2016='Third Party Votes 2016',
        dem_16_perc='Democratic Vote Percentage 2016',
        gop_16_perc='Republican Votes Percentage 2016',
        oth_16_perc='Third Party Votes Percentage 2016',
        win_marg_16='2016 Winning Margin',
        winner_16='2016 Winner',
        diff_0812='2008 t0 2012 Difference',
        diff_1216='2012 t0 2012 Difference',
        diff_0816='2008 t0 2016 Difference',
        direction_0812='2008 to 2012 Direction',
        direction_0816='2008 to 2016 Direction',
        direction_1216='2012 to 2016 Direction'
        )


def _valid_result(res):
    """Validates results returned by find_courses"""
    (HEADER, RESULTS) = [0,1]
    ok = (isinstance(res, (tuple, list)) and 
          len(res) == 2 and
          isinstance(res[HEADER], (tuple, list)) and
          isinstance(res[RESULTS], (tuple, list)))
    if not ok:
        return False

    n = len(res[HEADER])
    def _valid_row(row):
        return isinstance(row, (tuple, list)) and len(row) == n
    return reduce(and_, (_valid_row(x) for x in res[RESULTS]), True)


def _load_column(filename, col=0):
    """Loads single column from csv file"""
    with open(filename) as f:
        col = list(zip(*csv.reader(f)))[0]
        return list(col)


def _load_res_column(filename, col=0):
    """Load column from resource directory"""
    return _load_column(os.path.join(RES_DIR, filename), col=col)


def _build_dropdown(options):
    """Converts a list to (value, caption) tuples"""
    return [(x, x) if x is not None else ('', NOPREF_STR) for x in options]


STATES = _build_dropdown([None] + _load_res_column('state_list.csv'))
COUNTIES = _build_dropdown(_load_res_column('county_list.csv'))
#DEPTS = _build_dropdown([None] + _load_res_column('dept_list.csv'))


class IntegerRange(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        fields = (forms.IntegerField(),
                  forms.IntegerField())
        super(IntegerRange, self).__init__(fields=fields,
                                           *args, **kwargs)

    def compress(self, values):
        if values and (values[0] is None or values[1] is None):
            raise forms.ValidationError('Must specify both lower and upper '
                                        'bound, or leave both blank.')

        return values


class EnrollmentRange(IntegerRange):
    def compress(self, values):
        super(EnrollmentRange, self).compress(values)
        for v in values:
            if not (1 <= v <= 1000):
                raise forms.ValidationError('Enrollment bounds must be in the range 1 to 1000.')
        if values and (values[1] < values[0]):
            raise forms.ValidationError('Lower bound must not exceed upper bound.')
        return values


class TimeRange(IntegerRange):
    def compress(self, values):
        super(TimeRange, self).compress(values)
        for v in values:
            if not _valid_military_time(v):
                raise forms.ValidationError('The value {:04} is not a valid military time.'.format(v))
        if values and (values[1] < values[0]):
            raise forms.ValidationError('Lower bound must not exceed upper bound.')
        return values

RANGE_WIDGET = forms.widgets.MultiWidget(widgets=(forms.widgets.NumberInput,
                                                  forms.widgets.NumberInput))


class BuildingWalkingTime(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        fields = (forms.IntegerField(),
                  forms.ChoiceField(label='Building', choices=BUILDINGS, required=False),)
        super(BuildingWalkingTime, self).__init__(
                                           fields=fields,
                                           *args, **kwargs)

    def compress(self, values):
        if len(values) == 2:
            if values[0] is None or not values[1]:
                raise forms.ValidationError('Must specify both minutes and building together.')
            if values[0] < 0:
                raise forms.ValidationError('Walking time must be a non-negative integer.')
        return values


class SearchForm(forms.Form):
    # query = forms.CharField(
    #         label='Search terms',
    #         help_text='e.g. mathematics',
    #         required=False)
    # enrollment = EnrollmentRange(
    #         label='Enrollment (lower/upper)',
    #         help_text='e.g. 1 and 40',
    #         widget=RANGE_WIDGET,
    #         required=False)
    # time = TimeRange(
    #         label='Time (start/end)',
    #         help_text='e.g. 1000 and 1430 (meaning 10am-2:30pm)',
    #         widget=RANGE_WIDGET,
    #         required=False)
    # time_and_building = BuildingWalkingTime(
    #         label='Walking time:', 
    #         help_text='e.g. 10 and RY (meaning at most a 10-minute walk from Ryerson).',
    #         required=False, 
    #         widget=forms.widgets.MultiWidget(
    #             widgets=(forms.widgets.NumberInput,
    #                      forms.widgets.Select(choices=BUILDINGS))))
    county = forms.ChoiceField(label='Or see data from a county', choices=COUNTIES, required=False)
    states = forms.MultipleChoiceField(label='Select states',
                                     choices=STATES,
                                     widget=forms.CheckboxSelectMultiple,
                                     required=False)
    show_args = forms.BooleanField(label='Show args_to_ui',
                                   required=False)


def home(request):
    context = {}
    res = None
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():

            # Convert form data to an args dictionary for find_courses
            args = {}
            # if form.cleaned_data['query']:
            #     args['terms'] = form.cleaned_data['query']
            # enroll = form.cleaned_data['enrollment']
            # if enroll:
            #     args['enroll_lower'] = enroll[0]
            #     args['enroll_upper'] = enroll[1]
            # time = form.cleaned_data['time']
            # if time:
            #     args['time_start'] = time[0]
            #     args['time_end'] = time[1]

            county = form.cleaned_data['county']
            if county:
                args['county'] = county
            else:
                args['county'] = None
            states = form.cleaned_data['states']
            if states:
                args['state'] = states
            else:
                args['state'] = None
            # dept = form.cleaned_data['dept']
            # if dept:
            #     args['dept'] = dept

            # time_and_building = form.cleaned_data['time_and_building']
            # if time_and_building:
            #     args['walking_time'] = time_and_building[0]
            #     args['building'] = time_and_building[1]

            if form.cleaned_data['show_args']:
                context['args'] = 'args_to_ui = ' + json.dumps(args, indent=2)

            try:
                res = find_data(args)
            except Exception as e:
                print('Exception caught')
                bt = traceback.format_exception(*sys.exc_info()[:3])
                context['err'] = """
                An exception was thrown in find_courses:
                <pre>{}
{}</pre>
                """.format(e, '\n'.join(bt))

                res = None
    else:
        form = SearchForm()

    # Handle different responses of res
    if res is None:
        context['result'] = None
    elif isinstance(res, str):
        context['result'] = None
        context['err'] = res
        result = None
        cols = None
    elif not _valid_result(res):
        context['result'] = None
        context['err'] = ('Return of find_courses has the wrong data type. '
                         'Should be a tuple of length 4 with one string and three lists.')
    else:
        columns, result = res

        # Wrap in tuple if result is not already
        if result and isinstance(result[0], str):
            result = [(r,) for r in result]

        context['result'] = result
        context['num_results'] = len(result)
        context['columns'] = [COLUMN_NAMES.get(col, col) for col in columns]

    context['form'] = form
    return render(request, 'index.html', context)