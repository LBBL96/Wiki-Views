import requests
import json
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

class WikiViews():
    '''
    This class gives you an object allowing you to look up a person on Wikipedia
    and get the page views of that person over the last day, week, month, and 60 days.
    '''
    
    def __init__(self, person='Lisa Simpson'):
        person = person.lower().replace('.', '').split()
        person = '_'.join(word.capitalize() for word in person)
        self.name = person
        self.total_views = {}
        self.key = ''
        self.values = []
        self.labels = []
        
        """
        Part of instantiating an object will be loading a dictionary with the JSON result
        of the Wikipedia page so that only one API pull will be needed for all methods
        """
        
        uri = f'https://en.wikipedia.org/w/api.php?action=query&titles={self.name}&prop=pageviews&format=json'
        response = requests.get(uri).json()
        response_json = response
        pages = response_json['query']['pages']
        self.total_views.update(pages)
        
        """
        In order to dig down into the JSON file for total views, we need a key that is specific to the person
        being searched. The initializing function put the JSON from 'pages' down into a dictionary. To get
        to the next level, the page ID has to be parsed. 
        """
        self.key = self.total_views
        new_key = str(self.key.keys()).split("'")
        new_key = new_key[1]
        self.key = new_key

    def get_views(self):
        """
        Returns a dictionary with date keys and page view values for the sixty days 
        prior to instantiating the object.
        """
        pages = self.total_views
        pageviews = pages[self.key]['pageviews']
        return pageviews
    
    def sixty_day_count(self):
        """
        Returns int of total page views in the sixty days prior to instantiating the object.
        """
        values = WikiViews.values(self)
        sixty_days = sum(np.array(list(values)))
        return sixty_days
    
    def thirty_day_count(self):
        """
        Returns int of total page views in the thirty days prior to instantiating the object.
        """
        values = WikiViews.values(self)
        thirty_days = sum(np.array(values[-30:]))
        return thirty_days
        
    def seven_day_count(self):
        """
        Returns int of total page views in the seven days prior to instantiating the object.
        """
        values = WikiViews.values(self)
        seven_days = sum(np.array(values[-7:]))
        return seven_days
    
    def yesterday(self):
        """
        Returns int of total page views on the day prior to instantiating the object.
        """
        values = WikiViews.values(self)
        yesterday = int(values[-1])
        return yesterday
    
    def values(self):
        """
        Returns a list of views per day over the 60 days prior to instantiating the object.
        """
        views = WikiViews.get_views(self).values()
        values = np.array(list(views)[:-1])
        return values
    
    def mean(self):
        """
        Returns float of mean views over previous 60 days.
        """
        mean = WikiViews.values(self).mean()
        return mean
    
    def max_views(self):
        """
        Returns a tuple of the date of the max views and the number of views
        """
        # This needs to be made a list because get_views returns a dict
        keys = list(WikiViews.get_views(self).keys())
        
        values = WikiViews.values(self) # values function returns a list
        max_value = values.max()
        
        # Find index of max value in values list, then pull date from keys by that index
        date_loc = values.tolist().index(max_value)
        date = keys[date_loc]
        
        return (date, max_value)
        
    
    def labels(self):
        """
        Returns a list of date strings.
        """
        date_keys = list(WikiViews.get_views(self).keys())

        lookup = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'June',
        '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

        for item in date_keys:
            item = item.split('-')
            new_list.append([item[1],item[2],item[0]])

        dates = []
        month_day = []
        
        for item in new_list:
            dates.append(f'{lookup[item[0]]} {item[1]}, {item[2]}')
            month_day.append(f'{lookup[item[0]]} {item[1]}')
            
        return dates
        
    def plot_two_months(self):
        """
        Returns a time-series plot of total views.
        """
        day, hits = WikiViews.max_views(self)
        values = WikiViews.values(self)
        plt.figure(figsize=(10,5))
        plt.plot(values, 'g-')
        name = self.name.split('_')
        plt.suptitle(f'Wikipedia views of {name[0]} {name[1]} over previous 60 days', fontsize=14)
        plt.title(f'Highest view count was {hits} on {day}', fontsize=12)
        plt.show()