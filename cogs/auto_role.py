from discord.ext import commands
import discord

class auto_role(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listeners
    async def on_member_join(self, member):
        role = discord.utils.get(member.server.roles, id="1159897548446760981")
        await self.bot.add_roles(member, role)


def setup(bot):
    bot.add_cog(auto_role(bot))
