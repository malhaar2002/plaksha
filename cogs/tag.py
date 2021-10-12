import discord
from discord.enums import ContentFilter
from discord.ext import commands
from discord.ext.commands import context


class Tag(commands.Cog):
    # Plakshans I am sorry!! The code is not well commented
    # Neither the commands send Embeds, the Bot messages are ugly, I know
    # Only things left to solidify this approach is A database
    # The more-over, delete, and the claim sub-commands.

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

    @tag.command(aliases=['+'])
    async def create(self, ctx, *, tag_name: str = ''):

        if ctx.message.reference:
            if ctx.message.reference.fail_if_not_exists:

                Content_Search = self.content_search(tag_name)
                Name_Search = self.name_search(tag_name)

                if Content_Search[1] and not(Name_Search[1]):
                    self.Alias_Dict[Content_Search[0][-1]].append(tag_name)
                    await ctx.send(f'Added an alias!\nUse```plaksha tag {tag_name}```to reference it in the future!!')
                    return

                elif Name_Search[1]:
                    await ctx.message.reply(f'This tag name has already been used! use```plaksha tag {tag_name}```to see the contents of this tag\nOr use another name for the tag you want to create\n\nIf you want to add more content on the same tag name\nUse\n```plaksha tag more_over NAME```')
                    return

                elif not(Name_Search[1]):
                    self.Alias_Dict[tag_name] = []
                    self.Tag_Dict[tag_name] = []
                    self.Tag_Dict[tag_name].append(
                        (ctx.message.reference.resolved).content)
                    await ctx.send(f'Tag created.\nUse```plaksha tag {tag_name}```to access it in the future!!!!')

                else:
                    return

            else:

                await ctx.message.reply('```The message you replied to...maybe it has been deleted! If not contact the wizards of the server```')
                return

        else:
            await ctx.message.reply(f'```Please reply to a message/image/content while creating a tag for it!!```')
            return

    @tag.command(aliases=['more'], invoke_without_command=True)
    async def more_over(self, ctx, *, tag_name: str = ''):
        await ctx.message.reply('Um.. **more_over** method for Tag objects has not been coded | Wanna help?```Contact Wizards of the server```')
        print(tag_name)

    @tag.command(aliases=['remove', '-'], invoke_without_command=True)
    async def delete(self, ctx, *, tag_name: str = ''):
        await ctx.message.reply('Um.. **delete** method for Tag objects has not been coded | Wanna help?```Contact Wizards of the server```')
        print(tag_name)

        return

    @tag.command(aliases=['grab'], invoke_without_command=True)
    async def claim(self, ctx, *, tag_name: str = ''):
        await ctx.message.reply('Um.. **claim** method for Tag objects has not been coded | Wanna help?```Contact Wizards of the server```')
        print(tag_name)

        return


def setup(client):
    client.add_cog(Tag(client))
