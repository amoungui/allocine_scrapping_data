from Models.Entity import Entity as entity 
from Managers.SourceManager import SourceManager as base

class MovieEntityManager(base, entity):
    dataset = []
    
    def __init__(self):
        base.__init__(self)
        entity.__init__(self)
    
    def parse_json(self):
        """Construct a dictionary from the object pass as a parameter 
                        and add it to the attribute of the class which is a list. 
                        it thus returns a dictionary list
        Args:
            None 
        Returns:
            data (list): a List of dictionnary
        """                                
  
        data = {
            'title': self.getTitle(),
            'date_reprise': self.getre_release_date(),
            'date_sortie': self.getrelease_date(),
            'duration': self.getduration(),
            'director':self.getdirectors(),
            'actors': self.getactors(),
            'genre': self.getgenre(),
            'nationality':self.getnationality(),
            'press_rating': self.getpress_rating(),
            'nb_press': self.getnber_press_vote(),
            'spec_rating': self.getuser_rating(),
            'nb_spec': self.getnber_user_vote(),
        }   
        
        return self.dataset.append(data) #json.dumps(self.dataset, indent=2)  json.dumps(data, indent=2) 
        