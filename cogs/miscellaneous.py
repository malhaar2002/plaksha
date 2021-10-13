from discord.ext import commands
from discord.utils import get
import discord
import time
import asyncio


# This for the member join event

class Miscellaneous(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(
            member.guild.channels, id=833750512276471878)
        await member.add_roles(get(member.guild.roles, id=834114153412296706))

        if channel is not None:
            Welcome_Embed = discord.Embed(
                title="```Discord of Plaksha's Founding Cohort!```", description=f"-Student Community", color=0x007878)

            Welcome_Embed.add_field(
                name="Info to verify", value=f"> Please share your offer letter with one of the {get(member.guild.roles, id=897302377705644043)}", inline=True)

            Welcome_Embed.add_field(
                name="Advice", value="> **Get verified and gain access to the rest of the server 😄**", inline=True)

            Welcome_Embed.add_field(
                name="Reference", value="> An **offer-letter** similar to [this](https://i.ibb.co/cgpq1r7/Offer-Acceptance-Letter-Plaksha-for-Discord.png) commitment letter", inline=True)

            Welcome_Embed.add_field(
                name="Welcome Again", value="> If you're new to Discord, [this video](https://youtu.be/TJ13BA3-NR4) should be helpful", inline=True)

            Welcome_Embed.set_thumbnail(
                url='https://scet.berkeley.edu/wp-content/uploads/7.-Plaksha-Logo.jpeg')
            Welcome_Embed.set_image(
                url='https://i.ibb.co/cgpq1r7/Offer-Acceptance-Letter-Plaksha-for-Discord.png')

            await channel.send(f"> Welcome {member.mention}\n> You are currently {(get(member.guild.roles, id=834114153412296706)).mention}\n\u200b", embed=Welcome_Embed)

    @commands.command()
    async def ping(self, ctx: commands.Context):

        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(content=f"🏓 Pong!```{round(self.client.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms```")

    @commands.command(aliases=['burn'], pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, amount: int):

        await ctx.channel.purge(limit=amount, check=lambda message: message.pinned == False)

        resp_ = await ctx.send(f'```🧹 {amount} messages were cleaned` by {ctx.author}``')
        asyncio.sleep(5)
        await resp_.delete()


def setup(client):
    client.add_cog(Miscellaneous(client))
