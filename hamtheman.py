# Author:  Benjamin Johnson (AB3NJ)
# Purpose: It performs various ham radio-related tasks

'''
ONE SMALL LITTLE BIT OF SETUP: PLEASE READ

Copy the file 'config_default.json' and name it 'config.json'.

Then, fill out the information inside of it with the appropriate data.

TODO: Put the config in the bot itself instead of weirdly passing it around in the state cog
'''

import time
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
    print('signing in...')

bot = HamTheManBot(command_prefix=commands.when_mentioned_or('!'))

# discord-y things
bot.remove_command('help')
bot.owner_id = config['owner id']

# custom variables
bot.start_time = time.time()
bot.config = config

for cog in cogs:
    bot.load_extension(cog)

bot.run(config['discord key'])
