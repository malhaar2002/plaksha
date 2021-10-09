import discord
from discord.ext import commands
import os


print('Logging in...')
client = commands.Bot(command_prefix='plaksha')
print('Logged in!   ')



@client.command()
async def calling(ctx):

  commencement_date = '09/11/2021'
  days = "39 - today's date (october)"
  
  await ctx.send(f'Indeed, just {days} days before {commencement_date}')
  pass

for filename in os.listdir('./cogs'):
  if filename.ends_with('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['DISCORD_TOKEN'])
