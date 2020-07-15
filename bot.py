import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
#import requests
import os

description = '''Discord of Powers, the game of backstabbing allies'''
bot = commands.Bot(command_prefix='!', description=description)

client = discord.Client()


#@client.event
#async def on_ready():
   #await message.channel.send('Stirlitz, keep calm')


@client.event
async def on_message(message):
    if str(message.author) == "Stirlitz#0045":
        await message.channel.send('I remember you, your name is '+str(message.author))


bot.run(str(os.environ.get('BOT_TOKEN')))

