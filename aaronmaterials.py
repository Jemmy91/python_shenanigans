#! /usr/bin/env python
# Let's make this interactive so it can be used again and again. 

# This will allow me to calculate how much people owe me
# for parts and labor

# Setting up basic variables here. 
# These are the cost of the materials I purchased plus tax. 
# Section 1 
tax = 1.8025
ethernetbox = 139.99 * tax
cat6_keystone = 26.99 * tax
gang_plate = 10.92 * tax
keystone_wallplate = 9.95 * tax
crimp_connectors = 5.99 * tax
network_tools = 34.629175
labor = 100

##################################################

# Section 2
# Material quantities
cat6roll = 1000
keystones = 25
gangplate = 10
wallplates = 10
connectors = 50

##################################################

# Section 3 _final
# How much inventory was used during the job
cat6roll_final = 170
keystones_final = 4
gangplate_final = 3
wallplate_final = 3
connectors_final = 4

##################################################

# Section 4 _price
# This is the price per unit I used of material for the job
# To find out price per unit, divide cost of materials
# in section 1 with the quantity in Section 2.
cat6roll_price = ethernetbox / cat6roll
keystone_price = cat6_keystone / keystones
gangplate_price = gang_plate / gangplate
wallplate_price = keystone_wallplate / wallplates
connector_price = crimp_connectors / connectors

##################################################

# Section 5 _left (what's left in the packages)
# How much do I have left after my job?
cat6roll_left = cat6roll - cat6roll_final
keystones_left = keystones - keystones_final
gangplate_left = gangplate - gangplate_final
wallplate_left = wallplates - wallplate_final
connectors_left = connectors - connectors_final

##################################################

# Section 6 _total (inventory used for installation)
# Let's find the total amount of money spend on products from 
# the materials used. In order to do this, let's multiply the variable in Section 4 (price per unit) x the amount
# used in Section 3 (materials used)
cat6roll_total   = cat6roll_price  * cat6roll_final
keystones_total  = keystone_price  * keystones_final
gangplates_total = gangplate_price * gangplate_final
wallplates_total = wallplate_price * wallplate_final 
connectors_total = connector_price * connectors_final



###################################################

# Section 7 
# Cost of materials as is
print "Cable Matters 1000FT Cat6 $ %s"  % round(ethernetbox, 2)
print "Package of 25 keystones   $  %s" % round(cat6_keystone, 2)
print "Gang plates               $  %s" % round(gang_plate, 2)
print "Wallplates                $  %s" % round(keystone_wallplate, 2)
print "Cat6 Crimp Connectors     $  %s" % round(crimp_connectors, 2)
print "Tools used                $  %s" % round(network_tools, 2)
print ""
print ""
# Section 8 (housing? It's a joke...)
# At the end of the day...how much does he really owe me?
print "Feet of Cat6 used                %s FT" % cat6roll_final
print "Cat6 cable price per foot used   $ %s"  % round(cat6roll_total, 2)
print ""
print "Amount of Keystone Jacks used    %s"    % keystones_final
print "Keystone total price             $ %s"  % round(keystones_total, 2)
print ""
print "Drywall Gangplates used          %s"    % gangplate_final
print "Drywall Gangplate total price    $ %s"  % round(gangplates_total, 2)
print ""
print "Ethernet Wallplates used         %s"    % wallplate_final
print "Ethernet Wallplate total price   $ %s"  % round(wallplates_total, 2)
print ""
print "Cat6 Connectors used             %s"    % connectors_final
print "Cat6 Connectors total            $ %s"  % round(connectors_total, 2),
print ""

# Section 9 project_total
# Now that we've figured out the price for everything and calculated it
# we need to add up the totals for the project and get this over to Aaron
# so we can get paid for our work!

parts_total = cat6roll_total + keystones_total + gangplates_total + wallplates_total + connectors_total
project_total = parts_total + labor
print "Total parts                      $%s" % round(parts_total, 2)
print "Total labor                      $%s" % labor
print "Total amount owed for work done  $%s" % round(project_total, 2)
