#!/usr/bin/python

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for num in the_count:
    print "This is count {0}".format(num)

for fruit in fruits:
    print "A fruit of type: {0}".format(fruit)

for i in change:
    print "I have %r" % i

# we can also build lists, first start with empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print "Adding {0} to the list.".format(i)
    # append is a function that lists understand
    elements.append(i)

for i in elements:
    print "Element was: {elem}".format(elem=i)
