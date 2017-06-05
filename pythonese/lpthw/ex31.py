#!/usr/bin/python

print "You enter a dark room with three doors. Do you go through door #1, door #2 or secret door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a gian bear here eating a cheesecake. What do you do?"
    print "1. Take the cake"
    print "2. Scream at the bear."
    print "3. Find a rifle and shoot the bear's eye out."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job numbnuts!"
    elif bear == "2":
        print "The Bear eats your legs off. Another smart move!"
    elif bear == "3":
        print "You've shot the bear's eyes out, but now you're out of bullets! You realize the bear can still smell you and has mauled your face to bits!"

    else:
        print "Well, doing {0} is probably better. Bear runs away.".format(bear)

elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello, hello world!"
    else:
        print "The insanity rots your eyes into a pool of muck."

elif door == "3":
    print "You've just won the lottery, congratulations!!"
    i = 0
    while i == 0: print "Congrats!!"

else:
    print "You stumble around and fall on a knife and die. GG no re!"

