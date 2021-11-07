import discord
import asyncio
from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import ast

cred = credentials.Certificate("./key.json")
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
        """Sign up to be a mentor/mentee!"""
        def addToDb(isMentor, name, major, year, interests, request):
            data = {
                "name" : name,
                "discord" : ctx.author.name+"#"+str(ctx.author.discriminator),
                "major" : major,
                "year" : year,
                "interests" : interests,
                "request": request
            }
            if isMentor:
                mentors.add(data)
            else:
                mentees.add(data)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        
        multiple_choice = BotMultipleChoice(ctx, ['Mentor', 'Mentee'], "Would you like to be a mentor or a mentee?")
        mentorChoice = await multiple_choice.run()
        isMentor = mentorChoice[0].lower() == "mentor"
        await multiple_choice.quit(multiple_choice.choice)
        try:
            await mentorChoice[1].delete()  #delete message with string of seledction
        except Exception:
            pass

        print(isMentor)
        
        await ctx.send("Please enter your name!") 
        try:
            response = await self.bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("Timed out!")
            return
        name = response.content

        multiple_choice = BotMultipleChoice(ctx, ["Bioengineering", "Computer Science", "Chemical Engineering", "Computer Engineering", "Data Science", "Electrical Engineering", "Environmental Engineering", "Material Science", "Mechanical Engineering"], "What major are you?")
        majorChoice = await multiple_choice.run()
        major = majorChoice[0]
        await multiple_choice.quit(multiple_choice.choice)
        try:
            await majorChoice[1].delete()  #delete message with string of seledction
        except Exception:
            pass
        

        multiple_choice = BotMultipleChoice(ctx, ["1", "2", "3", "4"], "What year are you?")
        yearChoice = await multiple_choice.run()
        year = yearChoice[0]
        await multiple_choice.quit(multiple_choice.choice)
        try:
            await yearChoice[1].delete()  #delete message with string of seledction
        except Exception:
            pass

        await ctx.send("Please enter your interests(seperated by space, no comment): ")
        try:
            response = await self.bot.wait_for("message", check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("timed out!")
            return
        
        interests = response.content.split(" ")
        if isMentor:
            await ctx.send("What is your goal as a mentor? What do you bring to the table")
        else:
            await ctx.send("What topic/things do you want mentoring on? (i.e. getting an internship, python coding, etc...)")
        try:
            response = await self.bot.wait_for("message", check=check, timeout=90)
        except asyncio.TimeoutError:
            await ctx.send("timed out!")
            return
        
        request = response.content

        addToDb(isMentor, name, major, year, interests, request)

        await ctx.send("Added to database!")

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(Member_Commands(bot))