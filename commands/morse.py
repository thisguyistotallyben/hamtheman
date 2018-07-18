import discord

from core import bot, to_morse

'''
Translates from text to periods and dashes
'''
@bot.command()
async def morse(ctx, text:str):
    morsemess = ''
    for i in text:
        if i in to_morse:
            morsemess += to_morse[i]
        else:
            morsemess += '<?>'
        morsemess += '  '

    await ctx.send(morsemess)
