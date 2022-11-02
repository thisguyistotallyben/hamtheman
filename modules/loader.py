import discord
from discord.ext import commands


success_emoji = '✅'
fail_emoji = '❌'


class LoaderCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def modules(self, ctx):
        all_modules = ''
        loaded_modules = ''

        for cog in self.bot.cogs:
            all_modules += cog.split('.', 1)[1] + '\n'

        for mod in self.bot.extensions.keys():
            loaded_modules += mod.split('.', 1)[1] + '\n'

        await ctx.send('**All modules:**\n' + all_modules + '\n**Loaded Modules:**\n' + loaded_modules)

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, module: str):
        try:
            await self.bot.load_extension(self.get_module_path(module))
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
            await self.bot.unload_extension(self.get_module_path(module))
            await ctx.message.add_reaction(success_emoji)
        except:
            await ctx.message.add_reaction(fail_emoji)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, module: str):
        try:
            await self.bot.reload_extension(self.get_module_path(module))
            await ctx.message.add_reaction(success_emoji)
        except Exception as e:
            await ctx.message.add_reaction(fail_emoji)

    def get_module_path(self, module):
        return f'modules.{module}'


async def setup(bot):
    await bot.add_cog(LoaderCog(bot))