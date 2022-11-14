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
    
    'snow': snowfall in inches per year, int. States at or above 19 inches are 'snow' states. Round down for values in inches
    'rural_urban': classification of state as rural or urban, string.
    'income_tax': yes/no on state having income tax, string (yes/no)
    'rain': rainfall in inches per year, int. We consider approximately top 50% of rainfalls high rain, and bottom 50% low rain. Use >=42 inches for high rain. Round down for values in inches
    'coastline': yes/no on state having a coastline
    'avg_income': avg income in state, int. States above 70K are high, below 70K are low. Round as such: 78533 becomes 78500
    'political_climate': liberal/conservative per state, string (liberal/conservative)
    'university': indicates if state has an acclaimed university, string. If the state has an acclaimed (top 25) university, enter school name. Else, enter 'none'. In cases where a state has more than one top 25, list highest ranking
    'mountains': yes/no on if state has many mountains, string (yes/no)
    'desert': yes/no on if state is a desert environment, string (yes/no)
    'population: state population, int. Top 20 are high population, bottom 30 are low. Wisconsin is 20th place at 5.895 million, use this as cutoff. Round as such: 5895908 becomes 5895000
    'waterfront': yes/no on if state is either adjacent to a great lake or has one of the 10 longest rivers running through it, string (yes/no)

    'home_price': median home price for the state, int. States above 210K are high, states below 210K are low. Round as such: 321934 becomes 321000
    'crime_rate': crime rate ranking compared to other states, int. 1 means lowest crime, 50 means most crime, ie 5 means 5th safest state. 20 lowest crime rates are considered low crime.

    '''
    states = [
    
        {
            'name': 'alabama',
            'id': 0,
            'points': 0,
            'snow': 2,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 56,
            'coastline': 'yes',
            'avg_income': 51700,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 5039877
            'waterfront': 'yes',
            'home_price': 138000,
            'crime_rate': 37
        },
        {
            'name': 'alaska',
            'id': 1,
            'points': 0,
            'snow': 74,
            'rural_urban': 'rural',
            'income_tax': 'no',
            'rain': 29,
            'coastline': 'yes',
            'avg_income': 75400,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'yes',
            'desert': 'no',
            'population': 732673
            'waterfront': 'yes',
            'home_price': 300000,
            'crime_rate': 50
        },
        {
            'name': 'arizona',
            'id': 2,
            'points': 0,
            'snow': 0,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 12,
            'coastline': 'no',
            'avg_income': 57100,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'yes',
            'desert': 'yes',
            'population': 7276316
            'waterfront': 'yes',
            'home_price': 62000,
            'crime_rate': 46
        },
        {
            'name': 'arkansas',
            'id': 3,
            'points': 0,
            'snow': 5,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 50,
            'coastline': 'no',
            'avg_income': 49000,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 3025891
            'waterfront': 'yes',
            'home_price': 128000,
            'crime_rate': 47
        },
        {
            'name': 'california',
            'id': 4,
            'points': 0,
            'snow': 0,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 23,
            'coastline': 'yes',
            'avg_income': 80000,
            'political_climate': 'liberal',
            'university': 'stanford university',
            'mountains': 'no',
            'desert': 'yes',
            'population': 39237836
            'waterfront': 'yes',
            'home_price': 555000,
            'crime_rate': 35
        },
        {
            'name': 'colorado',
            'id': 5,
            'points': 0,
            'snow': 19,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 17,
            'coastline': 'no',
            'avg_income': 77100,
            'political_climate': 'liberal',
            'university': 'none',
            'mountains': 'yes',
            'desert': 'no',
            'population': 5812069
            'waterfront': 'yes',
            'home_price': 398000,
            'crime_rate': 31
        },
        {
            'name': 'connecticut',
            'id': 6,
            'points': 0,
            'snow': 40,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 50,
            'coastline': 'yes',
            'avg_income': 78800,
            'political_climate': 'liberal',
            'university': 'yale university',
            'mountains': 'no',
            'desert': 'no',
            'population': 3605597
            'waterfront': 'no',
            'home_price': 255000,
            'crime_rate': 4
        },
        {
            'name': 'delaware',
            'id': 7,
            'points': 0,
            'snow': 20,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 46,
            'coastline': 'yes',
            'avg_income': 70100,
            'political_climate': 'liberal',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 1003384
            'waterfront': 'no',
            'home_price': 254000,
            'crime_rate': 34
        },
        {
            'name': 'florida',
            'id': 8,
            'points': 0,
            'snow': 0,
            'rural_urban': 'urban',
            'income_tax': 'no',
            'rain': 55,
            'coastline': 'yes',
            'avg_income': 59200,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 21781128
            'waterfront': 'no',
            'home_price': 245000,
            'crime_rate': 26
        },
        {
            'name': 'georgia',
            'id': 9,
            'points': 0,
            'snow': 1,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 50,
            'coastline': 'yes',
            'avg_income': 62000,
            'political_climate': 'conservative',
            'university': 'emory university',
            'mountains': 'no',
            'desert': 'no',
            'population': 10799566
            'waterfront': 'no',
            'home_price': 201000,
            'crime_rate': 29
        },
        {
            'name': 'hawaii',
            'id': 10,
            'points': 0,
            'snow': 0,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 50,
            'coastline': 'yes',
            'avg_income': 83100,
            'political_climate': 'liberal',
            'university': 'none',
            'mountains': 'yes',
            'desert': 'no',
            'population': 1441553
            'waterfront': 'yes',
            'home_price': 636000,
            'crime_rate': 10
        },
        {
            'name': 'idaho',
            'id': 11,
            'points': 0,
            'snow': 19,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 17,
            'coastline': 'no',
            'avg_income': 61000,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'yes',
            'desert': 'no',
            'population': 1900923
            'waterfront': 'yes',
            'home_price': 286000,
            'crime_rate': 9
        },
        {
            'name': 'illinois',
            'id': 12,
            'points': 0,
            'snow': 24,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 39,
            'coastline': 'no',
            'avg_income': 69100,
            'political_climate': 'liberal',
            'university': 'university of chicago',
            'mountains': 'no',
            'desert': 'no',
            'population': 12671469
            'waterfront': 'yes',
            'home_price': 202000,
            'crime_rate': 33
        },
        {
            'name': 'indiana',
            'id': 13,
            'points': 0,
            'snow': 25,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 42,
            'coastline': 'no',
            'avg_income': 57600,
            'political_climate': 'conservative',
            'university': 'university of notre dame',
            'mountains': 'no',
            'desert': 'no',
            'population': 6805985	
            'waterfront': 'yes',
            'home_price': 155000,
            'crime_rate': 24
        },
        {
            'name': 'iowa',
            'id': 14,
            'points': 0,
            'snow': 35,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 34,
            'coastline': 'no',
            'avg_income': 61700,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 3193079
            'waterfront': 'yes',
            'home_price': 152000,
            'crime_rate': 17
        },
        {
            'name': 'kansas',
            'id': 15,
            'points': 0,
            'snow': 15,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 32,
            'coastline': 'no',
            'avg_income': 62100,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 2934582
            'waterfront': 'yes',
            'home_price': 150000,
            'crime_rate': 47
        },
        {
            'name': 'kentucky',
            'id': 16,
            'points': 0,
            'snow': 13,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 46,
            'coastline': 'no',
            'avg_income': 52300,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 4509394
            'waterfront': 'yes',
            'home_price': 146000,
            'crime_rate': 11
        },
        {
            'name': 'louisiana',
            'id': 17,
            'points': 0,
            'snow': 0,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 59,
            'coastline': 'yes',
            'avg_income': 51100,
            'political_climate': 'liberal',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 4624047
            'waterfront': 'yes',
            'home_price': 166000,
            'crime_rate': 45
        },
        {
            'name': 'maine',
            'id': 18,
            'points': 0,
            'snow': 62,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 46,
            'coastline': 'yes',
            'avg_income': 59000,
            'political_climate': 'liberal',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 1372247
            'waterfront': 'no',
            'home_price': 242000,
            'crime_rate': 1
        },
        {
            'name': 'maryland',
            'id': 19,
            'points': 0,
            'snow': 20,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 42,
            'coastline': 'yes',
            'avg_income': 86700,
            'political_climate': 'liberal',
            'university': 'johns hopkins university',
            'mountains': 'no',
            'desert': 'no',
            'population': 6165129
            'waterfront': 'no',
            'home_price': 308000,
            'crime_rate': 28
        },
        {
            'name': 'massachusetts',
            'id': 20,
            'points': 0,
            'snow': 43,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 48,
            'coastline': 'yes',
            'avg_income': 85800,
            'political_climate': 'liberal',
            'university': 'massachusetts institute of technology',
            'mountains': 'no',
            'desert': 'no',
            'population': 6984723
            'waterfront': 'no',
            'home_price': 422000,
            'crime_rate': 18
        },
        {
            'name': 'michigan',
            'id': 21,
            'points': 0,
            'snow': 51,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 33,
            'coastline': 'no',
            'avg_income': 59600,
            'political_climate': 'liberal',
            'university': 'university of michigan ann arbor',
            'mountains': 'no',
            'desert': 'no',
            'population': 10050811
            'waterfront': 'no',
            'home_price': 173000,
            'crime_rate': 41
        },
        {
            'name': 'minnesota',
            'id': 22,
            'points': 0,
            'snow': 54,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 27,
            'coastline': 'no',
            'avg_income': 74600,
            'political_climate': 'liberal',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 5707390
            'waterfront': 'yes',
            'home_price': 256000,
            'crime_rate': 13
        },
        {
            'name': 'mississippi',
            'id': 23,
            'points': 0,
            'snow': 1,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 56,
            'coastline': 'yes',
            'avg_income': 45800,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 2949965
            'waterfront': 'yes',
            'home_price': 126000,
            'crime_rate': 14
        },
        {
            'name': 'missouri',
            'id': 24,
            'points': 0,
            'snow': 17,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 43,
            'coastline': 'no',
            'avg_income': 57400,
            'political_climate': 'liberal',
            'university': 'washington university in st. louis',
            'mountains': 'no',
            'desert': 'no',
            'population': 6168187
            'waterfront': 'yes',
            'home_price': 162000,
            'crime_rate': 44
        },
        

        {
            'name': 'montana',
            'id': 25,
            'points': 0,
            'snow': 38,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 14,
            'coastline': 'no',
            'avg_income': 57100,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'yes',
            'desert': 'no',
            'population': 1104000
            'waterfront': 'yes',
            'home_price': 277000,
            'crime_rate': 40
        },
        {
            'name': 'nebraska',
            'id': 26,
            'points': 0,
            'snow': 25,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 26,
            'coastline': 'no',
            'avg_income': 63200,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 1963000,
            'waterfront': 'yes',
            'home_price': 175000,
            'crime_rate': 22
        },
        {
            'name': 'nevada',
            'id': 27,
            'points': 0,
            'snow': 21,
            'rural_urban': 'urban',
            'income_tax': 'no',
            'rain': 9,
            'coastline': 'no',
            'avg_income': 63200,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'yes',
            'desert': 'yes',
            'population': 3143000,
            'waterfront': 'yes',
            'home_price': 301000,
            'crime_rate': 39
        },
        {
            'name': 'new hampshire',
            'id': 28,
            'points': 0,
            'snow': 60,
            'rural_urban': 'rural',
            'income_tax': 'no',
            'rain': 44,
            'coastline': 'yes',
            'avg_income': 77900,
            'political_climate': 'conservative',
            'university': 'dartmouth college',
            'mountains': 'no',
            'desert': 'no',
            'population': 1388000,
            'waterfront': 'no',
            'home_price': 290000,
            'crime_rate': 2
        },
        {
            'name': 'new jersey',
            'id': 29,
            'points': 0,
            'snow': 16,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 48,
            'coastline': 'yes',
            'avg_income': 85700,
            'political_climate': 'conservative',
            'university': 'princeton university',
            'mountains': 'no',
            'desert': 'no',
            'population': 9267000,
            'waterfront': 'no',
            'home_price': 335000,
            'crime_rate': 5
        },
        {
            'name': 'new mexico',
            'id': 30,
            'points': 0,
            'snow': 9,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 14,
            'coastline': 'no',
            'avg_income': 51900,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'yes',
            'desert': 'yes',
            'population': 2115000,
            'waterfront': 'yes',
            'home_price': 203000,
            'crime_rate': 49
        },
        {
            'name': 'new york',
            'id': 31,
            'points': 0,
            'snow': 123,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 42,
            'coastline': 'yes',
            'avg_income': 72100,
            'political_climate': 'liberal',
            'university': 'cornell university',
            'mountains': 'no',
            'desert': 'no',
            'population': 19835000,
            'waterfront': 'no',
            'home_price': 321000,
            'crime_rate': 25
        },
        {
            'name': 'north carolina',
            'id': 32,
            'points': 0,
            'snow': 7,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 26,
            'coastline': 'yes',
            'avg_income': 57300,
            'political_climate': 'conservative',
            'university': 'duke university',
            'mountains': 'no',
            'desert': 'no',
            'population': 10551000,
            'waterfront': 'no',
            'home_price': 202000,
            'crime_rate': 30
        },
        {
            'name': 'north dakota',
            'id': 33,
            'points': 0,
            'snow': 51,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 18,
            'coastline': 'no',
            'avg_income': 64500,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 774000,
            'waterfront': 'yes',
            'home_price': 235000,
            'crime_rate': 21
        },
        {
            'name': 'ohio',
            'id': 34,
            'points': 0,
            'snow': 27,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 39,
            'coastline': 'no',
            'avg_income': 58600,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 11780000,
            'waterfront': 'yes',
            'home_price': 150000,
            'crime_rate': 19
        },
        {
            'name': 'oklahoma',
            'id': 35,
            'points': 0,
            'snow': 7,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 37,
            'coastline': 'no',
            'avg_income': 54400,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 3986000,
            'waterfront': 'yes',
            'home_price': 128000,
            'crime_rate': 38
        },
        {
            'name': 'oregon',
            'id': 36,
            'points': 0,
            'snow': 3,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 43,
            'coastline': 'yes',
            'avg_income': 67000,
            'political_climate': 'liberal',
            'university': 'none',
            'mountains': 'no',
            'desert': 'yes',
            'population': 4246000,
            'waterfront': 'yes',
            'home_price': 361000,
            'crime_rate': 15
        },
        {
            'name': 'pennsylvania',
            'id': 37,
            'points': 0,
            'snow': 28,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 42,
            'coastline': 'no',
            'avg_income': 63400,
            'political_climate': 'conservative',
            'university': 'university of pennsylvania',
            'mountains': 'no',
            'desert': 'no',
            'population': 12964000,
            'waterfront': 'yes',
            'home_price': 194000,
            'crime_rate': 27
        },
        {
            'name': 'rhode island',
            'id': 38,
            'points': 0,
            'snow': 33,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 49,
            'coastline': 'yes',
            'avg_income': 71100,
            'political_climate': 'liberal',
            'university': 'brown university',
            'mountains': 'no',
            'desert': 'no',
            'population': 1095000,
            'waterfront': 'no',
            'home_price': 300000,
            'crime_rate': 7
        },
        {
            'name': 'south carolina',
            'id': 39,
            'points': 0,
            'snow': 1,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 49,
            'coastline': 'yes',
            'avg_income': 56200,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 5190000,
            'waterfront': 'no',
            'home_price': 185000,
            'crime_rate': 43
        },
        {
            'name': 'south dakota',
            'id': 40,
            'points': 0,
            'snow': 43,
            'rural_urban': 'rural',
            'income_tax': 'no',
            'rain': 22,
            'coastline': 'no',
            'avg_income': 59500,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 895000,
            'waterfront': 'yes',
            'home_price': 205000,
            'crime_rate': 42
        },
        {
            'name': 'tennessee',
            'id': 41,
            'points': 0,
            'snow': 6,
            'rural_urban': 'rural',
            'income_tax': 'no',
            'rain': 51,
            'coastline': 'no',
            'avg_income': 56000,
            'political_climate': 'conservative',
            'university': 'vanderbilt university',
            'mountains': 'no',
            'desert': 'no',
            'population': 6975000,
            'waterfront': 'yes',
            'home_price': 185000,
            'crime_rate': 48
        },
        {
            'name': 'texas',
            'id': 42,
            'points': 0,
            'snow': 1,
            'rural_urban': 'urban',
            'income_tax': 'no',
            'rain': 35,
            'coastline': 'yes',
            'avg_income': 64000,
            'political_climate': 'conservative',
            'university': 'rice university',
            'mountains': 'no',
            'desert': 'yes',
            'population': 29527000,
            'waterfront': 'yes',
            'home_price': 207000,
            'crime_rate': 36
        },
        {
            'name': 'utah',
            'id': 43,
            'points': 0,
            'snow': 56,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 15,
            'coastline': 'no',
            'avg_income': 75700,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'yes',
            'desert': 'yes',
            'population': 3322000,
            'waterfront': 'yes',
            'home_price': 348000,
            'crime_rate': 12
        },
        {
            'name': 'vermont',
            'id': 44,
            'points': 0,
            'snow': 81,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 42,
            'coastline': 'no',
            'avg_income': 63000,
            'political_climate': 'liberal',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 645000,
            'waterfront': 'no',
            'home_price': 254000,
            'crime_rate': 3
        },
        {
            'name': 'virginia',
            'id': 45,
            'points': 0,
            'snow': 10,
            'rural_urban': 'urban',
            'income_tax': 'yes',
            'rain': 42,
            'coastline': 'yes',
            'avg_income': 76400,
            'political_climate': 'conservative',
            'university': 'university of virginia',
            'mountains': 'no',
            'desert': 'no',
            'population': 8642000,
            'waterfront': 'yes',
            'home_price': 285000,
            'crime_rate': 6
        },
        {
            'name': 'washington',
            'id': 46,
            'points': 0,
            'snow': 5,
            'rural_urban': 'urban',
            'income_tax': 'no',
            'rain': 38,
            'coastline': 'yes',
            'avg_income': 78600,
            'political_climate': 'liberal',
            'university': 'none',
            'mountains': 'no',
            'desert': 'yes',
            'population': 7738000,
            'waterfront': 'yes',
            'home_price': 409000,
            'crime_rate': 16
        },
        {
            'name': 'west virginia',
            'id': 47,
            'points': 0,
            'snow': 62,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 44,
            'coastline': 'no',
            'avg_income': 48800,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 1782000,
            'waterfront': 'yes',
            'home_price': 108000,
            'crime_rate': 23
        },
        {
            'name': 'wisconsin',
            'id': 48,
            'points': 0,
            'snow': 50,
            'rural_urban': 'rural',
            'income_tax': 'yes',
            'rain': 33,
            'coastline': 'no',
            'avg_income': 64100,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'no',
            'desert': 'no',
            'population': 5895000,
            'waterfront': 'yes',
            'home_price': 202000,
            'crime_rate': 20
        },
        {
            'name': 'wyoming',
            'id': 49,
            'points': 0,
            'snow': 91,
            'rural_urban': 'rural',
            'income_tax': 'no',
            'rain': 13,
            'coastline': 'no',
            'avg_income': 65000,
            'political_climate': 'conservative',
            'university': 'none',
            'mountains': 'yes',
            'desert': 'yes',
            'population': 578,
            'waterfront': 'yes',
            'home_price': 250000,
            'crime_rate': 8
        },

    ]
