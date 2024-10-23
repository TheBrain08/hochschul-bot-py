import calendar
import datetime

import discord
from discord.ext import commands , tasks
from datetime import datetime, timedelta, date

from main import bot

wochentage = ['tab-mon', 'tab-tue', 'tab-wed', 'tab-thu', 'tab-fri']


class EssenMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.slash_command(name='menu', description='Bekomme den Speißeplan gesendet ')
    #@commands.Cog.listener()
    #@tasks.loop(seconds=30.0)
    async def menu_command(self, ctx):  # ctx entfernen für später
        #channel = self.bot.get_channel(954094356988563467)
        #weekday = datetime.weekday(datetime.now())
        #if weekday == 1:

        for x in wochentage:
            embed = discord.Embed(title='Essen Menu von ' + str(open('./Essen/' + x + '-tag.txt', 'r').read()),
                                  color=discord.Color.blurple())
            embed.add_field(name='Essen 1',
                            value='```' + open('./Essen/' + x + '0.txt', 'r', encoding='windows-1252').read() + '```')
            embed.add_field(name='Essen 2',
                            value='```' + open('./Essen/' + x + '1.txt', 'r', encoding='windows-1252').read() + '```')
            embed.add_field(name='Buffet',
                            value='```' + open('./Essen/' + x + '2.txt', 'r', encoding='windows-1252').read() + '```')

            #embed.timestamp = datetime.utcnow()

            await ctx.respond(embed=embed)
            #await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(EssenMenu(bot))
