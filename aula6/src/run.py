import discord
from discord.ext import commands
# from discord.commands import slash_command
import os

client = commands.Bot(command_prefix='/input ', intents=discord.Intents.all())
# intents = discord.Intents.default()
# intents.message_content = True
# bot = commands.Bot(command_prefix='/input ', intents=intents)

@client.event
async def on_ready():
    print('pingpong app is ready!')

# @slash_command(guild_ids=[NVM_THIS], description="Responds with pong")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!')

TOKEN = os.getenv('not/gonna/dox/my/env/token.txt')

client.run('TOKEN')




