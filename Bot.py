import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

#Loads the .env file and access the value of the Discord Token stored in there
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename = 'discord.log',encoding='utf-8',mode='w')

#Enable Intents (permissions)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#Sets the prefix to activate the bot to a / and sets the intents to the ones we enabled above
bot = commands.Bot(command_prefix='/',intents = intents)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Not in vc")

@bot.command()
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left")
    else:
        await ctx.send("I am not in a vc")



bot.run(token,log_handler=handler,log_level=logging.DEBUG)

