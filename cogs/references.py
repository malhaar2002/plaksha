from discord.ext import commands
# This makes discord.ext.commands => commands


class References(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=['my_card', 'reference'], invoke_without_command=True)
    async def card(self, ctx):
        if ctx.message.reference:

            await ctx.send(f'What do you want to do with this message? Use \n> ```plaksha card create "YOUR_NAME"``` or Use\n> ```plaksha card add_field "Linked-In" "https://linkedin.com/Someone"```')
            await ctx.message.delete()

            return

        else:
            await ctx.message.reply('```Please reply to your card while making changes```')
            return

    @card.command(aliases=['+'])
    async def create(self, ctx, person=''):
        # registers an embed with title = Username
        return

    @card.command(aliases=['add_field'])
    async def field(self, ctx, field_name, field_url):
        # Edits the embed after verifying its yours
        return


def setup(client):
    client.add_cog(References(client))
