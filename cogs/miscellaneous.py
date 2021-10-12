from discord.ext import commands


# This for the member join event

class Miscellaneous(commands.Cog):

    def __init__(self, client):
        self.bot = client


def setup(client):
    client.add_cog(Miscellaneous(client))
