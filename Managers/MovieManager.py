from Managers.MovieEntityManager import MovieEntityManager as EntityManager
import numpy as np

class MovieManager(EntityManager):
    def __init__(self, tags:list):
        super().__init__()
        self.tags = tags
        self.the_title()


        
    def the_title(self):  

        """get the title of the moive entity
        Args:
            None
        Returns:
            title (str): the string that content title of movie
        """               

        try:
            self.setTitle(self.tags[1])
        except (TypeError, AttributeError, IndexError):
            self.setTitle(None)


    def test(self):          
        return self.getTitle()