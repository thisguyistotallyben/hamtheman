import time
from datetime import timedelta
import discord
from discord.ext import commands

from onlinelookup import htmlookup


# lookups
call_lookup = htmlookup.HtmLookup()

# stats
start_time = time.time()

def calc_uptime():
    up = str(timedelta(seconds=(time.time()-start_time)))

    # parse it pretty-like
    upsplit = up.split(',', 1)
    if len(upsplit) == 1:
        days = '0'
    else:
        days = upsplit[0].split()[0]
        upsplit[0] = upsplit[1]

    upsplit = upsplit[0].split(':')
    if len(upsplit) != 3:
        print('Something happened')
        return ''

    hours = upsplit[0]
    minutes = upsplit[1]
    seconds = upsplit[2].split('.', 1)[0]

    rets = f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds'

    return rets

# morse lookups
to_morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': ' / '  # this is for spaces
}

from_morse = {
    '.-': 'a'  # TODO: finish this
}

""" common strings """

bonk = (':regional_indicator_b: '
            ':regional_indicator_o: '
            ':regional_indicator_n: '
            ':regional_indicator_k:')

boonk = (':regional_indicator_b: '
             ':regional_indicator_o: '
             ':regional_indicator_o: '
             ':regional_indicator_n: '
             ':regional_indicator_k:     '
             ':regional_indicator_g: '
             ':regional_indicator_a: '
             ':regional_indicator_n: '
             ':regional_indicator_g:')

htm_kerchunk = 'H...A...M...T...H...E...M...A...N...Repeater *kksshh*'

htm_about = ('**Author**\n'
             '\tBen Johnson, AB3NJ\n'
             '\tDiscord: thisguyistotallyben#3699\n'
             '\n**Tools**\n'
             '\tPython 3.6\n'
             '\tDiscord API v1.0.0\n'
             '\n**Data Sources**\n'
             '\tSolar conditions from hamqsl.com\n'
             '\tOnline callsign lookups from HamQTH and callook.info\n'
             '\n**Source Code**\n'
             '\thttps://github.com/thisguyistotallyben/hamtheman\n'
             '\n**Uptime**\n\t')

# help dialog
help_message = ('**Core commands**\n'
                '\t**cond**: Solar conditions (Source: hamqsl.com)\n'
                '\t**utc:**: Time in UTC\n'
                '\t**call [callsign]:** Callsign information (Sources: HamQTH, callook.info)\n'
                '\t**morse [message]:** Translates a message into morse code (use quotes)\n'
                '\n**#someta**\n'
                '\t**uptime:** Bot uptime\n'
                '\t**about:** About the bot\n'
                '\n**The sillier things in life**\n'
                '\t**kerchunk:** Pretend htm is a repeater\n'
                '\t**standards:** To remind us how standards proliferate\n'
                '\n**This bot is also responsible for the oofs and bonks**')

help_embed = discord.Embed(title='Help: Preface commands with \'htm\'',
                            description=help_message,
                            color=0x00c0ff)

# birth of a bot
bot = discord.ext.commands.Bot(command_prefix='htm ',
                               description=help_message)

# for custom help dialog
bot.remove_command('help')