import logging
import discord
import random
from discord.ext import commands, tasks

from config.settings import TOKEN, PREFIX
from utils.cogs import LoadCogs

client = commands.Bot(command_prefix=(PREFIX))

@client.event
async def on_ready():
    logging.info("Bot is ready...")
    status.start()


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'src.{extension}')
    client.load_extension(f'src.{extension}')


@tasks.loop(seconds=10.0)
async def status():
    statuses = ["with you!", "with husoopy!", "with humans!"]
    await client.change_presence(activity=discord.Game(random.choice(statuses)))


LoadCogs(client, './src')

logging.info("Bot is initializing...")
client.run(TOKEN)