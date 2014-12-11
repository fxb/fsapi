#/usr/bin/env python

import ssdp
import sys
from pprint import pprint
from fsapi import FSAPI

services = ssdp.discover('urn:schemas-frontier-silicon-com:fs_reference:fsapi:1')
if not len(services):
    print 'No server found on network'
    sys.exit(1)

pprint(services[0].location)

with FSAPI(services[0].location, 1234) as fs:
    #fs.volume = 12
    #fs.mode = 'dab'
    #fs.power = True

    pprint(fs)

    print 'Name: %s' % fs.friendly_name
    print 'Version: %s' % fs.version
    print 'Mute: %s' % fs.mute
    print 'Mode: %s' % fs.mode
    print 'Power: %s' % fs.power
    print 'Volume: %s' % fs.volume
    print 'Play status: %s' % fs.play_status
    print 'Track name: %s' % fs.play_info_name
    print 'Track text: %s' % fs.play_info_text
