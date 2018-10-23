import discord
from . import hamqth, callook, olerror

class HtmLookup():
    def __init__(self):
        self.hamqth = hamqth.HamQTHLookup()
        self.callook = callook.CallookLookup()

        self.hamqth.connect()

    def lookup(self, call, params):
        clfail = False
        hqfail = False

        # callook lookup
        try:
            clr = self.callook.lookup(call)
        except olerror.LookupResultError:
            clfail = True

        # hamqth lookup
        try:
            hqr = self.hamqth.lookup(call)
        except olerror.LookupResultError:
            hqfail = True
        except olerror.LookupVerificationError:
            mess = 'Bad HamQTH Login.  Yell at the owner of the bot'
            return discord.Embed(title='Error',
                                 description=mess, colour=0x00c0ff)

        # if both failed
        if clfail and hqfail:
            return discord.Embed(title='¯\_(ツ)_/¯', description=('No callsign found\n\n'
                                                             f'You can try, but no promises: https://qrz.com/db/{call}')
                                                             , colour=0x00c0ff)

        # if at most one failed
        if not clfail:
            if hqfail:
                return self.clfill(clr)
            else:
                return self.clfill(clr, hqr)
        else:
            return self.hqfill(hqr)

    def clfill(self, r, hqr=None):
        rets = ''

        # extra info if neccessary
        if hqr is not None:
            itu = hqr.itu
            cq = hqr.cq

        # about field
        about = ''
        about += f'\t**Name:** {r.name}\n'
        if not r.club:
            about += f'\t**Class:** {r.opclass}\n'
        if r.prevcall != '':
            about += f'\t**Previous Callsign:** {r.prevcall}\n'

        # location field
        loc = ''
        loc += f'\t**Country:** {r.country}\n'
        loc += f'\t**Grid Square:** {r.grid}\n'
        loc += f'\t**State:** {r.state}\n'
        loc += f'\t**City:** {r.city}\n'

        # club field
        club = ''
        if r.club:
            club = '**Club Info**\n'
            club += f'\t**Trustee:** {r.trusteename} ({r.trusteecall})\n\n'

        # links
        links = ''
        links += f'\t**QRZ:** https://qrz.com/db/{r.callsign}\n'
        links += f'\t**ULS:** {r.uls}\n'

        # build magical string
        rets = ('**About**\n'
                f'{about}'
                '\n**Location**\n'
                f'{loc}'
                '\n'
                f'{club}'
                '**Links**\n'
                f'{links}')
        em = discord.Embed(title=r.callsign, url=f'https://qrz.com/db/{r.callsign}', description=rets, colour=0x00c0ff)
        em = em.set_footer(text='Source: callook.info')

        # return
        return em


    def hqfill(self, r):
        rets = ''

        # about field
        if r.name != '':
            rets = r.name
        elif 'nick' in r.raw:
            rets = r.raw['nick']
        else:
            rets = 'no name given'

        rets = f'**About**\n\t**Name:** {rets}\n\n'

        # location
        rets += f'**Location**\n\t**Country:** {r.country}\n'
        rets += f'\t**Grid Square:** {r.grid}\n'
        rets += f'\t**City:** {r.city}\n\n'

        # links
        rets += f'**Links**\n\t**QRZ:** https://qrz.com/db/{r.callsign}\n'

        em = discord.Embed(title=r.callsign, url=f'https://qrz.com/db/{r.callsign}', description=rets, colour=0x00c0ff)
        em = em.set_footer(text='Source: hamqth.com')
        return em
