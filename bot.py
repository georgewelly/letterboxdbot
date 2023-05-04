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
    url = f'https://letterboxd.com/{user}'

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')

    results = soup.find(id=request_type)
    films = []
    for movie in results.find_all('li'):
        title = movie.find('img')['alt']
        films.append(title)
    reply = user + "'s films are: " + ",  ".join(films)
    
    # Print the list of favourite movies
    await ctx.send(reply)

@bot.command(name='watchlist', help='letterboxd watchlist')
async def watchlist(ctx, user:str):
    url = f'https://letterboxd.com/{user}/watchlist'

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')

    results = soup.find(id="content")
    films = []
    for movie in results.find_all("li", class_="poster-container"):
        title = movie.find('img')['alt']
        films.append(title)
    reply = "The movies on " + user + "'s watchlist are: "+ ",  ".join(films)
    await ctx.send(reply)
       
 
bot.run(TOKEN)




