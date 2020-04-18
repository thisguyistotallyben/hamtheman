import discord
from discord.ext import commands


success_emoji = '✅'
fail_emoji = '❌'


class LoaderCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, module: str):
        try:
            self.bot.load_extension(self.get_module_path(module))
            await ctx.message.add_reaction(success_emoji)
        except Exception as e:
            await ctx.message.add_reaction(fail_emoji)

    @commands.command()
    @commands.is_owner()
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
    @commands.is_owner()
    async def reload(self, ctx, *, module: str):
        try:
            self.bot.reload_extension(self.get_module_path(module))
            await ctx.message.add_reaction(success_emoji)
        except Exception as e:
            await ctx.message.add_reaction(fail_emoji)

    def get_module_path(self, module):
        return f'modules.{module}'


def setup(bot):
    bot.add_cog(LoaderCog(bot))