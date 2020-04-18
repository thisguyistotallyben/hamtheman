import discord
from discord.ext import commands


class ReactionsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.state = bot.get_cog('StateCog')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return

        if message.content.startswith('oof'):
            await message.channel.send('rip')
            self.state.get_config()['oofs'] += 1

    @commands.command()
    async def oofs(self, ctx):
        await ctx.send('Number of oofs since last reboot: ' +
            str(self.state.get_config()['oofs']))


def setup(bot):
    bot.add_cog(ReactionsCog(bot))