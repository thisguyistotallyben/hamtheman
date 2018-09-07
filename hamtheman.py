# Author:  Benjamin Johnson
# Purpose: It performs various ham radio-related tasks


import discord

import core
from core import bot, bonk, boonk
from commands import lookup, misc, morse


# startup stuff
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="with Baofengs | htm help"))
    print('Shaking and Baking')

# every message goes through here
@bot.event
async def on_message(message):
    # make case-insensitive
    message.content = message.content.lower()

    # get the bonks, boonks, and the oofs
    if message.content == 'oof':
        core.oof_count += 1
        print(core.oof_count)
        await message.channel.send('rip')
    elif message.content == 'bonk':
        await message.channel.send(bonk)
    elif message.content.startswith('boonk'):
        await message.channel.send(boonk)

    # process everything else
    else:
        await bot.process_commands(message)

# run the bot
with open('keys/discord.txt', 'r') as f:
    lines = f.readlines()
    if len(lines) == 1:
        bot.run(lines[0].strip())
