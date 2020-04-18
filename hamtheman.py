# Author:  Benjamin Johnson (AB3NJ)
# Purpose: It performs various ham radio-related tasks

'''
ONE SMALL LITTLE BIT OF SETUP: PLEASE READ

Copy the file 'config_default.json' and name it 'config.json'.

Then, fill out the information inside of it with the appropriate data.
'''


import json
import discord
from discord.ext import commands


cogs = ['modules.state',
        'modules.utils.embed',
        'modules.morse',
        'modules.loader',
        'modules.misc',
        'modules.reactions']


class HamTheManBot(commands.Bot):
    async def on_ready(self):
        await self.change_presence(
            activity=discord.Game(name="with Baofengs | htm help"))
        print('Beep boop I am {0}'.format(self.user))


# THIS IS WHERE THE MAGIC STARTS

config = {}
with open('config.json', 'r') as f:
    config = json.load(f)
    print('config loaded')

bot = HamTheManBot(command_prefix=commands.when_mentioned_or('!'))

bot.remove_command('help')
bot.owner_id = config['owner id']

for cog in cogs:
    bot.load_extension(cog)

bot.get_cog('StateCog').set_config(config)
bot.run(config['discord key'])




















# import json
# import discord

# from commands import lookup, misc, morse


# '''
# STARTUP THINGS
# '''

# # master config
# config = {}
# with open('config.json', 'r') as f:
#     config = json.load(f)
#     print('config loaded')

# # for calculating uptime
# start_time = time.time()

# # for looking up callsigns
# call_lookup = htmlookup.HtmLookup()


# '''
# DISCORD STUFF
# '''





# # startup stuff
# @bot.event
# async def on_ready():
#     await bot.change_presence(
#         activity=discord.Game(name="with Baofengs | htm help"))
#     print('Shaking and Baking')


# # every message goes through here
# @bot.event
# async def on_message(message):
#     # make case-insensitive
#     message.content = message.content.lower()

#     # get the bonks, boonks, and the oofs
#     # TODO: Make a thread that periodically saves the oof count
#     if message.content == 'oof':
#         config['oofs'] += 1
#         await message.channel.send('rip')
#     elif message.content == 'bonk':
#         await message.channel.send(bonk)
#     elif message.content.startswith('boonk'):
#         await message.channel.send(boonk)

#     # process everything else
#     else:
#         await bot.process_commands(message)

# # run the bot
# with open('keys/discord.txt', 'r') as f:
#     lines = f.readlines()
#     if len(lines) == 1:
#         bot.run(lines[0].strip())


# '''
# STRINGS AND STUFF
# '''


# bonk = (':regional_indicator_b: '
#         ':regional_indicator_o: '
#         ':regional_indicator_n: '
#         ':regional_indicator_k:')

# boonk = (':regional_indicator_b: '
#          ':regional_indicator_o: '
#          ':regional_indicator_o: '
#          ':regional_indicator_n: '
#          ':regional_indicator_k:     '
#          ':regional_indicator_g: '
#          ':regional_indicator_a: '
#          ':regional_indicator_n: '
#          ':regional_indicator_g:')

# bot = discord.ext.commands.Bot(command_prefix=config['prefix'])
# bot.remove_command('help')
