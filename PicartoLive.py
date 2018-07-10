#!/usr/bin/env python
"""PicartoLive.py: Swaps out online and offline static resources based on wether a picarto stream is online."""
import urllib, json, os
from shutil import copyfile


__author__ = "TecknoJock"
__copyright__ = "2018 CC 3.0 sharealike--attriubution--derivative"
scriptDir = os.path.dirname(os.path.realpath(__file__))
with open('%s/urls.txt' % scriptDir,'r') as urls:
        url = urls.readline().strip()
        while url:
                response = urllib.urlopen("https://api.picarto.tv/v1/channel/name/%s" % url )
                data = json.loads(response.read())
                if data["online"]:
                        if data["adult"]:
                                copyfile('%s/_nsfwlive.png' % (scriptDir),'%s/%s.png' % (scriptDir,url))
                        else:
                                copyfile('%s/_live.png' % (scriptDir),'%s/%s.png' % (scriptDir,url))
                else:
                        copyfile('%s/_offline.png' % (scriptDir),'%s/%s.png' % (scriptDir,url))
                url = urls.readline().strip()
