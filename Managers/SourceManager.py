import os
import csv

from abc import ABC, abstractmethod

class SourceManager(ABC):
    
    @property
    @classmethod
    @abstractmethod
    def dataset(cls):
        return NotImplementedError
    
    @abstractmethod
    def parse_json(self):
        pass

    def to_csv(self):
        """write data into the csv file
        Args:
            None
        Returns:
            None
        """        
        directory = os.path.dirname(os.path.dirname(__file__)) # we get the right path.
        path_to_file = os.path.join(directory, "data", 'allocine_movies.csv') # with this path, we go inside the folder `data` and get the file.
        
        with open(path_to_file, 'w', encoding='utf-8') as csv_file: # we open the file as csv_file in w mode.
            writer = csv.DictWriter(csv_file, fieldnames=type(self).dataset[0].keys()) # instatiation of Writer objet that get the file and the fieldnames
            writer.writeheader() # we writer the header of the file
            
            for row in type(self).dataset:
                writer.writerow(row) # iteration into the dataset to write each row into the csv_file
        
        print('the dataset line has been written successfully!')