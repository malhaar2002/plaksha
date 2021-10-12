import discord
from discord.enums import ContentFilter
from discord.ext import commands
from discord.ext.commands import context


class Tag(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self.Tag_Dict = {'first_name': ['content/links']}
        self.Alias_Dict = {'first_name': ['aliases']}

    def content_search(self, content):

        for first_name in self.Tag_Dict.keys():
            for content_element in self.Tag_Dict[first_name]:

                if content_element == content:

                    Name_List = list(self.Alias_Dict[first_name])
                    Name_List.append(first_name)
                    return Name_List, True

        else:

            return [''], False

    def name_search(self, name):

        for first_name in self.Tag_Dict.keys():

            if first_name == name:
                return self.Tag_Dict[name], True

            for alias_name in self.Alias_Dict[first_name]:

                if alias_name == name:
                    return self.Tag_Dict[name], True

        else:

            return [''], False

    @commands.group(aliases=['fav', 'push'], invoke_without_command=True)
    async def tag(self, ctx, *, tag_name: str = ''):

        # There may come a problem if + or create is somehow
        # registered as tag_name
        # Use  if __ and tag_name != '+' or tag_name != 'create'  ???

        Name_Search = (self.name_search(tag_name))

        if tag_name == '':

            await ctx.message.reply('```A help Message, no Name was provided```')
            return

        elif Name_Search[1]:

            await ctx.message.reply(f'```An embed\tHere is your content list for now:```{Name_Search[0]}')
            return

        elif not(Name_Search[1]):

            await ctx.message.reply('```I was not able to find a tag with that name!!```')
            return

        else:
            await ctx.message.reply('```py\n# Something unexpected happened, inside Class Tag, command Tag\nelse:\n\tawait ctx.message.reply()```')
            return

    @tag.group(aliases=['+'], invoke_without_command=True)
    async def create(self, ctx, *, tag_name: str = ''):
        pass

    @tag.group(aliases=['more'], invoke_without_command=True)
    async def more_over(self, ctx, *, tag_name: str = ''):
        await ctx.message.reply('```Um.. **more_over** method for Tag objects has not been coded | Wanna help? Contact Wizards of the server```')
        print(tag_name)

        return

    @tag.group(aliases=['remove', '-'], invoke_without_command=True)
    async def delete(self, ctx, *, tag_name: str = ''):
        await ctx.message.reply('```Um.. **delete** method for Tag objects has not been coded | Wanna help? Contact Wizards of the server```')
        print(tag_name)

        return

    @tag.group(aliases=['grab'], invoke_without_command=True)
    async def claim(self, ctx, *, tag_name: str = ''):
        await ctx.message.reply('```Um.. **claim** method for Tag objects has not been coded | Wanna help? Contact Wizards of the server```')
        print(tag_name)

        return


def setup(client):
    client.add_cog(Tag(client))
