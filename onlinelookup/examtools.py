import json
import os.path
from urllib import request, error
import olerror, olresult


# importorator
__all__ = ['ExamToolsLookup']


class ExamToolsLookup:
    def lookup(self, call):
        """
        Uses exam.tools to look up information on a US callsign

        :param call: the callsign to look up
        :returns: LookupResult class filled with information from HamQTH
        :raises LookupResultError: if the lookup returns no information
        """

        # setup
        lr = olresult.LookupResult()

        # make request
        req = (f'https://exam.tools/api/uls/individual/{call}')

        with request.urlopen(req) as url:
            data = json.loads(url.read().decode())

        # check if callsign or not
        if 'type' in data:
            if data['type'] == 'NotFound':
                raise olerror.LookupResultError('ExamTools')

        # ## GET THE GOODS ## #

        lr.source = 'exam.tools'

        # basic info
        lr.callsign = data['callsign']

        first_name = data['first_name']
        middle_initial = data['middle_initial']
        last_name = data['first_name']
        lr.name = f'{first_name} {middle_initial} {last_name}'

        lr.opclass = data['license_class']

        # location
        lr.country = 'United States'

        lr.city = data['city']
        lr.state = data['state']
        lr.zip = data['zip']

        # club stuff (ASK ABOUT HOW THIS PART WORKS BECAUSE IT DOES NOT RIGHT NOW)
        # if data['type'] == 'CLUB':
        #     lr.club = True
        #     lr.trusteename = data['trustee']['name']
        #     lr.trusteecall = data['trustee']['callsign']

        # uls stuff
        lr.frn = data['frn']

        # raw data
        lr.raw = data

        return lr