import discord

from hamtheman import bot

'''
Translates from text to periods and dashes
'''


@bot.command()
async def morse(ctx, *, text: str):
    morsemess = ''
    for i in text:
        if i in to_morse:
            morsemess += to_morse[i]
        else:
            morsemess += '<?>'
        morsemess += '  '

    await ctx.send(morsemess)


'''
LOOKUP TABLES
'''


to_morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': ' / '
}

from_morse = {
    '.-': 'a'  # TODO: finish this
}
