import discord
from discord.ext import commands

class Tag(commands.Cog):

  def __init__(self, bot):
    self.bot = bot


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

        if tag_name != '':


          for name_element_list, content_element_list in Tag_Dict.items():

            if tag_name in name_element_list:

              await ctx.message.reply(f'{ctx.author.mention}\n> There already exists a tag with this name {tag_name}!!\nwith content\n> {Tag_Dict[tag_name]}\nIf you want to add stuff in this tag Use:```plaksha tag more_over Name```')
              return

            elif (ctx.message.reference.resolved).content in content_element_list:

              del Tag_Dict[name_element_list]
              name_element_list.append(tag_name)

              Tag_Dict[name_element_list] = content_element_list

              await ctx.send(f'This content is already tagged, added an alias for this content! Use```plaksha tag {tag_name}```To reference it in the future!!', refeerence=ctx.message.reference)
              return

          else:
            Tag_Dict[[tag_name]] = [(ctx.message.reference.resolved).content]
            await ctx.message.reply(f'Tag was created! Use```plaksha tag {tag_name}```To reference it in the future!!')



        else:
          await ctx.send(f'{(ctx.author).mention} Please input a NAME for the tag```plaksha tag create NAME```', reference=ctx.message.reference)
        pass

    else:
      await ctx.message.reply('Please reply/refer to a message while tagging it.')



  @tag.group(aliases=['more'], invoke_without_command=True)
  async def more_over(ctx, *, tag_name:str=''):

    if ctx.message.reference:

      if not(ctx.message.reference.fail_if_not_exists):
        await ctx.message.reply('Sorry this message may have been deleted!')

      else:

        for name_element_list, content_element_list in Tag_Dict.items():

          if tag_name in name_element_list:

            # CONTENT VS NAME create a function to check both at the same time

            Tag_Dict[name_element_list] = content_element.append(ctx.message.reference.resolved.content)
            return


    else:
      ctx.message.reply('Please reply/refer to a message while tagging it.')



def setup(client):
  client.add_cog(Tag(client))
