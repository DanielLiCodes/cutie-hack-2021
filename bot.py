import discord
from discord.ext import commands
import asyncio
import sys
import os


"""Python bot to help facilitate tutoring!"""


def get_prefix(bot, message):
    """Get the prefixes for the bot"""
    prefixes = ['!']
    if not message.guild:
        return '!'
    return commands.when_mentioned_or(*prefixes)(bot, message)

initial_extensions = ['cogs.registration', 'cogs.search']

bot = commands.Bot(command_prefix=get_prefix, description='Bot to help facilitate tutoring and collaberation!')

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)

@bot.event
async def on_ready():
    """does on ready"""

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(activity=discord.Game(name="Register to find a mentor/mentee with !register".format(len(bot.guilds))))
    print("in B)")  

bot.run(os.getenv('TOKEN'), bot=True, reconnect=True)