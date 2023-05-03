
import requests
from bs4 import BeautifulSoup

# User's Letterboxd username
username = "namastebrother"

# URL of the user's favourite movies page
url = f'https://letterboxd.com/{username}/watchlist'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'lxml')

results = soup.find(id="content")
films = []
#print(results.prettify())
for movie in results.find_all("li", class_="poster-container"):
    title = movie.find('img')['alt']
    films.append(title)
print(films)





# # Find the list of favourite movies
# favourites_list = soup.find('ul', {'class': 'poster-list'})

# # Extract the title and year of each movie
# favourites = []
# for movie in favourites_list.find_all('li'):
#     title = movie.find('img')['alt']
#     year = movie.find('span', {'class': 'year'}).text
#     favourites.append((title, year))

# # Print the list of favourite movies
# print(favourites)

# for movie in results.find_all("div", class_="cols-2 js-watchlist-content"):


# if request_type=="watchlist":
#     url = f'https://letterboxd.com/{username}/watchlist'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'lxml')
#     results = soup.find(id=content-nav)
#     for movie in results.find_all('ul'):
#         title = movie.find('img')['alt']
#         films.append(title)
#     reply = username + "'s films are: " + ",   ".join(films)
# else:
    

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





