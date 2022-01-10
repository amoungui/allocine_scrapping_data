#! /usr/bin/env python3
# coding: utf-8
import sys
import time
import requests
from bs4 import BeautifulSoup 
from Managers.MovieManager import MovieManager as Manager

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

def movie_launcher():
    """get the .... of the moive entity
    Args:
        None
    Returns:
        None
    """     
    for p in range(1, 4000):
        # Get request
        url = 'http://www.allocine.fr/films/?page={}'.format(str(p))
        response = requests.get(url)

        # Parse the content of the request with BeautifulSoup
        html_soup = BeautifulSoup(response.content.decode('utf-8', 'ignore'), 'html.parser')

        # Select all the movies url from a single page
        movies = html_soup.find_all('h2', 'meta-title')        

        for movie in movies:        
            res = requests.get('http://www.allocine.fr{}'.format(movie.a['href']))
            if res.ok:
                movie_html_soup = BeautifulSoup(res.content.decode('utf-8', 'ignore'), 'html.parser') # we get the soup content
                if movie_html_soup.find('div', 'titlebar-title'):
                    # Scrape the title
                    the_title = movie_html_soup.find('div', 'titlebar-title').text

                    # Set cursors
                    the_movie = movie_html_soup.section.div.div.div
                    the_movie_info_section = the_movie.select('.meta-body-item')
                    the_rating_info_section = the_movie.select('.rating-item')

                    manager = Manager([the_title, the_movie_info_section, the_rating_info_section]) # initialization of Manager  of movie
                    manager.test()
                    break
                    manager.parse_json() # convert the current objet to dictionnary
                    manager.to_csv() # register the current entity of movie into the csv file
        break

if __name__ == '__main__':
    print(movie_launcher())