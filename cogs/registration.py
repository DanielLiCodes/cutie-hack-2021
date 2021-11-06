import discord
import asyncio
from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError

import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import ast

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
mentors = db.collection("mentors")
mentees = db.collection("mentees")



class Member_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def fireBase():
        pass

    @commands.command()
    async def register(self, ctx):
        """register"""
        def addToDb(isMentor, name, major, year, interests):
            data = {
                "name" : name,
                "major" : major,
                "year" : year,
                "interests" : interests
            }
            if isMentor:
                mentors.add(data)
            else:
                mentees.add(data)
            


            pass
        await ctx.send("Please enter your name!") 

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            response = await self.bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("timed out!")
            return

        await ctx.send(response.content)
    

            




# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(Member_Commands(bot))