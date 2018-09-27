import os
import requests
import discord

from core import bot, call_lookup
from onlinelookup import olerror


'''
Callsign lookup

param callsign: The callsign, which must be a string
'''
@bot.command()
async def call(ctx, callsign:str):
    with ctx.typing():
        result = call_lookup.lookup(callsign)

        # send it
        await ctx.send(embed=result)

'''
Band conditions sourced from hamqsl
'''
@bot.command()
async def cond(ctx):
    with ctx.typing():
        # remove possibly conficting old file
        if os.path.isfile("conditions.gif"):
            os.remove("conditions.gif")

        # download the latest conditions
        r = requests.get('https://www.hamqsl.com/solar101pic.php')
        open('conditions.gif', 'wb').write(r.content)

        # send it
        f = discord.File('conditions.gif')
        await ctx.send(file=f)
