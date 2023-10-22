import calendar
import datetime

import discord
from discord.ext import commands
from datetime import datetime


class EssenMenu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.slash_command(name='menu', description='Bekomme Info\'s über einen User ')
    async def userinfo_command(self, ctx):

        embed = discord.Embed(title=f'Essen Menu der Woche {datetime.now().strftime("%d.%m.%Y")}', color=discord.Color.blurple())
        embed.add_field(name=' ', value=open('./Essen/tab-woche.txt','r').read())

        embed.timestamp = datetime.utcnow()
        embed.set_footer(text=f'Angefragt von {ctx.author}', icon_url=ctx.author.avatar_url)

        await ctx.respond(embed=embed, hidden=True)


def setup(bot):
    bot.add_cog(EssenMenu(bot))
