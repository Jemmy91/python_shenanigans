#!/usr/bin/python

i = 0
num = []

while i < 6:
    print "At the top i is {0}".format(i)
    num.append(i)

    i = i + 1
    print "Numbers now: " , num
    print "At bottom, i is {0}".format(i)

print ' numbs: '
    
for n in num:
    print n
