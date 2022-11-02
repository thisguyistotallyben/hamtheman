# Author:  Benjamin Johnson (AB3NJ)
# Purpose: It performs various ham radio-related tasks

'''
ONE SMALL LITTLE BIT OF SETUP: PLEASE READ

Copy the file 'config_default.json' and name it 'config.json'.

Then, fill out the information inside of it with the appropriate data.
'''

import time
import json
import asyncio
import discord
from discord.ext import commands





class HamTheManBot(commands.Bot):
    cogs = ['modules.state',
        'modules.utils.embed',
        'modules.loader',
        'modules.lookup',
        'modules.misc',
        'modules.morse',
        'modules.reactions']
    
    config = {}
    start_time = time.time()

    def __init__(self, config) -> None:
        self.config = config

        super().__init__(
            command_prefix=['htm ', 'Htm ', 'hTm ', 'htM ', 'HTm ', 'hTM ', 'HTM '],
            intents=discord.Intents.all(),
            case_insensitive=True
        )

    async def on_ready(self):
        await self.change_presence(
            activity=discord.Game(name="with Baofengs | htm help"))
        print(f'  Username: {self.user}')
        print(f'  Servers:  {len(self.guilds)}')
        print('-----\nReady...')

        self.remove_command('help')
        self.owner_id = config['owner id']

        print('loading extensions...')
        for cog in self.cogs:
            await self.load_extension(cog)
        print('  done.')
        print('starting bot...')
        



# THIS IS WHERE THE MAGIC STARTS

print('WELCOME TO HAM THE MAN\n-----')

config = {}
with open('config.json', 'r') as f:
    print('loading config...')
    config = json.load(f)
    config['accent color'] = int(config['accent color'], 16)
    print('  config loaded.')

bot = HamTheManBot(config)
bot.run(config['discord key'])
