import discord
from discord.ext import commands

class upskill(commands.Cog):
  
  def __init_(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_message(self, message:str):
    
    if str(message).starts_with('ping'):
      await ctx.send('pong!')

    pass

  @commands.command()
  async def suggest(self, ctx, anonymous:bool=False, *, message:str):

    if anonymous:
      ctx.guild.owner.send(f'Somebody anonymously suggested/n{message}')
      await ctx.message.delete()

    else:
      ctx.guild.owner.send(f'{ctx.author} suggested/n{message}')
      await ctx.delete()
    
    await ctx.send(f"Your message has been sent to {ctx.guild.owner}", delete_after = 5)
    
def setup(client):
  client.add_cog(upskill(client))
