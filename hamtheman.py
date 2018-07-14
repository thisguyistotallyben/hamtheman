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
from utils.utc import utc
from utils.cond import cond
from utils.onlinelookup import htmlookup


block_list = []

help_message = ("**morse [message]:** Translates a message into morse code\n"
                "**cond:** Gives solar conditions\n"
                "**call [callsign]:** gives information on a call sign\n"
                "**utc:** gives the time in UTC\n"
                "**kerchunk:** pretend htm is a repeater\n"
                "\n**This bot is also responsible for the oofs and bonks**")


class MyClient(discord.Client):
    def __init__(self):
        self.ol = htmlookup.HtmLookup()
        self.morse = morse.Morse()
        self.dbs = dbotsocket.DBotSocket(self, 50043)
        super().__init__()

    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name="with Baofengs"))
        print('Shaking and also baking')
        print('-------------------------------')

        # fill stats for dbotsocket
        self.dbs.fill_stats(self)

    async def on_message(self, message):
        # do-not-reply
        if message.author == self.user:
            return
        print(message.author, 'in', message.channel)
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
                    em = discord.Embed(title='Help (Preface commands with \'htm\')', description=help_message, colour=0x00c0ff)
                    await message.channel.send(embed=em)
                if command == 'utc':
                    await message.channel.send(embed=utc())
                elif command == 'cond':
                    await message.channel.send(file=cond())
                elif command == 'kerchunk':
                    await message.channel.send('H...A...M...T...H...E...M...A...N...Repeater *kksshh*')

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
        elif msplit[0] == 'bonk' and len(msplit) == 1:
            await message.channel.send(':regional_indicator_b: '
                                       ':regional_indicator_o: '
                                       ':regional_indicator_n: '
                                       ':regional_indicator_k:')
        elif msplit[0] == 'boonk':
            await message.channel.send(':regional_indicator_b: '
                                       ':regional_indicator_o: '
                                       ':regional_indicator_o: '
                                       ':regional_indicator_n: '
                                       ':regional_indicator_k:     '
                                       ':regional_indicator_g: '
                                       ':regional_indicator_a: '
                                       ':regional_indicator_n: '
                                       ':regional_indicator_g:')

with open('.discordkey.txt', 'r') as f:
    lines = f.readlines()
    if len(lines) == 1:
        client = MyClient()
        client.run(lines[0].strip())
