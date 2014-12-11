#/usr/bin/env python

import ssdp
import sys
from pprint import pprint
from fsapi import FSAPI

services = ssdp.discover('urn:schemas-frontier-silicon-com:fs_reference:fsapi:1')
if not len(services):
    print 'No device server found on network'
    sys.exit(1)

print 'Found device server at "%s".' % (services[0].location)

with FSAPI(services[0].location, 1234) as fs:
    #fs.volume = 10
    #fs.mode = 'dab'
    #fs.power = True

    print 'FSAPI Endpoint is "%s".' % fs.get_fsapi_endpoint()

    pprint(fs)

    print 'Name: %s' % fs.friendly_name
    print 'Version: %s' % fs.version
    print 'Mute: %s' % fs.mute
    print 'Mode: %s' % fs.mode
    print 'Power: %s' % fs.power
    print 'Volume: %s' % fs.volume
    print 'Play status: %s' % fs.play_status
    print 'Artist name: %s' % fs.play_info_artist
    print 'Album name: %s' % fs.play_info_album
    print 'Track name: %s' % fs.play_info_track
    print 'Duration: %s' % fs.play_info_duration
    print 'Track text: %s' % fs.play_info_text
    print 'EQ Bands: %s' % fs.eq_bands

    # Long poll for events.
    # print 'Notifications: %s' % fs.notifications
