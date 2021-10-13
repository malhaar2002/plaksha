# SOURCE: https://github.com/DXsmiley/LatexBot
# Method: Latex files in general linked with an image API

import discord
import urllib.request
import random
import os
import json
import shutil
import asyncio

import chanrestrict
from discord.ext import commands

LATEX_TEMPLATE = "template.tex"

HELP_MESSAGE = r"""
Hello! I'm the *LaTeX* math bot!
You can type mathematical *LaTeX* into the chat and I'll automatically render it!
Simply use the `!tex` command.
**Examples**
`!tex x = 7`
`!tex \sqrt{a^2 + b^2} = c`
`!tex \int_0^{2\pi} \sin{(4\theta)} \mathrm{d}\theta`
**Notes**
Using the `\begin` or `\end` in the *LaTeX* will probably result in something failing.
"""


class Latex(commands.Cog):
    # TODO: Check for bad token or login credentials using try catch
    def __init__(self, client):

        self.client = client

        self.check_for_config()
        self.settings = json.loads(open('settings.json').read())

        # Quick and dirty defaults of colour settings, if not already present in the settings
        if 'latex' not in self.settings:
            self.settings['latex'] = {
                'background-colour': '36393E',
                'text-colour': 'DBDBDB',
                'dpi': '200'
            }

        chanrestrict.setup(self.settings['channels']['whitelist'],
                           self.settings['channels']['blacklist'])

    # Check that config exists
    def check_for_config(self):
        if not os.path.isfile('settings.json'):
            shutil.copyfile('settings_default.json', 'settings.json')
            print('Now you can go and edit `settings.json`.')
            print('See README.md for more information on these settings.')

    def vprint(self, *args, **kwargs):
        if self.settings.get('verbose', False):
            print(*args, **kwargs)

    async def on_message(self, message):
        if chanrestrict.check(message):

            msg = message.content

            for c in self.settings['commands']['render']:
                if msg.startswith(c):
                    latex = msg[len(c):].strip()
                    self.vprint('Latex:', latex)

                    num = str(random.randint(0, 2 ** 31))
                    if self.settings['renderer'] == 'external':
                        fn = self.generate_image_online(latex)
                    if self.settings['renderer'] == 'local':
                        fn = self.generate_image(latex, num)
                        # raise Exception('TODO: Renable local generation')

                    if fn and os.path.getsize(fn) > 0:
                        await self.send_file(message.channel, fn)
                        self.cleanup_output_files(num)
                        self.vprint('Success!')
                    else:
                        await self.send_message(message.channel, 'Something broke. Check the syntax of your message. :frowning:')
                        self.cleanup_output_files(num)
                        self.vprint('Failure.')

                    break

            if msg in self.settings['commands']['help']:
                self.vprint('Showing help')
                await self.send_message(message.author, HELP_MESSAGE)

    # Generate LaTeX locally. Is there such things as rogue LaTeX code?
    def generate_image(self, latex, name):

        latex_file = name + '.tex'
        dvi_file = name + '.dvi'
        png_file = name + '1.png'

        with open(LATEX_TEMPLATE, 'r') as textemplatefile:
            textemplate = textemplatefile.read()

            with open(latex_file, 'w') as tex:
                backgroundcolour = self.settings['latex']['background-colour']
                textcolour = self.settings['latex']['text-colour']
                latex = textemplate.replace('__DATA__', latex).replace(
                    '__BGCOLOUR__', backgroundcolour).replace('__TEXTCOLOUR__', textcolour)

                tex.write(latex)
                tex.flush()
                tex.close()

        imagedpi = self.settings['latex']['dpi']
        latexsuccess = os.system(
            'latex -quiet -interaction=nonstopmode ' + latex_file)
        if latexsuccess == 0:
            os.system(
                'dvipng -q* -D {0} -T tight '.format(imagedpi) + dvi_file)
            return png_file
        else:
            return ''

    # More unpredictable, but probably safer for my computer.
    def generate_image_online(self, latex):
        url = 'http://frog.isima.fr/cgi-bin/bruno/tex2png--10.cgi?'
        url += urllib.parse.quote(latex, safe='')
        fn = str(random.randint(0, 2 ** 31)) + '.png'
        urllib.request.urlretrieve(url, fn)
        return fn

    # Removes the generated output files for a given name
    def cleanup_output_files(self, outputnum):
        try:
            os.remove(outputnum + '.tex')
            os.remove(outputnum + '.dvi')
            os.remove(outputnum + '.aux')
            os.remove(outputnum + '.log')
            os.remove(outputnum + '1.png')
        except OSError:
            pass


def setup(client):
    client.add_cog(Latex(client))
