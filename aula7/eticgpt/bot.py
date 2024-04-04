import discord
from discord.message import Message

intent=discord.Intents.default()

client = discord.Client()

@client.event
async def on_connect():
    pass

@client.event
async def on_ready():
    pass

@client.event
async def on_message(message: Message):
    pass