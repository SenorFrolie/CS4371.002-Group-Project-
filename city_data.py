'''
this is the file that will get all our info from our city api
'''
import os
import requests
from dotenv import load_dotenv
load_dotenv()

class CityInfo:
    '''
    this is the class where we will get all of our city data
    '''

    @staticmethod
    def get_info(location):
        '''
        this function doesnt have a realy purpose right now
        '''

        geo_api_key = os.getenv('geo_api_key')

        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q60"

        querystring = {"location":location}

        headers = {
            "X-RapidAPI-Key": geo_api_key,
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)
        return 'info'