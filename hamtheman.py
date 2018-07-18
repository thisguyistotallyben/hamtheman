# Author:  Benjamin Johnson
# Purpose: It performs various ham radio-related tasks


import discord

from core import bot
from commands import lookup, misc, morse


# startup stuff
@bot.event
async def on_ready():
    print('Shaking and Baking')

# every message goes through here
@bot.event
async def on_message(message):
    print('message received')

    # make case-insensitive
    message.content = message.content.lower()

    # process
    await bot.process_commands(message)

# run the bot
with open('keys/discord.txt', 'r') as f:
    lines = f.readlines()
    if len(lines) == 1:
        bot.run(lines[0].strip())
