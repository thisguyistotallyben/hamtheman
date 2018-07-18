import discord
from datetime import datetime


def utc():
    s = str(datetime.utcnow())
    ss = s.strip().split()
    date = ss[0]
    time = ss[1][0:8]

    etitle = 'Universal Coordinated Time'
    emess = "**Date:** " + date + "\n**Time:** " + time
    return discord.Embed(title=etitle, description=emess, colour=0x00c0ff)
