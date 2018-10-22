"""
HamQTH Callsign Lookup
Author: Ben Johnson, AB3NJ

Uses HamQTH's API to retreive information on callsigns
"""


import os.path
from urllib import request, error
import xml.etree.ElementTree as et
from . import olerror, olresult


# importorator
__all__ = ['HamQTHLookup']


# hamqth lookup class
class HamQTHLookup:
    def __init__(self):
        self.username = None
        self.password = None
        self.key = None

        self.active = False
        self.prefix = "{https://www.hamqth.com}"

    def connect(self):
        """
        tries to automatically connect with login information
        and start a HamQTH session if possible

        raises LookupVerificationError: if login is bad
        """
        # look for appropriate files
        if not os.path.exists('keys/hamqth-login.txt'):
            raise olerror.LookupVerificationError('HamQTH')
        with open('keys/hamqth-login.txt', 'r') as f:
            lines = f.readlines()
            if len(lines) != 2:
                raise olerror.LookupVerificationError('HamQTH')
            else:
                self.username = lines[0].strip()
                self.password = lines[1].strip()
        if os.path.exists('keys/hamqth-key.txt'):
            with open('keys/hamqth-key.txt', 'r') as f:
                lines = f.readlines()
                if len(lines) != 1:
                    self.get_key()
                else:
                    self.key = lines[0].strip()
                    self.active = True
        else:
            self.get_key()

    def create_login(self, username, password):
        """
        Creates or overwrites a login file

        :param username: HamQTH username (callsign)
        :param password: HamQTH account password
        """
        with open('.onlinelookup-login.txt', 'w') as f:
            f.write(username + '\n' + password)

    def get_key(self):
        """
        Gets and sets a HamQTH API key when starting and when the key expires
        Uses already set login credentials
        Note: This key is good for one hour

        raises LookupVerificationError: If login is bad
        """
        # make request
        req = (f'https://www.hamqth.com/xml.php'
               f'?u={self.username}'
               f'&p={self.password}')

        # get XML data
        data = et.parse(request.urlopen(req))
        root = data.getroot()

        # pass
        if root[0][0].tag == self.prefix + "session_id":
            self.active = True
            self.key = root[0][0].text

            # write to a file
            with open('keys/hamqth-key.txt', 'w') as f:
                f.write(self.key)
                f.close()

        # fail
        elif root[0][0].tag == self.prefix + "error":
            raise olerror.LookupVerificationError('HamQTH')

        # catastrophic failure
        else:
            raise olerror.LookupVerificationError('HamQTH')

    def lookup(self, call, retry=True):
        """
        Uses HamQTH to look up information on a callsign

        :param call: the callsign to look up
        :param retry: retry status for key renewal. If the service fails but
            the key is good, then this will stop an endless loop
        :returns: LookupResult class filled with information from HamQTH
        :raises LookupActiveError: if no connection has been made to the API
        :raises LookupVerificationError: if the login credentials are wrong
        :raises LookupResultError: if the lookup returns no information
        """
        # error check
        if not self.active:
            raise olerror.LookupActiveError('HamQTH')

        # setup
        lr = olresult.LookupResult()
        retdict = {}

        # make request
        req = (f'https://www.hamqth.com/xml.php'
               f'?id={self.key}'
               f'&callsign={call}'
               f'&prg=YARL')

        # get the goods
        data = et.parse(request.urlopen(req))
        root = data.getroot()

        # failure
        if root[0].tag == self.prefix + "session":
            # get failure cause
            errmess = root[0][0].text

            # bad key
            if errmess == 'Session does not exist or expired':
                self.get_key()
                if retry:
                    return self.lookup(call, False)
                else:
                    raise olerror.LookupVerificationError('HamQTH')

            # no call found
            elif errmess == 'Callsign not found':
                raise olerror.LookupResultError('HamQTH')

        # callsign found
        elif root[0].tag == self.prefix + "search":
            for t in root[0]:
                key = t.tag[len(self.prefix):]
                value = t.text

                # info filling
                if key == 'callsign':
                    lr.callsign = value.upper()
                elif key == 'adr_name':
                    lr.name = value
                elif key == 'adr_street1':
                    lr.street1 = value
                elif key == 'adr_street2':
                    lr.street2 = value
                elif key == 'adr_city':
                    lr.city = value
                elif key == 'us_state':
                    lr.state = value
                elif key == 'adr_zip':
                    lr.zip = value
                elif key == 'country':
                    lr.country = value
                # elif key == 'qth':
                #     lr.qth = value
                elif key == 'itu':
                    lr.itu = value
                elif key == 'cq':
                    lr.cq = value
                elif key == 'grid':
                    lr.grid = value

                # set raw data for extra whatever
                if key is not None and value is not None:
                    retdict[key] = value

            # set raw data and return
            lr.raw = retdict
            return lr
