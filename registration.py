import discord
from discord.ext import commands

class Registration_Commands(commands.Cog, name="registration"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'checkEyesAmmount', aliases=['checkEyes', 'checkEyesAmnt'])
    @commands.guild_only()
    async def checkEyesAmmount(self, ctx):
        await ctx.send("in")

def setup(bot):
    bot.add_cog(Registration_Commands(bot))