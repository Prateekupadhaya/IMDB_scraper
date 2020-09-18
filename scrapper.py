from bs4 import BeautifulSoup
import requests

URL='https://vw.ffmovies.sc/movies/'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#title = soup.find(title="Movies").get_text()
def get_movies():
    for a_tag in soup.find_all('a', class_='name', href=True):
        print ('href: ', a_tag['href'])

    #for i in range (25):
    #    a = soup.find(class = "name").get_text()
    #    print(a)
    #print(title)


get_movies()
