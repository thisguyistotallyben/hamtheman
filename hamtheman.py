# Author:  Benjamin Johnson
# Purpose: It performs various ham radio-related tasks


import discord
import asyncio
import os
import socket

from random import randint

import json

from utils import morse
from utils import dbotsocket
from utils import stats
from utils.misc import *
from utils.utc import utc
from utils.cond import cond
from utils.onlinelookup import htmlookup


class MyClient(discord.Client):
    def __init__(self):
        self.ol = htmlookup.HtmLookup()
        self.morse = morse.Morse()
        self.stats = stats.BotStats('HamTheMan')
        #self.dbs = dbotsocket.DBotSocket(self, 50043)
        super().__init__()

    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name="with Baofengs | htm help"))
        print('Shaking and also baking')
        print('-------------------------------')

        # fill stats for dbotsocket
        #self.dbs.fill_stats(self)

    async def on_message(self, message):
        # do-not-reply
        if message.author == self.user:
            return
        print(f'{message.author} in {message.guild}: {message.channel}')
        print('  ' + message.content)

        # split the message
        msplit = message.content.lower().split(' ', 2)

        # htm * commands
        if msplit[0] == 'htm':
            # no content
            if len(msplit) == 1:
                return

            # get command
            command = msplit[1]

            # commands that do not need parameters
            if len(msplit) == 2:
                if command == 'help':
                    await message.channel.send(embed=htm_help)
                if command == 'utc':
                    await message.channel.send(embed=utc())
                elif command == 'cond':
                    await message.channel.send(file=cond())
                elif command == 'kerchunk':
                    await message.channel.send(htm_kerchunk)
                elif command == 'uptime':
                    await message.channel.send(self.stats.uptime())
                elif command == 'standards':
                    await message.channel.send('https://xkcd.com/927')

            # commands that do need parameters
            elif len(msplit) == 3:
                par = msplit[2]
                if command == 'morse':
                    await message.channel.send(self.morse.translate_text(par))
                elif command == 'call':
                    print('here')
                    await message.channel.send(embed=self.ol.lookup(par))


        # non-htm * commands
        if msplit[0] == 'oof':
            await message.channel.send('rip')
        elif msplit[0] == '||oof||':
            await message.channel.send('||rip||')    
        elif msplit[0] == 'bonk' and len(msplit) == 1:
            await message.channel.send(htm_bonk)
        elif msplit[0] == 'boonk':
            await message.channel.send(htm_boonk)

with open('.discordkey.txt', 'r') as f:
    lines = f.readlines()
    if len(lines) == 1:
        client = MyClient()
        client.run(lines[0].strip())
