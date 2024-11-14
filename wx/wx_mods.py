import json
import requests
import sys

        
def get_wind_data(r_json):
    
    wind_speed_mph = r_json['current']['wind_mph']
    wind_speed_kph = r_json['current']['wind_kph']
    wind_direction = r_json['current']['wind_dir']
    wind_degree = r_json['current']['wind_degree']
    
    wind_data = [wind_speed_mph, wind_speed_kph, wind_direction, wind_degree]
    return wind_data
    
def current_wx(wx_base_url, wx_current_api, wx_token, location):
    url = wx_base_url + wx_current_api + '?key=' + wx_token
    parameters = {'q': location}
    
    r_json = getWxJson(url, parameters)
    # print(r_json)
    print(f'Current Conditions: {r_json['current']['condition']['text']}')
    print(f'Temperature: {r_json['current']['temp_f']} {u'\N{DEGREE SIGN}'}F ({r_json['current']['temp_c']} {u'\N{DEGREE SIGN}'}C)')
    print(f'Barometer: {r_json['current']['pressure_in']}in ({r_json['current']['pressure_mb']} mb)')
    
    
def astro_data(wx_base_url, wx_astro_api, wx_token, location):
    url = wx_base_url + wx_astro_api + '?key=' + wx_token
    parameters = {'q': location}
    
    r_json = getWxJson(url, parameters)
    
    print(f'Location: {r_json['location']['name']}, {r_json['location']['region']}')
    print(f'Local Time: {r_json['location']['localtime']}')
    print(f'Sunrise: {r_json['astronomy']['astro']['sunrise']}')
    print(f'Sunset: {r_json['astronomy']['astro']['sunset']}')
    
def getWxJson(url, parameters):
    # error checking on session
    s = requests.Session()
    r = s.get(url, params=parameters)
    r_json = json.loads(r.text)
    return r_json

