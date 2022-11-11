"""
this is just a test module to test my api
"""

from city_data import CityInfo
from state_data import StateData

if __name__ == '__main__':
    # city = CityInfo()

    # location = 'Austin'
    # city.get_info(location)
    obj = StateData()
    
    count = 0
    for i in obj.states:
        if i['snow'] == 'yes':
            obj.points['alabama'] + 1
        if i['rain'] == 'yes':
        print(i['snow'])
        count = count + 1