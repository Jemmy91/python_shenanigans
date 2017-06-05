from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from {0} to {1}".format(from_file, to_file)

in_file = open(from_file); indata = in_file.read()

print "The input file is {x} bytes long".format(x=len(indata))

print """Does the output file exist?
...{f}""".format(f=exists(to_file))
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w'); out_file.write(indata)

print "Alright, pencil's down. Done!"

out_file.close()
in_file.close()

