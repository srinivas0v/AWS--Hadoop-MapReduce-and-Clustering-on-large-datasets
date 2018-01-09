#!/usr/bin/python

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    if len(line) >=41:
	a = line[8]
	if a and not a.isspace():
          state = a
	  print '%s\t%s' % (a, 1)

reducer.py
#!/usr/bin/python
#Reducer.py
import sys

st_count = {}
b = "TX"
#Partitoner
for line in sys.stdin:
    line = line.strip()
    state, count = line.split('\t')

    if state in st_count:
        st_count[state].append(int(count))
    else:
        st_count[state] = []
        st_count[state].append(int(count))
