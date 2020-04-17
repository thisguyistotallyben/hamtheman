import discord
from discord.ext import commands


'''
TODO
    - Add 'admin only' rights to these commands because they would totally
      be abused
'''


class LoaderCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx, *, module: str):
        try:
            self.bot.load_extension(module)
            await ctx.send(f'{module} loaded')
        except:
            await ctx.send(f'module `{module}` not found')

    @commands.command()
    async def unload(self, ctx, *, module: str):
        ''' please do not delete yourself '''
        if module == 'module.loader':
            await ctx.send('No.')
            return

        try:
            self.bot.unload_extension(module)
            await ctx.send(f'{module} unloaded')
        except:
            await ctx.send(f'module `{module}` not found')

    @commands.command()
    async def reload(self, ctx, *, module: str):
        try:
            self.bot.reload_extension(module)
            await ctx.send(f'{module} reloaded')
        except:
            await ctx.send(f'module `{module}` not found')

    def cog_check(self, ctx):
        print('checking')
        return True


def setup(bot):
    bot.add_cog(LoaderCog(bot))