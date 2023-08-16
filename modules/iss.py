import discord
import json, urllib.request, pytz, time
import maidenhead as mh
from discord.ext import commands
from datetime import datetime
from timezonefinder import TimezoneFinder

def convert_utc_to_local(utc_timestamp, timezone_str):
    if timezone_str:
        timezone = pytz.timezone(timezone_str)
        utc_datetime = datetime.utcfromtimestamp(utc_timestamp)
        local_datetime = utc_datetime.replace(tzinfo=pytz.utc).astimezone(timezone)
        return local_datetime.strftime("%I:%M%p %Z")
    else:
        return None

class IssCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.embed_Service = bot.get_cog('EmbedCog')
        self.n2yoapi = bot.config['n2yo']

    @commands.command()
    async def iss(self, ctx, *, text: str = None):
        starttime = int(time.time())
        if text is None:
            await ctx.send("Usage: htm iss <gridsquare>")
            return
        elif self.n2yoapi == "0":
            await ctx.send("Please ask the host of this bot to sign up for API access at N2YO.com")
            return      
        else:
            grid = text
        try:
            lat = mh.to_location(grid)[0]
            lon = mh.to_location(grid)[1]
            tz_finder = TimezoneFinder()
            timezone_str = tz_finder.timezone_at(lng=lon, lat=lat)
        except:
            await ctx.send("Invalid grid square")
            return
        data = urllib.request.urlopen("https://api.n2yo.com/rest/v1/satellite/radiopasses/25544/" + str(lat) + "/" + str(lon) + "/150/1/5/&apiKey=" + self.n2yoapi + "").read()
        ISS = json.loads(data)

        passlist = []

        # This takes a three letter compass point (NNW, ESE) and makes it just two. I don't need it that precise!        
        def compasstrim(c):
            if (len(c) == 3):
                return c[1:]
            elif (len(c) == 1):
                return c.rjust(2, ' ')
            elif (len(c) == 2):
                return c

        for x in ISS['passes']:
            nicetime = convert_utc_to_local(x['startUTC'], timezone_str)
            if (nicetime[0] == '0'):
                nicetime = nicetime.lstrip('0')
                nicetime = " " + nicetime
            if (len(nicetime) == 6):
                nicetime = ' ' + nicetime
            if (len(str(round(x['maxEl']))) == 2):
                maxel = ' ' + str(round(x['maxEl']))
            elif (len(str(round(x['maxEl']))) == 1):
                maxel = '  ' + str(round(x['maxEl']))
            passlist.append('| ' + nicetime  + ' ' + compasstrim(x['startAzCompass']) + ' ->' + maxel + "°" + ' -> ' + compasstrim(x['endAzCompass']) + ' \n')
        separator = ', '
        items_as_strings = [str(item) for item in passlist]
        passstring = separator.join(items_as_strings)
        newpassstring = passstring.replace(separator, '')
        stoptime = int(time.time()) - starttime
        await ctx.send(embed=self.embed_Service
            .generate(
                title="ISS Passes for " + grid.upper(),
                description=f"```\n{newpassstring}\n```",
                footer="Processing time: " + str(stoptime) + " sec"
            )
        )

async def setup(bot):
        await bot.add_cog(IssCog(bot))