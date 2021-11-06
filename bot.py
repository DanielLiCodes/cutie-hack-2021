import discord
from discord.ext import commands
import random
from random import randint
import asyncio
import sys
import traceback
import requests
import aiohttp
import bs4
import os
import shelve
import math
from discord.ext.commands.cooldowns import BucketType



"""Py3.6, bot for tracking ender dragon summoners/runners"""


def get_prefix(bot, message):
    """Get the prefixes for the bot"""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['!']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return 'r^'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)


# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.registration']

bot = commands.Bot(command_prefix=get_prefix, description='bot to track ender dragon summons')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()



@bot.event
async def on_ready():
    """does on ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(activity=discord.Game(name="r^help in {} servers".format(len(bot.guilds))))
    print("in B)")  
    print("in spreadsheet too B))")


bot.run('OTA2NTY2MzEwNDUwODMxMzgw.YYafqw.y9Lu3mXbpP4XBQxIp8z2GJmCYRg', bot=True, reconnect=True)