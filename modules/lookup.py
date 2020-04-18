import os
import requests
import discord
from discord.ext import commands
from onlinelookup import hamqth, callook, olerror


class LookupCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cond(self, ctx):
        # remove possibly conficting old file
        if os.path.isfile("conditions.gif"):
            os.remove("conditions.gif")

        # download the latest conditions
        r = requests.get('https://www.hamqsl.com/solar101pic.php')
        open('conditions.gif', 'wb').write(r.content)

        with open('conditions.gif', 'rb') as f:
            await ctx.send(file=discord.File(f, 'conditions.gif'))

    @commands.command()
    async def call(self, ctx, callsign: str):
        await ctx.send(callsign)


def setup(bot):
    bot.add_cog(LookupCog(bot))

















# import os
# import requests
# import xml.etree.ElementTree as et
# import discord

# from hamtheman import bot, call_lookup
# from onlinelookup import olerror


# '''
# Callsign lookup

# param callsign: The callsign, which must be a string
# '''


# @bot.command()
# async def call(ctx, callsign: str, *, params: str=None):
#     if params is not None:
#         params = params.split()
#     print(callsign, params)

#     async with ctx.typing():
#         result = call_lookup.lookup(callsign, params)

#         # send it
#         await ctx.send(embed=result)


# '''
# Band conditions sourced from hamqsl
# '''


# @bot.command()
# async def cond(ctx):
#     async with ctx.typing():
#         # remove possibly conficting old file
#         if os.path.isfile("conditions.gif"):
#             os.remove("conditions.gif")

#         # download the latest conditions
#         r = requests.get('https://www.hamqsl.com/solar101pic.php')
#         open('conditions.gif', 'wb').write(r.content)

#         # send it
#         f = discord.File('conditions.gif')
#     await ctx.send(file=f)


# @bot.command()
# async def newcond(ctx):
#     r = requests.get('http://www.hamqsl.com/solarxml.php')

#     data = et.parse(r.content)
#     root = data.getroot()
#     print(root)
#     await ctx.send(r.content)
