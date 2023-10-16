import logging
import os
from pathlib import Path

import discord
from discord.ext import  commands

from dotenv import  load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('BOT-MAIN')

bot = commands.Bot(
    command_prefix=None,
    intents=discord.Intents.default(),
    activity=discord.Activity(type=discord.ActivityType.playing, name='auf AI WS23/24!'),
    status=discord.Status.online,
    sync_commands=True,
    delete_not_existing_commands=True
)

if __name__ == '__main__':
    log.info('Starting bot...')
    cogs = [file.stem for file in Path('cogs').glob('**/*.py') if not file.name.startswith('__')]
    log.info(f'Loading {len(cogs)} cogs...')

    for cog in cogs:
        bot.load_extension(f'cogs.{cog}')
        log.info(f'Loaded cog {cog}')
    token = os.getenv('BOT_TOKEN')
    bot.run(token)

@bot.event()
async def on_member_join(user):
    role = discord.utils.get(user.server.roles, id ='<1159897548446760981>')
    await bot.add_roles(user, role)