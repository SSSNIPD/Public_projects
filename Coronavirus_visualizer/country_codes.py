from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """ Return the Pygal 2-digit country code for the given country"""

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif country_name == 'Iran':
            return 'ir'
        elif country_name == 'Palestine':
            return 'ps'
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Brunei':
            return 'bn'
        elif country_name == 'Costa-Rica':
            return 'cr'
        elif country_name == 'New-Zealand':
            return 'nz'
        elif country_name == 'Papua-New-Guinea':
            return 'pg'
        elif country_name == 'USA':
            return 'us'
        elif country_name == 'UK':
            return 'gb'
        elif country_name == 'UAE':
            return 'ps'
        elif country_name == 'Dominican-Republic':
            return 'do'
        elif country_name == 'Hong-Kong':
            return 'hk'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Puerto-Rico':
            return 'pr'
        elif country_name == 'Russia':
            return 'ru'
        elif country_name == 'Taiwan':
            return 'tw'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Syria':
            return 'sy'
        elif country_name == 'El-Salvador':
            return 'sv'
        elif country_name == 'Sri-Lanka':
            return 'lk'
        elif country_name == 'Bosnia-and-Herzegovina':
            return 'ba'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Saudi-Arabia':
            return 'sa'
        elif country_name == 'Sierra-Leone':
            return 'sl'
        elif country_name == 'South-Africa':
            return 'za'
        elif country_name == 'Vatican-City':
            return 'va'
        elif country_name == 'Venezuela':
            return 've'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Taiwan':
            return 'tw'

    # If the country wasn't found, return None.
    return None
