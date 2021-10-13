#  Satandard API calls
#  But it is interesting to note how these API generate these images
#  https://github.com/alvesvaren/QuickLaTeX-bot/blob/master/main.py

import multidict
import aiohttp.payload as payload
from urllib.parse import urlencode, quote
import asyncio

import discord
import aiohttp
from discord.ext import commands


class Latex(commands.Cog):

    def __init__(self, client):

        self.client = client

        self.default_data = {
            "fsize": "25px",
            "fcolor": "cccccc",
            "mode": 0,
            "out": 1,
            "errors": 1,
            "preamble": r"\usepackage{amsmath}\usepackage{amsfonts}\usepackage{amssymb}"
        }

    @commands.command(aliases=["l", "L"])
    async def latex(self, ctx: commands.Context, *, formula: str):
        async with aiohttp.ClientSession() as session:
            async with ctx.typing():

                embed = discord.Embed()
                form_data = self.CustomFormData()
                form_data.add_field("formula", formula)
                form_data.add_fields(multidict.MultiDict(self.default_data))

                async with session.post("https://www.quicklatex.com/latex3.f", data=form_data) as response:
                    formula_data = (await response.text()).splitlines()
                    if int(formula_data[0]) != 0:
                        await ctx.send("That isn't a valid latex expression")
                        await ctx.send(f"`{formula_data[2]}`")
                        return
                    image_url = formula_data[1].split()[0]
                    print("Sending", formula)
                    embed.set_image(url=image_url)
                    message: discord.Message = await ctx.message.reply(embed=embed)
            try:
                before, after = await self.client.wait_for("message_edit", check=lambda old, _: old.id == ctx.message.id, timeout=600)
                await message.delete()
                await self.client.process_commands(after)
            except asyncio.TimeoutError:
                pass

    class CustomFormData(aiohttp.FormData):
        def _gen_form_urlencoded(self) -> payload.BytesPayload:
            # form data (x-www-form-urlencoded)
            data = []
            for type_options, _, value in self._fields:
                data.append((type_options['name'], value))

            charset = self._charset if self._charset is not None else 'utf-8'

            if charset == 'utf-8':
                content_type = 'application/x-www-form-urlencoded'
            else:
                content_type = ('application/x-www-form-urlencoded; '
                                'charset=%s' % charset)

            return payload.BytesPayload(
                urlencode(data, doseq=False, encoding=charset,
                          quote_via=quote).encode(),
                content_type=content_type)


def setup(client):
    client.add_cog(Latex(client))
