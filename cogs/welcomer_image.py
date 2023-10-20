import datetime

import discord
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font


class WelcomerImage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.slash_command(name='Bla', description='Starte eine Umfrage, die nur mit ja oder nein beantwortet '
                                                         'werden kann.')
    async def on_member_join(self, member):
        channel = self.bot.get_channel(953381552539189322)

        background = Editor('bg.png')
        profile_image = await load_image_async(str(member.avatar_url))

        profile = Editor(profile_image).resize((150,150)).circle_image()
        poppins = Font.poppins(size=50, variant="bold")

        poppins_small = Font.poppins(size=20, variant="light")

        background.paste(profile, (550, 250))
        background.ellipse((550,250), 150,150,outline="white",stroke_width=5)

        background.text((550,400),f"Welcome on {member.guild.name}", color="white", font=poppins, align="center")

        filer = File(fp=background.image_bytes, filename='bg.png')
        await channel.send(file=filer)

       """embed = discord.Embed(title=f'Willkommen auf dem {member.guild.name}  Server',
                              description=f'Willkommen Test auf unserem Server!\n\n'
                                            f'Du bist der {len(member.guild.members)}. User auf unserem Server!',
                              color=discord.Color.green())
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)"""

def setup(bot):
    bot.add_cog(WelcomerImage(bot))
