import json
import re
import requests
import os.path

def validate_zipcode(zipcode):
    # To Do: build out validation from USPS.
    if re.match(r'^[0-9]{5}$', zipcode):
        return zipcode
    else:
        raise

def getWxJson(url, parameters):
    # error checking on session
    s = requests.Session()
    r = s.get(url, params=parameters)
    r_json = json.loads(r.text)
    return r_json

def read_config(path):
    try:
        file = open(path,'r')
    except FileNotFoundError:
        print(f'error opening file: {path}')
        sys.exit(1)
    else:
        d = {}
        with file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split(':')
                d[key] = value
        return d
