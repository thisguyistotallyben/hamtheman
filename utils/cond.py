import discord
import os
import wget
import urllib
import urllib.request


def cond():
    if os.path.isfile("conditions.gif"):
        os.remove("conditions.gif")
    wget.download("http://www.hamqsl.com/solar101pic.php",
                  "conditions.gif", bar=None)
    # os.chmod("conditions.gif", 655)
    return discord.File('conditions.gif')
    # return await client.send_file(mess.channel, "conditions.gif")
