import discord
from discord.ext import commands

from onlinelookup import htmlookup

# birth of a bot
bot = commands.Bot(command_prefix='htm ', description='it is HamTheMan')

# lookups
call_lookup = htmlookup.HtmLookup()

# ## common strings ## #

help_message = ('**Core commands**\n'
                '  **cond**: Solar conditions (Source: hamqsl.com)\n'
                '  **utc:**: Time in UTC\n'
                '  **call [callsign]:** Callsign information (Sources: HamQTH, callook.info)\n'
                '  **morse [message]:** Translates a message into morse code\n'
                '\n**#someta**\n'
                '  **uptime:** Bot uptime\n'
                '\n**The sillier things in life**\n'
                '  **kerchunk:** Pretend htm is a repeater\n'
                '  **standards:** To remind us how standards proliferate\n'
                '\n**This bot is also responsible for the oofs and bonks**')

htm_bonk = (':regional_indicator_b: '
            ':regional_indicator_o: '
            ':regional_indicator_n: '
            ':regional_indicator_k:')

htm_boonk = (':regional_indicator_b: '
             ':regional_indicator_o: '
             ':regional_indicator_o: '
             ':regional_indicator_n: '
             ':regional_indicator_k:     '
             ':regional_indicator_g: '
             ':regional_indicator_a: '
             ':regional_indicator_n: '
             ':regional_indicator_g:')

htm_kerchunk = 'H...A...M...T...H...E...M...A...N...Repeater *kksshh*'
