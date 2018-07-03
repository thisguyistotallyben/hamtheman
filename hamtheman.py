# Author:  Benjamin Johnson
# Purpose: It performs various ham radio-related tasks


import discord
import asyncio
import os
import wget
from random import randint
import urllib
import urllib.request
import json
from datetime import datetime

from onlinelookup import htmlookup
from morse import morse


block_list = []


class MyClient(discord.Client):
    def __init__(self):
        self.ol = htmlookup.HtmLookup()
        self.morse = morse.Morse()
        super().__init__()

    async def on_ready(self):
        # await client.change_presence(game=discord.Game(name="with Baofengs"))
        print('Shaking and also baking')
        print('-------------------------------')

    async def on_message(self, message):
        # do-not-reply
        if not message.content.startswith('htm'):
            return
        if message.author == self.user:
            return

        # htm * commands
        if message.content.startswith('htm'):
            msplit = message.content.split(' ', 2)
            print(msplit)

            # no content
            if len(msplit) == 1:
                return

            # get command
            command = msplit[1]

            # commands that do not need parameters
            if len(msplit) == 2:
                if command == 'utc':
                    await message.channel.send(embed=self.utc())

            # commands that do need parameters
            elif len(msplit) == 3:
                par = msplit[2]
                if command == 'morse':
                    await message.channel.send(self.morse.translate_text(par))
                elif command == 'call':
                    print('here')
                    await message.channel.send(embed=self.ol.lookup(par))

        '''
            with message.channel.typing():
                await asyncio.sleep(5.0)
                await message.channel.send('Done sleeping.')
        '''

    def utc(self):
        s = str(datetime.utcnow())
        ss = s.strip().split()
        date = ss[0]
        time = ss[1][0:8]

        etitle = 'Universal Coordinated Time'
        emess = "**Date:** " + date + "\n**Time:** " + time
        return discord.Embed(title=etitle, description=emess, colour=0x00c0ff)

with open('.discordkey.txt', 'r') as f:
    lines = f.readlines()
    if len(lines) == 1:
        client = MyClient()
        client.run(lines[0].strip())
