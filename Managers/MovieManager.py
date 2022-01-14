from Managers.MovieEntityManager import MovieEntityManager as EntityManager
#import dateparser
import numpy as np

class MovieManager(EntityManager):
    def __init__(self, tags:list):
        EntityManager.__init__(self)
        self.tags = tags
        self.the_title()
        self.the_release_date()
        self.the_duration()
        self.the_directors()
        self.the_actors()
        self.the_genre()
        self.the_press_rating()
        self.the_nber_press_vote()
        self.the_user_rating()
        self.the_nber_user_vote()
        self.the_nationality()
        self.the_re_release_date()

###########  define the setters method   ###################
    def the_title(self):
        self.settitle(self.tags[0])

    def the_release_date(self):
        if self.tags[1].find('span', 'date'):
            self.setrelease_date(self.tags[1].find('span', 'date').text.strip())

    def the_duration(self):
        a_string = ''
        l = self.tags[1].find('div', attrs={'class':'meta-body-item meta-body-info'}).text.strip().split()
        arr = np.array(l)
        if np.where(arr=='/'):
            index = np.where(arr=='/')
            for i in range(int(index[0][0])+1, int(index[0][1])):
                a_string = a_string + "" + l[i]
        self.setduration(a_string.strip())

    def the_directors(self):
        cors = self.tags[1].find_all('div', attrs={'class', 'meta-body-item meta-body-direction'})
        arr = []
        for i in cors:    
            if i.find('span', 'light').text.strip() == 'Par':
                arr = [e.text.strip() for e in i.find_all('span')][1:]
            else:
                arr = [e.text.strip() for e in i.find_all('span')][1:] 
        self.setdirectors(arr)

    def the_actors(self):
        cors = self.tags[1].find('div', attrs={'class': 'meta-body-item meta-body-actor'}).find_all('span')
        self.setactors([e.text.strip() for e in cors][1:])

    def the_genre(self):
        l = self.tags[1].find('div', attrs={'class':'meta-body-item meta-body-info'}).text.split()
        arr = np.array(l)
        index = np.where(arr=='/')
        self.setgenre([l[i] for i in range(int(index[0][1])+1, len(l))])

    def the_press_rating(self):
        self.setpress_rating(self.tags[2][0].find('span', attrs={'class': 'stareval-note'}).text.strip())

    def the_nber_press_vote(self):
        self.setnber_press_vote(self.tags[2][0].find('span', attrs={'class': 'stareval-review light'}).text.strip().split()[0])        

    def the_user_rating(self):
        self.setuser_rating(self.tags[2][1].find('span', attrs={'class': 'stareval-note'}).text.strip())

    def the_nber_user_vote(self):
        self.setnber_user_vote(self.tags[2][1].find('span', attrs={'class', 'stareval-review light'}).text.strip().split()[0])

    def the_nationality(self):
        i = self.tags[-1].find('section', attrs={'class':'section ovw ovw-technical'}).select('.item')[0] 
        if (i.span.text == 'Nationalité') | (i.span.text == 'Nationalités'):
            self.setnationality(i.text.strip().split()[1:])
        else:
            default = 'americain'
            self.setnationality(default)

    def the_re_release_date(self):
        for i in self.tags[-1].find('section', attrs={'class':'section ovw ovw-technical'}).select('.item'):
            if i.find('span', attrs={'class': 'what light'}).text.strip() == 'Année de production':
                self.setre_release_date(i.find('span', attrs={'class': 'that'}).text.strip())      

    def test(self):

        return [
            self.gettitle(), 
            self.getre_release_date(), 
            self.getrelease_date(), 
            self.getduration(), 
            self.getgenre(),
            self.getdirectors(),
            self.getactors(),
            self.getnationality(),
            self.getpress_rating(),
            self.getnber_press_vote(),
            self.getuser_rating(),
            self.getnber_user_vote()
        ]




