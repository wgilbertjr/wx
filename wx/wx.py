import json
import requests

# https://api.weatherapi.com/v1/astronomy.json?key=03b8e7b5c6e74f02bfe115319242408&q=21742

# move these to config file.
weather_token = '03b8e7b5c6e74f02bfe115319242408'
weather_base_url = 'https://api.weatherapi.com/v1/'
weather_astro_api = 'astronomy.json'
weather_location = '21742'

url = weather_base_url + weather_astro_api + '?key=' + weather_token
parameters = {'q': weather_location}

# error checking on session
s = requests.Session()
r = s.get(url, params=parameters)

r_status_code = r.status_code

r_json = json.loads(r.text)
#for (k) in r_json:
#    print(f'<>: [ {k} ] {r_json[k]}')

print(f'Location: {r_json['location']['name']}, {r_json['location']['region']}')
print(f'Local Time: {r_json['location']['localtime_epoch']}')
print(f'Sunrise: {r_json['astronomy']['astro']['sunrise']}')
print(f'Sunset: {r_json['astronomy']['astro']['sunset']}')



# figure out __name__ and __main__

