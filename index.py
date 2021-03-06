import discord
from discord.ext import commands
import os
from datetime import datetime


print('Logging in...')
client = commands.Bot(command_prefix='plaksha ', intents=discord.Intents(
    guilds=True, members=True, messages=True, reactions=True, presences=True))
print('Logged in!   ')


@client.command()
async def calling(ctx):
    days = 40 - datetime.now().day
    await ctx.send(f'Indeed, just {days} days before the 9th of November!')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.environ['DISCORD_TOKEN'])
