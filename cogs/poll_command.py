import datetime

import discord
from discord.ext import commands



class PollCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.slash_command(name='Poll', description='Starte eine Umfrage')
    async def poll_command(self, ctx, *args):

        embed = discord.Embed(title=f'Umfrage 📊',
                              description=f'{" ".join(args)}', color='red')
        #embed.set_thumbnail(url="https://i.ibb.co/yy80FHf/analytics-max-removebg-preview.png")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'Erstellt von {ctx.author} • ', icon_url=ctx.author.avatar_url)

        await ctx.respond(embed=embed)
        """await message.add_reaction('✔️')
        await message.add_reaction('❌')"""



def setup(bot):
    bot.add_cog(PollCommand(bot))
