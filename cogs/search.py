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
#firebase_admin.initialize_app(cred)
db = firestore.client()



class FindOthers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def findMentee(self, ctx, category, *, value):
        """Category(major, year), then value"""
        datas = []
        for x in db.collection("mentees").get():
            data = {'name':x.get("name"),
                    'discord':x.get("discord"),
                    'major':x.get('major'),
                    'year':x.get('year'),
                    'interests': x.get('interests'),
                'request':x.get('request')}
            datas.append(data)
        df = pd.DataFrame(datas)
        
        embeds = []

        #print(df.loc[df[category] == str(value)])

        for x in df.loc[df[category.lower()] == str(value)].sort_values("request").iterrows():
            emb = discord.Embed(title=x[1].get("name")+", " + x[1].get("discord"), description=x[1].get("request"), color=0x115599)
            emb.add_field(name="Major", value=x[1].get("major"), inline=True)
            emb.add_field(name="Year", value=x[1].get("year"), inline=True)
            for y in range(min(5, len(x[1].get("interests")))):
                emb.add_field(name="Interest:\u200b" ,value=x[1].get("interests")[y], inline=False)
            emb.timestamp = datetime.datetime.utcnow()
            emb.set_footer(text='\u200b',icon_url=ctx.author.avatar_url)
            embeds.append(emb)
        try:
            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()
        except Exception:
            await ctx.send("Couldn't find anyone that matched your search parameters!")
    
    
    
    @commands.command()
    async def findMentor(self, ctx, category, *, value):
        """Category(major, year), then value"""
        datas = []
        for x in db.collection("mentors").get():
            data = {'name':x.get("name"),
                    'discord':x.get("discord"),
                    'major':x.get('major'),
                    'year':x.get('year'),
                    'interests': x.get('interests'),
                'request':x.get('request')}
            datas.append(data)
        df = pd.DataFrame(datas)
        
        embeds = []

        #print(df.loc[df[category] == str(value)])

        for x in df.loc[df[category.lower()] == str(value)].sort_values("request").iterrows():
            emb = discord.Embed(title=x[1].get("name")+", " + x[1].get("discord"), description=x[1].get("request"), color=0x115599)
            emb.add_field(name="Major", value=x[1].get("major"), inline=True)
            emb.add_field(name="Year", value=x[1].get("year"), inline=True)
            for y in range(min(5, len(x[1].get("interests")))):
                emb.add_field(name="Interest:\u200b" ,value=x[1].get("interests")[y], inline=False)
            emb.timestamp = datetime.datetime.utcnow()
            emb.set_footer(text='\u200b',icon_url=ctx.author.avatar_url)
            embeds.append(emb)
        try:
            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()
        except Exception:
            await ctx.send("Couldn't find anyone that matched your search parameters!")


            

def setup(bot):
    bot.add_cog(FindOthers(bot))