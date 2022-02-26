import discord
from discord.ext import commands

import sys
from datetime import datetime

from settings.utils import prefix

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['Nuke', 'NUKE', 'purge', 'Purge', 'PURGE'])
    async def nuke(self, ctx, amount=0):
        try:
            if amount > 10:
                warning_embed = discord.Embed(title='Safety Block', color=0xfffff, description='You cannot delete more than 10 messages at a time!')
                warning_embed.timestamp = datetime.now()
                await ctx.send(embed=warning_embed)
            else:
                await ctx.message.delete()
                async for message in ctx.message.channel.history(limit=amount):
                    if message.author.id == ctx.message.author.id:
                        await message.delete()
        except Exception as e:
            warning_embed = discord.Embed(title='Error!', color=0xfffff, description=f'{e}')
            warning_embed.timestamp = datetime.now()
            await ctx.send(embed=warning_embed)


def setup(bot):
    bot.add_cog(Help(bot))
