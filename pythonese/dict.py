#!/usr/bin/env python

import re
import os
import json

searchPath = "/root/testing/plugdj"
search_artist = input("Enter the artist you want to search for: ")

if not (searchPath.endswith("/") or searchPath.endswith("\\") ):
    searchPath = searchPath + "/"

for fname in os.listdir("/root/testing/plugdj/"):
    if fname.endswith('.json'):
        jdata = json.loads(open (searchPath + fname).read())
        for c in jdata['title'][0]['title']:
            print 'Title: {}, Artist: {}'.format(c.get('title', 'no tittle'),
                                                 c.get('artist', 'no artist'))

def build_structure(data, d=[]):
    if 'title' in data:
        for c in data['title']:
            d.append({'title': c.get('title', 'no tittle'),
                                     'artist': c.get('artist', None)})
            build_structure(c, d)
    return d

pprint.pprint(build_structure(jdata))
