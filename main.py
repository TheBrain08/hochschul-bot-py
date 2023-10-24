import logging
import os
from pathlib import Path

import discord
from discord.ext import commands

from dotenv import load_dotenv
from Essen import scratchdelet

load_dotenv()

log = logging.getLogger('BOT-MAIN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or(),
    intents=intents,
    activity=discord.Activity(type=discord.ActivityType.playing, name='auf AI WS23/24!'),
    status=discord.Status.online,
    sync_commands=True,
    delete_not_existing_commands=True
)
scratchdelet.start()

if __name__ == '__main__':
    log.info('Starting bot...')
    cogs = [file.stem for file in Path('cogs').glob('**/*.py') if not file.name.startswith('__')]
    log.info(f'Loading {len(cogs)} cogs...')

    for cog in cogs:
        bot.load_extension(f'cogs.{cog}')
        log.info(f'Loaded cog {cog}')
    token = os.getenv('BOT_TOKEN')
    bot.run(token)



