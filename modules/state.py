import discord
from discord.ext import commands


success_emoji = '✅'
fail_emoji = '❌'


class StateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = {}

    '''
    setter entry point for
        - status
        - color
    '''
    @commands.command()
    @commands.is_owner()
    async def set(self, ctx, command: str, *, args: str):
        if command == 'status':
            await self.set_status(ctx, args)
        elif command =='color':
            await self.set_color(ctx, args)
        else:
            await ctx.message.add_reaction(fail_emoji)
            await ctx.send('That is not a valid setter')

    async def set_status(self, ctx, text):
        await self.bot.change_presence(activity=discord.Game(text))
        await ctx.message.add_reaction(success_emoji)

    async def set_color(self, ctx, color):
        try:
            self.bot.config['accent color'] = int(color, 16)
        except:
            await ctx.message.add_reaction(fail_emoji)


async def setup(bot):
    await bot.add_cog(StateCog(bot))