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




##@bot.event
##async def on_command_error(ctx, error):
##    if hasattr(ctx.command, 'on_error'):
##        return
##    
##    ignored = (commands.CommandNotFound, commands.UserInputError)
##    error = getattr(error, 'original', error)
##    
##    if isinstance(error, ignored):
##        return
##    
##    elif isinstance(error, commands.CommandOnCooldown):
##        timeInSeconds = error.retry_after
##        if timeInSeconds > 3600:
##            hours = timeInSeconds / 3600
##            ppe = math.floor(hours)*3600
##            numberOfSecondsWithoutHours = timeInSeconds - ppe
##            minutes = numberOfSecondsWithoutHours / 60
##            return await ctx.send("This command is on cooldown for {0} hour(s), and {1} minute(s).".format(math.floor(hours), round(minutes)))
##        if timeInSeconds < 60:
##            return await ctx.send("This command is on cooldown for {} seconds().".format(round(timeInSeconds)))
##        minutes = timeInSeconds / 60
##        ppe = minutes * 60
##        seconds = timeInSeconds - ppe
##        return await ctx.send("This command is on cooldown for {0} minute(s) and {1} seconds".format(round(minutes), round(seconds)))
##    
##
##    elif isinstance(error, commands.MissingPermissions):
##        return await ctx.send("No perms :(")
##    
##    elif isinstance(error, commands.CheckFailure):
##        return await ctx.send("You are missing a role that you need :(")
##
##    elif isinstance(error, discord.NotFound):
##        return await ctx.send("I could not find this member")
##    
##    elif isinstance(error, commands.BadArgument):z
##        return await ctx.send('I could not find that member. Please try again.') 
##
##    
##        
##    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
##    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
 

bot.run('OTA2NTY2MzEwNDUwODMxMzgw.YYafqw.HT1hNvKGYMSBHZj9Qn56-zipM6g', bot=True, reconnect=True)