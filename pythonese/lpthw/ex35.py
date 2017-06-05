from sys import exit

def gold_room():
    print "tHIS ROOM is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Dead man can't type.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy fucker, take more!")


def bear_room():
    print """There is a bear here.
             The bear has a bunch of honey and
             the fat bear is in front of another door. 
             How are you going to get passed the bear?"""
    bear_moved = False

    while True:
        choice = raw_input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You shall pass!"
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear is pissed and now you've got no legs!")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "Whatchu sayin?"

def cthulhu_room():
    print """ Here you see the great evil Cthulhu. 
              He, it, whatever it is, stares at you and you go insane!
              Do you flee for your life or eat your head?"""

    choice = raw_input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print """You're in a dark room. 
             There is a door to your right and left,
             which one do you take?"""

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around until you stave, like a zombie!")

start()
