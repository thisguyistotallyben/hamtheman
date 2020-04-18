import discord
from discord.ext import commands


class ReactionsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return

        if message.content.startswith('oof'):
            await message.channel.send('rip')
            self.bot.config['oofs'] += 1
        elif message.content == 'bonk':
            await message.channel.send((
                ':regional_indicator_b: '
                ':regional_indicator_o: '
                ':regional_indicator_n: '
                ':regional_indicator_k:'))
        elif message.content == 'boonk':
            await message.channel.send((
                ':regional_indicator_b: '
                ':regional_indicator_o: '
                ':regional_indicator_o: '
                ':regional_indicator_n: '
                ':regional_indicator_k:     '
                ':regional_indicator_g: '
                ':regional_indicator_a: '
                ':regional_indicator_n: '
                ':regional_indicator_g:'))

    @commands.command()
    async def oofs(self, ctx):
        await ctx.send('Number of oofs since last reboot: ' +
            str(self.bot.config['oofs']))


def setup(bot):
    bot.add_cog(ReactionsCog(bot))
