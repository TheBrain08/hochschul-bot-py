import datetime

import discord
from discord.ext import commands


class Welcomer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1159897549503742023)

        embed = discord.Embed(title=f'Willkommen auf dem {member.guild.name}  Server',
                              description=f'Willkommen {member.mention} auf unserem Server!\n\n'
                                            f'Du bist der {len(member.guild.members)}. User auf unserem Server!',
                              color=discord.Color.green())
        embed.set_thumbnail(url=member.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Welcomer(bot))
