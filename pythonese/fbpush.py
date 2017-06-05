#!/usr/bin/evn python

#-*- coding: utf-8 -*-
import time
from facepy import GraphAPI


#Author: T Shrinivasan <tshrinivasan@gmail.com>


# get api from here  https://developers.facebook.com/tools/explorer


api = "EAACEdEose0cBAJXgocg6uxBevhk6tg6lLPmfozynXFnMAzynwVeKahWhPajkKi8qvx5QogZBZCPt0RZBZAW4VNBQ0eTGzhvHOTAemZCzxjT53ZBByXufpZAUjuuHPS1vz5bNVZCp5i75MU5GyHUkqlBO2eLWY5XE3ysc8035fiJ6rwZDZD"



graph = GraphAPI(api)

message = '''


This is only a test message to my facebook profile. I want to test out how to post 
http://www.1001tracklists.com/tracklist/118234_adam-ellis-trancepodium-10th-anniversary-2016-09-29.html

'''


# Find the ids of your desired groups from http://lookup-id.com/  
# and add this in this array groups

groups = [ 'me' ]



#for group_id in groups:
print "Posting to " + 'http://www.facebook.com/seanderson'
graph.post(path =str(groups) + '/feed', message=message)
#time.sleep(10)
print "Done"
