# Author:  Benjamin Johnson
# Purpose: It wants to be the very dankest.


import discord
import os
import wget
from random import randint
import urllib
import urllib.request
import json
from datetime import datetime

from onlinelookup import hamqth, callook, olerror


# setup
client = discord.client.Client()
tomorse = {'a':'.-',
           'b':'-...',
           'c':'-.-.',
           'd':'-..',
           'e':'.',
           'f':'..-.',
           'g':'--.',
           'h':'....',
           'i':'..',
           'j':'.---',
           'k':'-.-',
           'l':'.-..',
           'm':'--',
           'n':'-.',
           'o':'---',
           'p':'.--.',
           'q':'--.-',
           'r':'.-.',
           's':'...',
           't':'-',
           'u':'..-',
           'v':'...-',
           'w':'.--',
           'x':'-..-',
           'y':'--.-',
           'z':'--..',
           '1':'.----',
           '2':'..---',
           '3':'...--',
           '4':'....-',
           '5':'.....',
           '6':'-....',
           '7':'--...',
           '8':'---..',
           '9':'----.',
           '0':'-----'
          }
help_message = ("**morse [message]:** Translates a message into morse code\n"
                "**cond:** Gives solar conditions\n"
                "**call [callsign]:** gives information on a call sign\n"
                "**utc:** gives the time in UTC")

discordworkaround = 0
ol = hamqth.HamQTHLookup()
cl = callook.CallookLookup()

# start online lookup
ol.connect()

# ready message
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="with Baofengs"))
    print('Shaking and also baking')

# main looping algorithm
@client.event
async def on_message(mess):
    # setup
    isstr = False
    isem = False
    s = ''

    # string manipulation
    nmess = mess.content.lower()
    msplit = nmess.split(' ', 1)

    # normal command prefaced with htm
    if msplit[0] == 'htm' and len(msplit) == 2:
        # split suffix
        command = msplit[1].split(' ')
        clen = len(command)

        # help
        if command[0] == 'help' and clen == 1:
            em = discord.Embed(title='Commands: Preface with \'htm\'',
                               description=help_message,
                               colour=0x00c0ff)
            return await client.send_message(mess.channel, embed=em)

        # morse
        elif command[0] == 'morse' and clen >= 2:
            s += morse(mess.content)

        # conditions
        elif command[0] == 'cond' and clen == 1:
            if os.path.isfile("conditions.gif"):
                os.remove("conditions.gif")
            wget.download("http://www.hamqsl.com/solar101pic.php", "conditions.gif", bar=None)
            # os.chmod("conditions.gif", 655)
            return await client.send_file(mess.channel, "conditions.gif")

        # standards
        elif command[0] == 'standards' and clen == 1:
            return await client.send_file(mess.channel, 'standards.png')

        # call lookup
        elif command[0] == 'call' and clen == 2:
            em = get_call(command[1])
            return await client.send_message(mess.channel, embed=em)
        # time in utc
        elif command[0] == 'utc' and clen == 1:
            em = get_time()
            return await client.send_message(mess.channel, embed=em)

    # silly other things
    elif msplit[0] == 'oof':
        s += 'rip'

    elif msplit[0] == 'boonk':
        s += (':regional_indicator_b: :regional_indicator_o: :regional_indicator_o: :regional_indicator_n: :regional_indicator_k:     '
              ':regional_indicator_g: :regional_indicator_a: :regional_indicator_n: :regional_indicator_g:')
    elif msplit[0] == 'bonk' and len(msplit) == 1:
        s += ':regional_indicator_b: :regional_indicator_o: :regional_indicator_n: :regional_indicator_k:'

    '''
    # specifically the ham not HAM part
    smess = mess.content.split(' ')
    if "HAM" in smess and mess.author.name != "HamTheMan":
        s += "ham not HAM"
    '''

    if s != '':
        return await client.send_message(mess.channel, s)


def get_cond():
    dwa = open("dwa.txt", 'r')
    num = dwa.readline()
    print(num)
    dwa.close()
    s = "http://www.hamqsl.com/solar101vhf.php?q=" + num
    num = str(int(num) + 1)
    dwa = open("dwa.txt", 'w')
    dwa.write(num)
    dwa.close()
    return s


