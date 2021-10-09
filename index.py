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



Tag_Dict = {
  ['Name_of_Tag'] : ['contents/links']
}

@client.group(aliases=['fav', 'push'], invoke_without_command=True)
async def tag(ctx, *, tag_name:str=''):
  if tag_name == '':
    # Send a help command here
    if ctx.message.reference != None:
      if not(ctx.message.reference.fail_if_not_exists):
        await ctx.message.reply('Sorry this message may have been deleted!')
      else:
        await ctx.send('*Please define what do you want to do with this message.*\n> For **creating a tag** of this, Use ```plaksha tag create NAME```', reference=ctx.message.reference)
    else:
      await ctx.message.reply('Please reply/refer to a message while tagging it.')

  else:
    # Add better search and nearby words later on
    for tag_name_list in Tag_Dict.keys():
      if tag_name in tag_name_list:
        await ctx.send(f'{Tag_Dict[tag_name_list]}', reference=ctx.message.reference)
        return
    else:
      await ctx.message.reply(f'There is no tag with this name {tag_name}\n> Use:```plaksha tag create NAME```')

@tag.group(aliases=['+'], invoke_without_command=True)
async def create(ctx, *, tag_name:str=''):

  if ctx.message.reference != None:
    if not(ctx.message.reference.fail_if_not_exists):
      await ctx.message.reply('Sorry this message may have been deleted!')
    else:
      await ctx.send('*Please define what do you want to do with this message.*\n> For **creating a tag** of this, Use ```plaksha tag create NAME```', reference=ctx.message.reference)
  else:
    await ctx.message.reply('Please reply/refer to a message while tagging it.')

  if tag_name != '':
    for name_element_list, content_element_list in Tag_Dict.items():
      if tag_name in name_element_list:
        await ctx.message.reply(f'{ctx.author.mention} ```There already exists a tag with this name {tag_name}!!```with content\n> {Tag_Dict[tag_name]}\n')
        await ctx.send(f'Add this content to this ****')
        return
    elif (ctx.message.reference.resolved).content

    else:
      Tag_Dict[tag_name] = (ctx.message.reference.resolved).content
      await ctx.message.reply(f'Tag was created! Use```plaksha tag {tag_name}```To reference it in the future!!')
  else:
    await ctx.send(f'{(ctx.author).mention} Please input a NAME for the tag```plaksha tag create NAME```', reference=ctx.message.reference)
  pass
  
  


def create_embed():
  return 'Hm...'

# for filename in os.listdir('./cogs'):
#   if filename.endswith('.py'):
#     client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.environ['DISCORD_TOKEN'])
