import os
import logging

logging.info("Cogs loading... This may take some time!")
def LoadCogs(client, folder):
    for filename in os.listdir(folder):
        if filename.endswith('.py'):
            folder_name = folder.replace(".", "").replace("/", ".").replace(".", "", 1)
            client.load_extension(f'{folder_name}.{filename[:-3]}')
            logging.info(f"{filename} cog is loaded!")
        if os.path.isdir(f'{folder}/{filename}'):
            LoadCogs(client, f'{folder}/{filename}')
