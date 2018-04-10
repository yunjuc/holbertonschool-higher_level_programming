#!/usr/bin/python3
'''Send search request to StarWar api'''
import requests
import sys


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/?search=' + sys.argv[1]
    r = requests.get(url)
    json = r.json()
    print('Number of results: {}'.format(json['count']))
    for item in json['results']:
        print(item['name'])
