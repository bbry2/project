#!/usr/bin/python3

import matplotlib
matplotlib.use('Agg')
import pylab

print("HI")
pylab.plot([1,2,3])
pylab.savefig('/home/student/cs122-win-17-rhopkins18/project/ img.png')
