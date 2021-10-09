import discord
from discord.ext import commands


print('Logging in...')
client = commands.Bot(command_prefix='plaksha')
print('Logged in!   ')


client.command()
async def calling(ctx):

  commencement_date = '09/11/2021'
  days = "39 - today's date (october)"
  
  await ctx.send(f'Indeed, just {days} days before {commencement_date}')
  pass

client.run('ODkzNzkyNjg3OTA2NDk2NTUz.YVgnTg.rHAj8BEYwvmuAuHqjIv81RH2DyI')
