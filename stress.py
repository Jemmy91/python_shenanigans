#!/usr/bin/python
from random import randint

thesaurus = ['stupid','dumb','foolish','futile','ill-advised','laughable','ludicrous','naive','senseless','shortsighted','trivial','rash','thick','unintelligent','brainless','dense','dim','doltish','dopey','half-baked','half-witted','idiodic','inane','meaningless','mindless','moronic','nonsensical','obtuse','pointless','simple-minded','thick-headed','witless']

def stress_out():
  sentence = raw_input('Please vent so that your sentence should end in an adjective: ')
  print sentence, thesaurus[randint(0,31)]
  for num in range(0,31):
    answer = raw_input('Do you need to vent more? [y/n]')
    if answer == "y":
      sentence = raw_input('Please continue to vent: ')
      print sentence, thesaurus[randint(0,31)]
    elif answer == "n":
      print "Glad I could help."
      exit()
    else:
      print "Please come back when you're ready to cooperate."
      exit()

stress_out()
