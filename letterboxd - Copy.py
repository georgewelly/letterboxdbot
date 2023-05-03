# bot.py

import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='cs', help='Responds with a random quote')
async def cs_quote(ctx):
    quotes = [
        
            'I am one lost Mirage T-side away from doing a fucking WarOwl class Discord live after one of these 10-mans',
            '"you just lost to Joe OMEGALUL" - Moris',
            '*DEAD* george : baiter cuck rat ♥♥♥♥',
            'fck off communication',
            "I can't see myself moving to another country because of the Smash Tournaments in the UK.",
            'Joe: I pre-watched the demo and knew that was gonna happen George:why didnt you pre-trade me you ♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥♥'
    ]

    response = random.choice(quotes)
    await ctx.send(response)

bot.run(TOKEN)


# load_dotenv()

# TOKEN = os.getenv("DISCORD_TOKEN")
# GUILD = os.getenv('DISCORD_GUILD')


# client = discord.Client(intents=discord.Intents.default())

# @client.event
# async def on_ready():
#     # print(f'{client.user} has dropped in tilted towers')
    
    
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})\n'
#     )
    
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     quotes = [
        
#             'I am one lost Mirage T-side away from doing a fucking WarOwl class Discord live after one of these 10-mans',
#             '"you just lost to Joe OMEGALUL" - Moris',
#             '*DEAD* george : baiter cuck rat ♥♥♥♥',
#             'fck off communication',
#             "I can't see myself moving to another country because of the Smash Tournaments in the UK.",
#             'Joe: I pre-watched the demo and knew that was gonna happen George:why didnt you pre-trade me you ♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥♥'
#         ,
#     ]

#     if message.content == 'cs quote':
#         response = random.choice(quotes)
#         await message.channel.send(response)

    
    
    
    
    ##print(client.guilds[0]) ## prints first server connected to 

# client.run(TOKEN)



