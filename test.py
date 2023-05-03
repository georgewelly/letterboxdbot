
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



results = soup.find(id="content")
films = []
#print(results.prettify())
for movie in results.find_all("li", class_="poster-container"):
    title = movie.find('img')['alt']
    films.append(title)
print(films)

# for movie in results.find_all("div", class_="cols-2 js-watchlist-content"):





