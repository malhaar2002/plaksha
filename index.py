import discord
from discord.ext import commands
import os


print('Logging in...')
client = commands.Bot(command_prefix='plaksha ', intents=discord.Intents(guilds=True, members=True, messages=True, reactions=True, presences=True))
print('Logged in!   ')

Upskill_Dict = {
  'Leader_Board' :
    {
      'username': 'number_of_praises',
    },

  'tags' :
    {
      'Name_of_Tag': ['contents/links'],
    },
}



@client.command()
async def calling(ctx):

  commencement_date = '09/11/2021'
  days = "39 - today's date (october)"
  
  await ctx.send(f'Indeed, just {days} days before {commencement_date}')
  pass



@client.group(aliases=['learn'], invoke_without_command=True)
async def upskill(ctx):
  await ctx.send(create_embed())
  pass


@upskill.group(aliases=['fav', 'push'], invoke_without_command=True)
async def tag(ctx):
  if ctx.message.channel.category.id == 850043220020559933:
    if ctx.message.reference:
      if not(ctx.message.reference.fail_if_not_exists):
        await ctx.message.reply('Sorry this message may have been deleted!')
      else:
        await ctx.message.reference.reply('Please define what do you want to do with this message.\n> For creating a tag of this use ```plaksha upskill tag create NAME```')
    else:
      await ctx.message.reply('Please reply/refer to a message while tagging it.')
    


  else:
    category = discord.utils.get(ctx.guild.channels, id=850043220020559933)

    await ctx.reply(f'{ctx.author} this should be used inside one of {category}')

@tag.group(aliases=['+'], invoke_without_command=True)
async def create(ctx, name:str):
  pass
  
  


def create_embed():
  return 'Hm...'

# for filename in os.listdir('./cogs'):
#   if filename.endswith('.py'):
#     client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['DISCORD_TOKEN'])
