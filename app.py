#! /usr/bin/env python3
# coding: utf-8
import sys
import time
import requests
from bs4 import BeautifulSoup 
from Managers.MovieManager import MovieManager as Manager

from warnings import warn
import traceback

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

    # init list to save errors
    errors = []    
    for p in range(1, 4000):
        # Get request
        url = 'http://www.allocine.fr/films/?page={}'.format(str(p))
        response = requests.get(url)

        # Parse the content of the request with BeautifulSoup
        html_soup = BeautifulSoup(response.content.decode("utf-8"), 'html.parser')

        # Select all the movies url from a single page
        movies = html_soup.find_all('h2', 'meta-title')        

        for movie in movies:   
            res = requests.get('http://www.allocine.fr{}'.format(movie.a['href']))
            if res.ok:
                movie_html_soup = BeautifulSoup(res.content.decode("utf-8"), 'html.parser') # we get the soup content
                if movie_html_soup.find('div', 'titlebar-title'):
                    # Scrape the title
                    the_title = movie_html_soup.find('div', 'titlebar-title').text 

                    # Set cursors                                   
                    the_movie_info_section = movie_html_soup.select('.meta-body')[0]
                    the_rating_info_section = movie_html_soup.select('.rating-item')
                    manager = Manager([the_title, the_movie_info_section, the_rating_info_section, movie_html_soup]) # initialization of Manager  of movie
                    print(manager.test())      
                break           
        break

if __name__ == '__main__':
    print(movie_launcher())