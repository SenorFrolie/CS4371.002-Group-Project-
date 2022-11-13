"""
this is the file that has all our city data in it
"""

class StateData:
    '''
    this is the class that will contain all our data form our states
    '''
    '''
    Template:
    Each category with an explanation on it's use/how it's used
    'name': state name, string
    'id': state id#, int. 0 is first alphabetically, 1 is 2nd, etc.
    'points': point total for a state; all totals start at 0
    Lines from here on relate to questions
    'snow': snowfall in inches per year, int. States above 19 inches are 'snow' states
    'rural_urban': classification of state as rural or urban, string.
    'income_tax': yes/no on state having income tax, string (yes/no)
    'rain': rainfall in inches per year, int. We consider approximately top 50% of rainfalls high rain, and bottom 50% low rain. Use >=42 inches for high rain.
    'coastline': yes/no on state having a coastline
    'avg_income': avg income in state, int. States above 70K are high, below 70K are low
    'political_climate': liberal/conservative per state, string (liberal/conservative)
    'university': indicates if state has an acclaimed university, string. If the state has an acclaimed (top 20) university, enter school name. Else, enter 'none'
    'mountains': yes/no on if state has many mountains, string (yes/no)
    'desert': yes/no on if state is a desert environment, string (yes/no)
    'population: state population, int. Top 20 are high population, bottom 30 are low. Wisconsin is 20th place at 5.895 million, use this as cutoff
    'waterfront': yes/no on if state is either adjacent to a great lake or has one of the 10 longest rivers running through it, string (yes/no)

    'home_price': median home price for the state, int. States above 210K are high, states below 210K are low
    'crime_rate': crime rate ranking compared to other states, int. 1 means lowest crime, 50 means most crime. Bottom 20 are considered low crime.

    '''
    states = [
        {
            'name': 'alabama',
            'id': 0,
            'points': 0,
            'snow': 'no',
            'rain': 'no',
            'ocean': 'no'
        },
        {
            'name': 'arkansas',
            'id': 1,
            'points': 0,
            'snow': 'yes',
            'rain': 'no',
            'ocean': 'no'
        }
        #Amir's states to be entered here

        {
            'name': 'montana',
            'id': 25,
            'points': 0,
            'snow': 
        }
    ]
