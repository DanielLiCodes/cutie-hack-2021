import discord
import datetime
import asyncio
from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import ast

cred = credentials.Certificate("./key.json")
db = firestore.client()



class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def drop(self, ctx):
        """Leave our database ):"""

        confirmation = BotConfirmation(ctx, 0x333333)
        await confirmation.confirm("Are you sure you want to drop out of our database?")

        if confirmation.confirmed:
            await confirmation.update("Goodbye ):", color=0x55ff55)
        else:
            await confirmation.update("Thanks for staying!", hide_author=True, color=0xff5555)
            return
        for x in db.collection("mentors").get():
            if x.get("discord") == ctx.author.name+"#"+str(ctx.author.discriminator):
                x.reference.delete()

        for x in db.collection("mentees").get():
            if x.get("discord") == ctx.author.name+"#"+str(ctx.author.discriminator):
                x.reference.delete()

        



            

def setup(bot):
    bot.add_cog(Utility(bot))
