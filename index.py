import discord
from discord.ext import commands
import os


print('Logging in...')
client = commands.Bot(command_prefix='plaksha ', intents=discord.Intents(guilds=True, members=True, messages=True, reactions=True, presences=True))
print('Logged in!   ')

Tag_Dict = {
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


@client.group(aliases=['fav', 'push'], invoke_without_command=True)
async def tag(ctx, *, tag_name:str=''):
  if tag_name == '':
    if ctx.message.channel.category.id == 850043220020559933:
      if ctx.message.reference:
        if not(ctx.message.reference.fail_if_not_exists):
          await ctx.message.reply('Sorry this message may have been deleted!')
        else:
          await ctx.send('*Please define what do you want to do with this message.*\n> For **creating a tag** of this, Use ```plaksha upskill tag create NAME```', reference=ctx.message.reference)
      else:
        await ctx.message.reply('Please reply/refer to a message while tagging it.')
    else:
      category = discord.utils.get(ctx.guild.channels, id=850043220020559933)

      await ctx.reply(f'{ctx.author} this should be used inside one of {category}')

  else:
    # Add better search and nearby words later on
    if tag_name in Tag_Dict.keys():
      await ctx.send(f'{Tag_Dict[tag_name]}', reference=ctx.message.reference)
    else:
      await ctx.message.reply(f'There is no tag with this name\n> {tag_name}')
      




@tag.group(aliases=['+'], invoke_without_command=True)
async def create(ctx, *, tag_name:str=''):

  if tag_name != '':
    for name_element, content_element in Tag_Dict.items():
      if tag_name == name_element:
        await ctx.message.reply(f'{ctx.author.mention} ```There already exists a tag with this name!!```with content\n> {Tag_Dict[tag_name]}')
        return

      elif (ctx.message.reference.resolved).content == content_element:
        await ctx.send(f'{ctx.author.mention} There already exists a tag with this content!!\nWith the name\n> {name_element}', reference=ctx.message.reference)
        return

    else:
      Tag_Dict[tag_name] = (ctx.message.reference.resolved).content
      await ctx.message.reply(f'Tag was created! Use```plaksha upskill tag {tag_name}```To reference it in the future!!')
  else:
    await ctx.send(f'{(ctx.author).mention} Please input a NAME for the tag```plaksha upskill tag create NAME```', reference=ctx.message.reference)
  pass
  
  


def create_embed():
  return 'Hm...'

# for filename in os.listdir('./cogs'):
#   if filename.endswith('.py'):
#     client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['DISCORD_TOKEN'])
