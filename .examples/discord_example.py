# This example uses discord.py

import discord
from discord.ext import commands
import asyncio

# iDoggo modules
from iDoggo import dog1
from iDoggo import dog2
import iDoggo

bot = commands.Bot(command_prefix="!")

@bot.commands(pass_context=True)
async def dog1(ctx):
     doggo = iDoggo.dog1()
     await bot.say(doggo)
 
 token = "xxxxxxxxxxxxxxxxxxxxxxxx"
 bot.run(token)
