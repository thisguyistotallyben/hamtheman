import discord
from discord.ext import commands


'''
I'm thinking for this, I'll have a main "entry" point of 'get' and 'set'

Set
- presence
'''


success_emoji = '✅'


class StateCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = {}
        self.bot_color = 0x00c0ff # TODO: make this from a config sometime

    @commands.command()
    @commands.is_owner()
    async def set(self, ctx, command: str, *, args: str):
        if command == 'status':
            await self.set_status(ctx, args)
        elif command =='color':
            self.set_color(args)

    async def set_status(self, ctx, text):
        await self.bot.change_presence(activity=discord.Game(text))
        await ctx.message.add_reaction(success_emoji)

    async def set_color(self, color):
        self.bot_color = color

    def set_config(self, config):
        self.config = config

    def get_config(self):
        return self.config

    def get_color(self):
        return self.bot_color


def setup(bot):
    bot.add_cog(StateCog(bot))