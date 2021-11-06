
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext
import sys
import os

from discord import activity
cogs = ["cogs.registration"]


if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = discord.Intents.default()
bot = Bot(command_prefix=config["bot_prefix"], intents=intents)


# The code in this even is executed when the bot is ready
@bot.event
async def on_ready():
    print(f"Bot is up!")
    await bot.change_presence(activity=discord.Game(name="Tutoring {} students!"))



if __name__ == "__main__":
    for cog in cogs:
        try:
            bot.load_extension(cog)
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            print(f"Failed to load extension {exception}")