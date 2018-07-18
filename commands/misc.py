from datetime import datetime

from core import *
from core import bot, help_embed, htm_kerchunk, htm_about


'''
UTC time
'''
@bot.command()
async def utc(ctx):
    s = str(datetime.utcnow())
    ss = s.strip().split()
    date = ss[0]
    time = ss[1][0:8]

    # send it
    em = discord.Embed(title='Universal Coordinated Time',
                       description=f'**Date:** {date}\n**Time:** {time}',
                       color=0x00c0ff)
    await ctx.send(embed=em)

'''
Kerchunk like a repeater
'''
@bot.command()
async def kerchunk(ctx):
    await ctx.send(htm_kerchunk)

'''
standards
'''
@bot.command()
async def standards(ctx):
    await ctx.send('https://xkcd.com/927')

'''
Help dialog
'''
@bot.command()
async def help(ctx):
    await ctx.send(embed=help_embed)

'''
About dialog
'''
@bot.command()
async def about(ctx):
    abstr = htm_about + calc_uptime()
    em = discord.Embed(title='About HamTheMan',
                       description=abstr,
                       color=0x00c0ff)
    em = em.set_footer(text='Licensed under the MIT License')

    # send it
    await ctx.send(embed=em)

'''
Uptime
'''
@bot.command()
async def uptime(ctx):
    await ctx.send(calc_uptime())
