from discord.ext import commands

# nothing here for now
# need to make a proper embeding cog


class Beautify(commands.Cog):

    def __init__(self, client):
        self.bot = client


def setup(client):
    client.add_cog(Beautify(client))
