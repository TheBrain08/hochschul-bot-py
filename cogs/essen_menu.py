import calendar
import datetime

import discord
from discord.ext import commands
from datetime import datetime

wochentage = ['tab-mon','tab-tue','tab-wed','tab-thu','tab-fri']

class EssenMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.slash_command(name='menu', description='Bekomme den Speißeplan gesendet ')
    async def menu_command(self, ctx):

        embed = discord.Embed(title=f'Essen Menu der Woche {datetime.now().strftime("%d.%m.%Y")}', color=discord.Color.blurple())
        for x in wochentage:
            embed.add_field(name=open('./Essen/'+x + '-tag.txt', 'r',encoding='windows-1252').read() , value='```'+ open('./Essen/'+x +'.txt','r',encoding='windows-1252').read() + '```')

        embed.timestamp = datetime.utcnow()
        embed.set_footer(text=f'Angefragt von {ctx.author}', icon_url=ctx.author.avatar_url)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(EssenMenu(bot))
