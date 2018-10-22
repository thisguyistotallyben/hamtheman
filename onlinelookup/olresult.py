# return class
class LookupResult:
    def __init__(self):
        # basic info
        self.callsign = ''
        self.prevcall = ''
        self.opclass = ''
        self.name = ''

        # location
        self.country = ''
        self.grid = ''
        self.itu = ''
        self.cq = ''
        self.zip = ''
        self.state = ''
        self.city = ''

        # club stuff
        self.club = False
        self.trusteename = ''
        self.trusteecall = ''

        # other info
        self.street1 = ''
        self.street2 = ''

        # ULS stuff
        self.frn = ''
        self.uls = ''

        # raw data
        self.raw = {}
