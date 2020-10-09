# Author:  Benjamin Johnson (AB3NJ)
# Purpose: It performs various ham radio-related tasks

'''
ONE SMALL LITTLE BIT OF SETUP: PLEASE READ

Copy the file 'config_default.json' and name it 'config.json'.

Then, fill out the information inside of it with the appropriate data.
'''

import time
import json
import discord
from discord.ext import commands


cogs = ['modules.state',
        'modules.utils.embed',
        'modules.loader',
        'modules.lookup',
        'modules.misc',
        'modules.morse',
        'modules.reactions']


class HamTheManBot(commands.Bot):
    async def on_ready(self):
        await self.change_presence(
            activity=discord.Game(name="with Baofengs | htm help"))
        print(f'  Username: {self.user}')
        print(f'  Servers:  {len(self.guilds)}')
        print('-----\nReady...')


# THIS IS WHERE THE MAGIC STARTS

print('WELCOME TO HAM THE MAN\n-----')

config = {}
with open('config.json', 'r') as f:
    print('loading config...')
    config = json.load(f)
    config['accent color'] = int(config['accent color'], 16)
    print('  config loaded.')

# this is a bit of a yikes, but it's an okay patch until I find out to actually do this
bot = HamTheManBot(command_prefix=['htm ', 'Htm ', 'hTm ', 'htM ', 'HTm ', 'hTM ', 'HTM '], case_insensitive=True)

# discord-y things
bot.remove_command('help')
bot.owner_id = config['owner id']

# custom variables
bot.start_time = time.time()
bot.config = config

print('loading extensions...')
for cog in cogs:
    bot.load_extension(cog)
print('  done.')
print('starting bot...')

bot.run(config['discord key'])
