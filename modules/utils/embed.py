import discord
from discord.ext import commands


class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def generate(self, **kwargs):
        title = ''
        description = ''

        if 'title' in kwargs:
            title = kwargs['title']
        if 'description' in kwargs:
            description = kwargs['description']

        return discord.Embed(title=title,
                             description=description,
                             colour=self.bot.config['accent color'])


def setup(bot):
    bot.add_cog(EmbedCog(bot))