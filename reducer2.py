import sys


arg1 = sys.argv[1]
arg2 = sys.argv[2]

ag_count = []

#Partitoner
for line in sys.stdin:
    line = line.strip()
    age, count = line.split('\t')

    if int(age) >= int(arg1) and int(age) <= int(arg2) :
        ag_count.append(int(count))


#Reducer

print '%s\t%s'% ("sum", sum(ag_count))
