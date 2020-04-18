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
