import datetime

import discord
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font


class WelcomerImage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1159897549503742023)

        background = Editor("bg.jpg")
        profile_image = await load_image_async(str(member.avatar_url))

        profile = Editor(profile_image).resize((220, 220)).circle_image()
        poppins = Font.poppins(size=50, variant="bold")

        poppins_small = Font.poppins(size=30)

        background.paste(profile, (450, 80))
        background.ellipse((450, 80), 220, 220, outline="white",stroke_width=5)

        background.text((550, 350), f"Welcome on {member.guild.name}", color="white", font=poppins, align="center")
        #background.text((550, 400), f"{member.display_name} du bist der {len(member.guild.members)} user auf dem Server", color="white", font=poppins_small, align="center")

        filer = File(fp=background.image_bytes, filename="bg.jpg")
        await channel.send(file=filer)

def setup(bot):
    bot.add_cog(WelcomerImage(bot))
