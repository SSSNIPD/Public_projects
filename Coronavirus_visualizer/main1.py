import requests
import json
from pygal.maps.world import World
from pygal.style import RotateStyle

from country_codes import get_country_code
from function_timer import timer


def main():
    url = "https://covid-193.p.rapidapi.com/statistics"

    # Import countries list
    with open('coronavirus_countries.json') as f:
        countries = json.load(f)

    @timer
    def get_data(countries, url):
        """ Get data for each country"""
        data_dict = {}
        for country in countries:
            # API requests
            querystring = {"country": country}

            headers = {
                'x-rapidapi-host': "covid-193.p.rapidapi.com",
                'x-rapidapi-key': "cf0c1e4f88msh517766bd05c79e0p1b2912jsn8e0df2adc794"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            # Process API response
            r = response.json()
            data_cases = int(r['response'][0]['cases']['total'])
            code = get_country_code(country)
            if code:
                data_dict[code] = data_cases
            print(code)

        return data_dict

    # Group the countries into 4 cases labels
    corona_dict = get_data(countries, url)
    corona_dict_1, corona_dict_2, corona_dict_3, corona_dict_4 = {}, {}, {}, {}
    for c, cases in corona_dict.items():
        if cases < 1000:
            corona_dict_1[c] = cases
        elif cases < 10000:
            corona_dict_2[c] = cases
        elif cases < 100000:
            corona_dict_3[c] = cases
        else:
            corona_dict_4[c] = cases

    # Output how many countries are in each level
    print(len(corona_dict_1), len(corona_dict_2), len(corona_dict_3), len(corona_dict_4))

    # Create visualization
    wm_style = RotateStyle('#d62d20')
    wm = World(style=wm_style, width=1200, height=600, )
    wm.title = 'Total Covid-19 cases, by country(4/15/20 : 4:15 pm)\n(Updated every 15 minutes)'
    wm.add('100,000+ ', corona_dict_4)
    wm.add('1000-10,000 ', corona_dict_3)
    wm.add('1000-100,1000 ', corona_dict_2)
    wm.add('0-1000 ', corona_dict_1)

    wm.render_to_file('world_covid19_cases.svg')


if __name__ == '__main__':
    main()
