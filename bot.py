import os, discord, random, requests

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#API_KEY = os.getenv('LETTERBOXD_API_KEY')

# 2
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')



@bot.command(name='lb', help='letterboxd')
async def letterboxd(ctx, user:str, request_type:str):
    
    # User's Letterboxd username
    username = user

    # URL of the user's favourite movies page
    url = f'https://letterboxd.com/{username}'

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')

    results = soup.find(id=request_type)
    films = []
    for movie in results.find_all('li'):
        title = movie.find('img')['alt']
        films.append(title)
    

    reply = username + "'s films are: " + ",   ".join(films)
    
    # Print the list of favourite movies
    await ctx.send(reply)

# @bot.command(name='roll_dice', help='Simulates rolling dice.')
# async def roll(ctx, number_of_dice: int, number_of_sides: int):
#     dice = [
#         str(random.choice(range(1, number_of_sides + 1)))
#         for _ in range(number_of_dice)
#     ]
#     await ctx.send(', '.join(dice))

# @bot.command(name='cs', help='Responds with a random quote')
# async def cs_quote(ctx):
#     quotes = [
        
#             'asdf',
#             'asdf',
#             ''
#     ]
#     response = random.choice(quotes)
#     await ctx.send(response)

bot.run(TOKEN)




