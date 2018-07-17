# miscellaneous commands


import discord


# common strings

help_message = ("**morse [message]:** Translates a message into morse code\n"
                "**cond:** Gives solar conditions\n"
                "**call [callsign]:** gives information on a call sign\n"
                "**utc:** gives the time in UTC\n"
                "**kerchunk:** pretend htm is a repeater\n"
                "\n**This bot is also responsible for the oofs and bonks**")

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

# help embed
htm_help = discord.Embed(tite='Help: Preface commands with \'htm\'',
                            description=help_message,
                            color=0x00c0ff)
