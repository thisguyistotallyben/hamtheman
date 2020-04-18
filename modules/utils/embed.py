import discord
from discord.ext import commands


class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def generate(self, **kwargs):
        title = ''
        description = ''
        footer = ''

        if 'title' in kwargs:
            title = kwargs['title']
        if 'description' in kwargs:
            description = kwargs['description']
        if 'footer' in kwargs:
            footer = kwargs['footer']

        return discord.Embed(
            title=title,
            description=description,
            colour=self.bot.config['accent color']
        ).set_footer(text=footer)


def setup(bot):
    bot.add_cog(EmbedCog(bot))