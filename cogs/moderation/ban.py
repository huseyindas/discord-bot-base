from discord.ext import commands

class BanCog(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def foo(self, ctx):
        print("command working")
        return False

    @commands.command(hidden=False)
    async def bar(self, ctx):
        print("command working")
        return True

def setup(client):
    client.add_cog(BanCog(client))