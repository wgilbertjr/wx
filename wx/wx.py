import json
import os.path
import re
import requests
import sys
import wx_mods
from  icecream import ic



# https://api.weatherapi.com/v1/astronomy.json?key=03b8e7b5c6e74f02bfe115319242408&q=21742
# https://api.weatherapi.com/v1/current.json?key=03b8e7b5c6e74f02bfe115319242408&q=21742
#
# To Do:
# error checking for api calls
# logging for errors, etc

def main():
    ic.disable()
    wx_base_url = 'https://api.weatherapi.com/v1/'
    wx_astro_api = 'astronomy.json'
    wx_current_api = 'current.json'
    
    try:
        cfg_file = os.path.dirname(os.path.realpath(__file__)) + '/wx.config'
        cfg = wx_mods.read_config(cfg_file)
    except FileNotFoundError:
        ic('File not found.', cfg_file)
        sys.exit(1)
    finally:
        astro = astro_data(wx_base_url, wx_astro_api, cfg['wx_token'], cfg['zipcode'])
        print(astro)
        current = current_wx(wx_base_url, wx_current_api, cfg['wx_token'], cfg['zipcode'])
        print(current)

def get_wind(r_json):
    wind_speed_mph = r_json['current']['wind_mph']
    wind_speed_kph = r_json['current']['wind_kph']
    wind_direction = r_json['current']['wind_dir']
    wind_degree = r_json['current']['wind_degree']
    
    wind_data = [wind_speed_mph, wind_speed_kph, wind_direction, wind_degree]
    return wind_data
    
def current_wx(wx_base_url, wx_current_api, wx_token, location):
    url = wx_base_url + wx_current_api + '?key=' + wx_token
    parameters = {'q': str(location)}
    
    r_json = wx_mods.getWxJson(url, parameters)
    
    return {'current_conditions':r_json['current']['condition']['text'],
           'temp_f':r_json['current']['temp_f'],
           'temp_c':r_json['current']['temp_c'],
           'pressure_in':r_json['current']['pressure_in'],
           'pressure_mb':r_json['current']['pressure_mb']
           }
    
def astro_data(wx_base_url, wx_astro_api, wx_token, location):
    url = wx_base_url + wx_astro_api + '?key=' + wx_token
    parameters = {'q': str(location)}
    
    r_json = wx_mods.getWxJson(url, parameters)
    
    return {'location':r_json['location']['name'], 
              'region':r_json['location']['region'],
              'l_time':r_json['location']['localtime'],
              'sunrise':r_json['astronomy']['astro']['sunrise'],
              'sunset':r_json['astronomy']['astro']['sunset']
            }
    
def getWxJson(url, parameters):
    # error checking on session
    s = requests.Session()
    r = s.get(url, params=parameters)
    r_json = json.loads(r.text)
    return r_json

if __name__ == '__main__':
    main()
