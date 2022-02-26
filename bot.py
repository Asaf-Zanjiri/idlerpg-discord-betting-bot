import discord
from discord.ext import commands

import os
from settings.utils import token, prefix

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')

# Goes over all of the python command files
for command in os.listdir('./commands'):
    if command.endswith('.py') and command != 'utils.py':
        bot.load_extension(f'commands.{command[:-3]}')




print('Bot started..')
bot.run(token, bot=False)
