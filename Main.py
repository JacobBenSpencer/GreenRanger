import discord
from discord.ext import commands
from dotenv import load_dotenv
import logging
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"IM ALIVE in, {bot.user.name}")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
