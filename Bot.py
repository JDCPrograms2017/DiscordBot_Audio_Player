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

#Sets the prefix to activate the bot to a ! and sets the intents to the ones we enabled above
bot = commands.Bot(command_prefix='!',intents = intents)

async def setup_hook():
    await bot.load_extension("cogs.music")
    print("Music cog loaded")

@bot.event
async def on_message(message):
    print(f"Message received: {message.content}")
    await bot.process_commands(message)

bot.setup_hook = setup_hook

bot.run(token,log_handler=handler,log_level=logging.DEBUG)