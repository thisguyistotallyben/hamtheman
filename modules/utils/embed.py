import discord
from discord.ext import commands


class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # requires state cog to be loaded
        self.state_service = bot.get_cog('StateCog')
        print(self.state_service)

    def generate(self, **kwargs):
        title = ''
        description = ''

        if 'title' in kwargs:
            title = kwargs['title']
        if 'description' in kwargs:
            description = kwargs['description']

        return discord.Embed(title=title,
                             description=description,
                             colour=self.state_service.get_color())


def setup(bot):
    bot.add_cog(EmbedCog(bot))