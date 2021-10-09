import discord
import discord.ext import commands

class upskill(commands.Cog):
  
  def __init_(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_message(message:str):
    
    if message.starts_with(ping):
      await ctx.send(pong!)

    pass

  @commands.command()
  async def suggest(ctx, anonymous:bool=False, *, message:str):

    if anonymous:
      ctx.guild.owner.send(f'Somebody anonymously suggested/n{message}')
      await ctx.message.delete()

    else:
      ctx.guild.owner.send(f'{ctx.author} suggested/n{message}')
      await ctx.delete()
    
    await ctx.send(f"Your message has been sent to {ctx.guild.owner}", delete_after = 5)
    
def setup(client):
  client.add_cog(upskill(client))
