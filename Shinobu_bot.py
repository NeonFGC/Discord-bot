import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from the .env file
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Define the intents (required by Discord API)
intents = discord.Intents.default()
intents.message_content = True  # To allow reading messages for commands

# Set up bot with command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: When the bot has connected to Discord
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Command: Simple ping-pong command
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
bot.run(TOKEN)
