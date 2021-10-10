import discord
from discord.ext import commands


class Tag(commands.Cog):

    Tag_Dict = {'first_name': ['content/links']}
    Alias_Dict = {'first_name': ['aliases']}

    def __init__(self, client):
        self.bot = client
        self.Tag_Dict = {'first_name': ['content/links']}
        self.Alias_Dict = {'first_name': ['aliases']}

    def tag_search(self, name, content):
        global Tag_Dict, Alias_Dict

        def content_search(self, content):
            content_present = False

            for first_name in self.Tag_Dict.keys():
                for content_element in self.Tag_Dict[first_name]:
                    if content_element == content:
                        content_present = True
                        return content_present
            else:
                content_present = False
                return content_present

        def name_search(self, name):
            name_present = False

            for first_name in self.Alias_Dict.keys():
                if first_name == name:
                    name_present = True
                    return name_present

                for alias_name in self.Alias_Dict[first_name]:
                    if alias_name == name:
                        name_present = True
                        return name_present

            else:
                name_present = False
                return name_present

        content_present = content_search(name)
        name_present = name_search(content)

        return content_present, name_present

    @commands.group(aliases=['fav', 'push'], invoke_without_command=True)
    async def tag(self, ctx, *, tag_name: str = ''):
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
            content_present, name_present = self.tag_search(tag_name, None)
            if name_present:
                await ctx.reply('Tag found!')

    @tag.group(aliases=['+'], invoke_without_command=True)
    async def create(self, ctx, *, tag_name: str = ''):

        if ctx.message.reference != None:

            if not(ctx.message.reference.fail_if_not_exists):
                await ctx.message.reply('Sorry this message may have been deleted!')

            else:

                if tag_name != '':

                    pass

                else:
                    await ctx.send(f'{(ctx.author).mention} Please input a NAME for the tag```plaksha tag create NAME```', reference=ctx.message.reference)
                pass

        else:
            await ctx.message.reply('Please reply/refer to a message while tagging it.')

    @tag.group(aliases=['more'], invoke_without_command=True)
    async def more_over(self, ctx, *, tag_name: str = ''):

        if ctx.message.reference:

            if not(ctx.message.reference.fail_if_not_exists):
                await ctx.message.reply('Sorry this message may have been deleted!')

            else:
                return

        else:
            ctx.message.reply(
                'Please reply/refer to a message while tagging it.')


def setup(client):
    client.add_cog(Tag(client))
