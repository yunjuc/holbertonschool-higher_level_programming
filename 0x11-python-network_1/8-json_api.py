#!/usr/bin/python3
'''Send search request to an api'''
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if sys.argv[1] is None:
        q=""
    else:
        q = sys.argv[1]
    value = {'q': q}
    try:
        r = requests.post(url, data=value)
        json = r.json()
        print('[{}] {}'.format(json['id'], json['name']))
    except KeyError:
        print('No result')
    except ValueError:
        print('Not a valid JSON')
