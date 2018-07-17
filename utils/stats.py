import discord
import time
from datetime import timedelta


class BotStats:
    def __init__(self, botname):
        self.name = botname
        self.discord_version = discord.__version__
        self.start_time = time.time()
        self.invite = 'https://discordapp.com/api/oauth2/authorize?client_id=368613435543650314&permissions=8&scope=bot'

    def uptime(self):
        up = str(timedelta(seconds=(time.time()-self.start_time)))

        # parse it pretty-like
        upsplit = up.split(',', 1)
        if len(upsplit) == 1:
            days = '0'
        else:
            days = upsplit[0].split()[0]
            upsplit[0] = upsplit[1]

        upsplit = upsplit[0].split(':')
        if len(upsplit) != 3:
            print('Something happened')
            return ''

        hours = upsplit[0]
        minutes = upsplit[1]
        seconds = upsplit[2].split('.', 1)[0]

        rets = f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds'

        return rets
