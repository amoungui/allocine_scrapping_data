#! /usr/bin/env python3
# coding: utf-8
import numpy as np

class Entity:
    def __init__(self):
        self.title = np.nan
        self.release_date = np.nan
        self.re_release_date = np.nan
        self.duration = np.nan
        self.genre = []
        self.directors = []
        self.actors = []
        self.nationality = np.nan
        self.press_rating = np.nan 
        self.nber_press_vote = np.nan 
        self.user_rating = np.nan 
        self.nber_user_vote = np.nan 

    def gettitle(self):
        """get the title of the moive entity
        Args:
            None
        Returns:
            title (str): the tag that content title
        """        
        
        return self.title 

    def getrelease_date(self):
        """get the release date of the moive entity
        Args:
            None
        Returns:
            release_date (str): the tag that content release date of movie
        """         
        return self.release_date

    def getre_release_date(self):
        """get the re-release date of the moive entity
        Args:
            None
        Returns:
            re-release_date (str): the tag that content re-release date of movie
        """         
        return self.re_release_date

    def getduration(self):
        """get the duration of the moive entity
        Args:
            None
        Returns:
            duration (str): the tag that content duration of movie
        """         
        return self.duration

    def getgenre(self):
        """get the genre of the moive entity
        Args:
            None
        Returns:
            genre (str): the tag that content genre of movie
        """         
        return self.genre
    
    def getdirectors(self):
        """get the directors of the moive entity
        Args:
            None
        Returns:
            directors (list): the tag that content the directors of movie
        """        
        return self.directors
    
    def getactors(self):
        """get the actors of the moive entity
        Args:
            None
        Returns:
            director (list): the tag that content the the director of movie
        """            
        return self.actors   
 
    def getnationality(self):
        """get the country name of the moive entity
        Args:
            None
        Returns:
            country (str): the tag that content the  country name of movie
        """                         
        return self.nationality   
    
    def getpress_rating(self):
        """get the press rating of the moive entity
        Args:
            None
        Returns:
            press_rating (int): the tag that content the press rating of movie
        """                                 
        return self.press_rating
    
    def getnber_press_vote(self):
        """get the number of press vote of the moive entity
        Args:
            None
        Returns:
            nber_press_vote (int): the tag that content the number of press vote of movie
        """                                 
        return self.nber_press_vote
    
    def getuser_rating(self):
        """get the user rating of the moive entity
        Args:
            None
        Returns:
            user_rating (int): the tag that content the user_rating of movie
        """                                 
        return self.user_rating
        
    def getnber_user_vote(self):
        """get the number user vote of the moive entity
        Args:
            None
        Returns:
            nber_user_vote (int): the tag that content the number user vote of movie
        """                              
        return self.nber_user_vote
                
    ################################################################
    ##                          setter                            ##
    ################################################################

    def settitle(self, tag):
        """get the title of the moive entity
        Args:
            tag (str): the tag that content the title of movie
        Returns:
            None
        """                 
        if tag is not None:
            self.title = tag
        else: 
            self.title = np.nan 

    def setrelease_date(self, tag):
        """get the release date of the moive entity
        Args:
            tag (str): the tag that content the release date of movie
        Returns:
            None
        """                        
        if tag is not None:
            self.release_date = tag
        else:
            self.release_date = 'NaN'

    def setre_release_date(self, tag):
        """get the re_release date of the moive entity
        Args:
            tag (str): the tag that content the re_release date of movie
        Returns:
            None
        """                        
        if tag is not None:
            self.re_release_date = tag
        else:
            self.re_release_date = np.nan                       

    def setduration(self, tag):
        """get the duration of the moive entity
        Args:
            tag (str): the tag that content the duration of movie
        Returns:
            None
        """                        
        if tag is not None:
            self.duration = tag
        else:
            self.duration = np.nan                 


    def setgenre(self, tag):
        """set the genre of the moive entity
        Args:
            tag (list): the tag that content the liste of genre of movie
        Returns:
            None
        """                            
        if tag is not None:
            self.genre = tag
        else:
            self.genre = np.nan    
    
    def setdirectors(self, tag):
        """set the tag directors entity
        Args:
            tag (list): the tag that content the directors of movie
        Returns:
            None
        """                            
        if tag is not None:
            self.directors = tag
        else:
            self.directors = np.nan 
    
    def setactors(self, tag):
        """set the tag actors of the moive entity
        Args:
            tag (list): the tag that content the actor list of movie
        Returns:
            None
        """              
        if tag is not None:
            self.actors = tag
        else:
            self.actors = np.nan 
    
    def setnationality(self, tag):
        """set the tag nationality of the moive entity
        Args:
            tag (str): the tag that content the nationality of movie
        Returns:
            None
        """
        if tag is not None:
            self.nationality = tag
        else:
            self.nationality = np.nan 
    
    def setpress_rating(self, tag):
        """set the tag press rating of the moive entity
        Args:
            tag (str): the tag that content the press rating of movie
        Returns:
            None
        """                        
        if tag is not None:
            self.press_rating = tag
        else:
            self.press_rating = np.nan 
    
    def setnber_press_vote(self, tag):
        """set the tag number of press vote of the moive entity
        Args:
            tag (str): the tag that content the number of press vote of movie
        Returns:
            None
        """                                
        if tag is not None:
            self.nber_press_vote = tag
        else:
            self.nber_press_vote = np.nan 
            
    def setuser_rating(self, tag):
        """set the tag user rating of the moive entity
        Args:
            tag (str): the tag that content the user rating of movie
        Returns:
            None
        """                     
        if tag is not None:
            self.user_rating = tag
        else:
            self.user_rating = np.nan 
    
    def setnber_user_vote(self, tag):
        """set the tag number of user vote of the moive entity
        Args:
            tag (str): the tag that content the number of user vote of movie
        Returns:
            None
        """             
        if tag is not None:
            self.nber_user_vote = tag
        else:
            self.nber_user_vote = np.nan 
        


