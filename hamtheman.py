# Author:  Benjamin Johnson
# Purpose: It performs various ham radio-related tasks


import discord
import asyncio
import os

from random import randint

import json

from utils.utc import utc
from utils.cond import cond
from utils import morse
from utils.onlinelookup import htmlookup


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
        if message.author == self.user:
            return
        print(message.author, 'in', message.channel)
        print('  ' + message.content)

        # split the message
        msplit = message.content.split(' ', 2)

        # htm * commands
        if msplit[0] == 'htm':
            # no content
            if len(msplit) == 1:
                return

            # get command
            command = msplit[1]

            # commands that do not need parameters
            if len(msplit) == 2:
                if command == 'utc':
                    await message.channel.send(embed=utc())
                elif command == 'cond':
                    await message.channel.send(file=cond())

            # commands that do need parameters
            elif len(msplit) == 3:
                par = msplit[2]
                if command == 'morse':
                    await message.channel.send(self.morse.translate_text(par))
                elif command == 'call':
                    print('here')
                    await message.channel.send(embed=self.ol.lookup(par))

        # non-htm * commands
        if msplit[0] == 'bonk' and len(msplit) == 1:
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
