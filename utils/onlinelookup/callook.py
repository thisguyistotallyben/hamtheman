"""
Callook Callsign Lookup
Author: Ben Johnson, AB3NJ

Uses Callook's API to retreive information on callsigns
"""


import json
import os.path
from urllib import request, error
from . import olerror


# importorator
__all__ = ['CallookLookup']


# return class
class CallookResult:
    def __init__(self):
        # basic info
        self.callsign = ''
        self.prevcall = ''
        self.name = ''
        self.opclass = ''

        # location
        self.country = ''
        self.grid = ''
        self.zip = ''
        self.state = ''
        self.city = ''


        # club stuff
        self.club = False
        self.trusteename = ''
        self.trusteecall = ''

        # ULS stuff
        self.frn = ''
        self.uls = ''

        # raw data
        self.raw = {}


def prettify(name):
    names = name.split()
    newname = ''

    for i in names:
        if len(name) > 1:
            newname += i[0] + i[1:].lower()
        else:
            newname += i
        newname += ' '

    return newname


# hamqth lookup class
class CallookLookup:
    def lookup(self, call):
        """
        Uses callook.info to look up information on a US callsign

        :param call: the callsign to look up
        :returns: LookupResult class filled with information from HamQTH
        :raises LookupResultError: if the lookup returns no information
        """

        # setup
        lr = CallookResult()
        retdict = {}

        # make request
        req = (f'https://callook.info/{call}/json')

        with request.urlopen(req) as url:
            data = json.loads(url.read().decode())

        # check if callsign or not
        if data['status'] == 'INVALID':
            raise olerror.LookupResultError('Callook')

        # ## GET THE GOODS ## #

        # basic info
        lr.callsign = data['current']['callsign']
        lr.prevcall = data['previous']['callsign']

        lr.name = prettify(data['name'])

        lr.opclass = prettify(data['current']['operClass'])

        # location
        lr.country = 'United States'
        lr.grid = data['location']['gridsquare']

        addrs = data['address']['line2'].split(',')
        addrs2 = addrs[1].split()
        lr.city = prettify(addrs[0])
        lr.state = addrs2[0]
        lr.zip = addrs2[1]

        # club stuff
        if data['type'] == 'CLUB':
            lr.club = True
            lr.trusteename = data['trustee']['name']
            lr.trusteecall = data['trustee']['callsign']

        # uls stuff
        lr.frn = data['otherInfo']['frn']
        lr.uls = data['otherInfo']['ulsUrl']

        # raw data
        lr.raw = data

        return lr
