#!/usr/bin/python

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) >=41:
	a = unicode(line[21], 'utf-8')
	if a and a.isnumeric() and not a.isspace():
          state = a
	  print '%s\t%s' % (a, 1)
