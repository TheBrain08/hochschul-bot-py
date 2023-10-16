from discord.ext import commands
import discord


class auto_role(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, mmebers):
        role = discord.utils.get(mmebers.server.roles, id="1159897548446760981")
        await mmebers.add_roles(mmebers, role)


def setup(bot):
    bot.add_cog(auto_role(bot))
