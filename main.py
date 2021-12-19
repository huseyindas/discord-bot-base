import logging
from discord.ext import commands

from config.settings import TOKEN, PREFIX
from utils.cogs import LoadCogs

client = commands.Bot(command_prefix=(PREFIX))

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


LoadCogs(client, './cogs')
logging.info("Bot is initializing...")

client.run(TOKEN)