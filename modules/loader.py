import discord
from discord.ext import commands


'''
TODO
    - Add 'admin only' rights to these commands because they would totally
      be abused
'''

success_emoji = '✅'
fail_emoji = '❌'


class LoaderCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx, *, module: str):
        try:
            self.bot.load_extension(self.get_module_path(module))
            await ctx.message.add_reaction(success_emoji)
        except Exception as e:
            await ctx.message.add_reaction(fail_emoji)
            print(e)

    @commands.command()
    async def unload(self, ctx, *, module: str):
        ''' please do not delete yourself '''
        if module == 'loader':
            await ctx.send('No.')
            return

        try:
            self.bot.unload_extension(self.get_module_path(module))
            await ctx.message.add_reaction(success_emoji)
        except:
            await ctx.message.add_reaction(fail_emoji)

    @commands.command()
    async def reload(self, ctx, *, module: str):
        try:
            self.bot.reload_extension(self.get_module_path(module))
            await ctx.message.add_reaction(success_emoji)
        except:
            await ctx.message.add_reaction(fail_emoji)

    def cog_check(self, ctx):
        return True

    def get_module_path(self, module):
        return f'modules.{module}'


def setup(bot):
    bot.add_cog(LoaderCog(bot))