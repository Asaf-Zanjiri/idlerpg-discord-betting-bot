import discord
from discord.ext import commands

import sys
from datetime import datetime

from settings.utils import prefix

from time import sleep
from math import floor
import re


class Flip_Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.enabled = False
        self.starting_balance = 0

    @commands.command(aliases=['Flip_bot', 'FLIP_BOT', 'flipbot', 'Flipbot', 'FLIPBOT'])
    async def flip_bot(self, ctx, state='enable'):
        self.ctx = ctx
        try:
            if (state == 'enable' or state =='start') and self.enabled == False:
                self.enabled = True
                response = await self.send_command('$bal')
                balance = int(re.search("\$([0-9,]*)", response).group(1).replace(',',''))
                self.starting_balance = balance
                await self.print_embed('Starting bot', f'Starting balance: {balance}\nMay your god be with you.')
                sleep(5)


                #algo
                amount = floor(balance/(2**20))
                start_balance = balance
                if amount == 0: amount = 1
                while self.enabled:
                    print(f'Betting: {amount} - {balance}')
                    response = await self.send_command(f'$flip {amount}')
                    if re.search('You won', response):
                        print('Won')
                        balance = balance + int(re.search("\$([0-9,]*)", response).group(1).replace(',',''))
                        start_balance = balance
                        amount = floor(balance/(2**20))
                        if amount == 0: amount = 1
                    elif re.search('You lost', response):
                        print('Lost')
                        balance = balance - int(re.search("\$([0-9,]*)", response).group(1).replace(',',''))
                        amount = amount*2
                        if amount+4>=(start_balance/4)-1:
                            await self.print_embed('Warning!', 'You\'ve excceeded the safe amount to bet.\nThe betting price has been reset')
                            amount = floor(balance/(2**20))
                    sleep(5)
            elif (state == 'disable' or state == 'stop') and self.enabled:
                self.enabled = False
                sleep(5)
                response = await self.send_command('$bal')
                balance = re.search("\$([0-9,]*)", response).group(1).replace(',','')
                await self.print_embed('Stopping bot', f'Starting balance: {self.starting_balance}.\nFinal balance: {balance}.\nHope u didnt lose it all my man. ily')
            else:
                await self.print_embed('Error!', 'Bot is already enabled/disabled.')
                
                
        except Exception as e:
            warning_embed = discord.Embed(title='Error!', color=0xfffff, description=f'{e}')
            warning_embed.timestamp = datetime.now()
            await ctx.send(embed=warning_embed)

    async def fetch_latest_message_from_bot(self, bot_id=424606447867789312):
        latest_message = await self.ctx.message.channel.history().find(lambda m: m.author.id == bot_id)
        return latest_message.content

    async def send_command(self, message):
        ''' Sends a command and returns the response from the bot '''
        await self.ctx.send(message)
        response = await self.fetch_latest_message_from_bot()
        while re.search('You are being rate-limited. Chill down', response):
            sleep(5)
            await self.ctx.send(message)
            response = await self.fetch_latest_message_from_bot()
        return response
    
    async def print_embed(self, title, description):
        enabled_embed = discord.Embed(title=title, color=0xfffff, description=description)
        enabled_embed.timestamp = datetime.now()
        await self.ctx.send(embed=enabled_embed)


def setup(bot):
    bot.add_cog(Flip_Bot(bot))
