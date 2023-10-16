from discord.ext import commands
import discord


class auto_role(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = member.guild.get_role(1159897548446760981)
        await member.add_roles(role)


def setup(bot):
    bot.add_cog(auto_role(bot))
