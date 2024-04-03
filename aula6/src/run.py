import discord
from discord.ext import commands

client = commands.Bot(command_prefix="/input ", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("pingpong is ready!")
    print("----------------------")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


client.run('TOKEN')