def get_time():
    s = str(datetime.utcnow())
    ss = s.strip().split()
    date = ss[0]
    time = ss[1]
    time = time[0:8]

    ntitle = "Universal Coordinated Time"
    nmessage = "**Date:** " + date + "\n**Time:** " + time
    return discord.Embed(title=ntitle, description=nmessage, colour=0x00c0ff)


def get_call(call):
    clfail = False
    hqfail = False

    # try to get information from at least one source
    try:
        clr = cl.lookup(call)
    except olerror.LookupResultError:
        clfail = True
    try:
        hqr = ol.lookup(call)
    except olerror.LookupResultError:
        hqfail = True
    except olerror.LookupVerificationError:
        return discord.Embed(title='Error', description='Bad HamQTH Login\n¯\_(ツ)_/¯', colour=0x00c0ff)

    # if both failed
    if clfail and hqfail:
        return discord.Embed(title='¯\_(ツ)_/¯', description=('No callsign found\n\n'
                                                         f'You can try, but no promises: https://qrz.com/db/{call}')
                                                         , colour=0x00c0ff)

    # if at most one failed
    if not clfail:
        if hqfail:
            return clfill(clr)
        else:
            return clfill(clr, hqr)
    else:
        return hqfill(hqr)

def clfill(r, hqr=None):
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


def hqfill(r):
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

    '''
    # build result string
    rs = (f'**Name:** {name}\n'
          f'**Country:** {r.country}\n')
    if r.state != '':
        rs += f'**State:** {r.state}\n'
    if 'current' in callook:
        level = callook['current']['operClass']
        level = level[0] + level[1:].lower()
        rs += f'**Level:** {level}\n'
    rs += (f'**Location:** {r.qth}\n\n'
           f'**More Info:** https://qrz.com/db/{r.callsign}')
    '''
    em = discord.Embed(title=r.callsign, url=f'https://qrz.com/db/{r.callsign}', description=rets, colour=0x00c0ff)
    em = em.set_footer(text='Source: hamqth.com')
    return em


'''
def get_call(message, mode):
    # setup
    s = ""
    ntitle = ""
    nmessage = ""
    splitmess = message.split()

    # error checking
    if len(splitmess) != 3:
        ntitle = "Syntax Error"
        nmessage = "Usage: !call callsign"

    else:
        # isolate call sign from message
        call = splitmess[2]

        # grab cool text-only website
        websource = urllib.request.urlopen("https://callook.info/" + call + "/text")
        for lines in websource.readlines():
            s += lines.decode("utf-8")

        # formatting
        ssplit = s.split('\n')

        # if a call sign was found
        if len(ssplit) > 1:
            #retrieve call sign
            tmp = ssplit[1].strip().split(':')
            ntitle = tmp[1]

            if mode == "simple":
                # cut out unneccessary crap
                ssplittmp = ssplit[2:-6]
                for i in range(0, len(ssplittmp)):
                    if ssplittmp[i].startswith('Previous Callsign:'):
                        del ssplittmp[i]
                        break
                for i in range(0, len(ssplittmp)):
                    if ssplittmp[i].startswith('Previous Class:'):
                        del ssplittmp[i]
                        break
                nmessage = '\n'.join(ssplittmp)
            else: nmessage = s

        # if no call sign was found
        else:
            ntitle = "Error"
            nmessage = "Call sign not found"

    return discord.Embed(title=ntitle, description=nmessage, colour=0x00c0ff)
'''


def morse(message):
    morse_message = ""
    splitmess = message.strip().split()
    if len(splitmess) == 2:
        return "You need to have a message, silly goose."

    splitmess = splitmess[2:]

    for word in splitmess:
        lowerword = word.lower()
        for letter in lowerword:
            if letter in tomorse:
                morse_message += tomorse[letter]
            else:
                morse_message += '<?>'
            morse_message += ' '
        morse_message += '/ '

    morse_message = morse_message[:-2]
    return morse_message


with open('.discordkey.txt', 'r') as f:
    lines = f.readlines()
    if len(lines) == 1:
        client.run(lines[0].strip())
