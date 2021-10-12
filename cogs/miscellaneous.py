from discord.ext import commands
from discord.utils import get
import discord


# This for the member join event

class Miscellaneous(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = get(member.guild.channels, id=833750512276471878)
        await member.add_roles(get(member.guild.roles, id=897167079176818729))

        if channel is not None:
            Welcome_Embed = discord.Embed(
                title="```Welcome to the Discord of Plaksha's Founding Cohort!```", description=f"-Student Community", color=0x007878)

            Welcome_Embed.add_field(
                name="Info to verify", value=f"> Please share your commitment letter with one of the {get(member.guild.roles, id=897302377705644043)}", inline=True)
            Welcome_Embed.add_field(
                name="Advice", value="> Get verified and gain access to the rest of the server 😄", inline=True)
            Welcome_Embed.add_field(
                name="Advice", value="A commitment letter looks like [this]('https://i.ibb.co/cgpq1r7/Offer-Acceptance-Letter-Plaksha-for-Discord.png')", inline=True)

            Welcome_Embed.set_footer(
                "If you're new to Discord, ['this video']('https://youtu.be/TJ13BA3-NR4') should be helpful")

            Welcome_Embed.set_thumbnail(
                'https://scet.berkeley.edu/wp-content/uploads/7.-Plaksha-Logo.jpeg')

            await channel.send(f'> Welcome {member.mention}\n> You are currently <>', embed=Welcome_Embed)


def setup(client):
    client.add_cog(Miscellaneous(client))