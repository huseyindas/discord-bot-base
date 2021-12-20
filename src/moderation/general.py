from discord.ext import commands

from utils.prefix import ChangePrefix
from utils.restart import RestartBot

class GeneralCog(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def restart(self, ctx):
        await ctx.send("Yeniden başlıyorum...")
        RestartBot()
        
    @commands.command()
    async def prefix(self, ctx, prefix):
        ChangePrefix(prefix)
        await ctx.send("Lemon prefix'im değiştirildi. Yeniden başlıyorum...")
        RestartBot()


def setup(client):
    client.add_cog(GeneralCog(client))