import discord
from discord.ext import commands


'''
TODO
    - Add 'admin only' rights to these commands because they would totally
      be abused
'''


class CogLoaderCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx, *, module: str):
        self.bot.load_extension(module)
        await ctx.send(f'{module} loaded')

    @commands.command()
    async def reload(self, ctx, *, module: str):
        self.bot.reload_extension(module)
        await ctx.send(f'{module} reloaded')


def setup(bot):
    bot.add_cog(CogLoaderCog(bot))