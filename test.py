"""
this is just a test module to test my api
"""

from city_data import CityInfo

if __name__ == '__main__':
    city = CityInfo()

    location = 'Austin'
    city.get_info(location)