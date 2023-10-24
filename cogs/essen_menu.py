import calendar
import datetime

import discord
from discord.ext import commands
from datetime import datetime, timedelta, date

wochentage = ['tab-mon','tab-tue','tab-wed','tab-thu','tab-fri']

class EssenMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.slash_command(name='menu', description='Bekomme den Speißeplan gesendet ')
    async def menu_command(self, ctx):
        my_dt = datetime(2024, 6, 21, 10, 12, 53)
        my_dt_trunc = date(my_dt.year,
                                    my_dt.month,
                                    my_dt.day)
        start_of_week = my_dt_trunc - timedelta(days=my_dt_trunc.weekday())

        end_of_week = start_of_week + timedelta(days=6)
        for x in wochentage:

            embed = discord.Embed(title='Essen Menu von' + str(open('./Essen/' + x + '-tag.txt', 'r').read()), color=discord.Color.blurple())
            embed.add_field(name='Essen 1',
                            value='```'+ open('./Essen/' + x + '0.txt', 'r', encoding='windows-1252').read() + '```')
            embed.add_field(name='Essen 2',
                            value='```' + open('./Essen/' + x + '1.txt', 'r', encoding='windows-1252').read() + '```')
            embed.add_field(name='Buffet',
                            value='```' + open('./Essen/' + x + '2.txt', 'r', encoding='windows-1252').read() + '```')

            embed.timestamp = datetime.utcnow()

            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(EssenMenu(bot))
