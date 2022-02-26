import discord
from discord.ext import commands

import sys
from datetime import datetime

from settings.utils import prefix

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['Help', 'HELP'])
    async def help(self, ctx):
        helpEmbed = discord.Embed(title='Command List', color=0xfffff,
        description=f'Prefix: {prefix}')
        helpEmbed.add_field(name='Gambling', value='`flip_bot`')
        helpEmbed.add_field(name='Misc', value='`help` `nuke`')
        helpEmbed.timestamp = datetime.now()

        await ctx.send(embed=helpEmbed)


def setup(bot):
    bot.add_cog(Help(bot))
