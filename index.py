import discord
from discord.ext import commands
import os


print('Logging in...')
client = commands.Bot(command_prefix='plaksha ', intents=discord.Intents(guilds=True, members=True, messages=True, reactions=True, presences=True))
print('Logged in!   ')



@client.command()
async def calling(ctx):

  commencement_date = '09/11/2021'
  days = "39 - today's date (october)"
  
  await ctx.send(f'Indeed, just {days} days before {commencement_date}')
  pass



@client.group(name='upskill', invoke_without_command=True)
async def upskill(ctx):
  await ctx.send(create_embed())
  pass


@upskill.command(name='tag', invoke_without_command=True)
async def tag(ctx):
  if ctx.message.channel.category.id == 850043220020559933:
    if ctx.message.reference:
      await ctx.message.reference.reply('This?')



def create_embed():
  return 'Hm...'

# for filename in os.listdir('./cogs'):
#   if filename.endswith('.py'):
#     client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['DISCORD_TOKEN'])
