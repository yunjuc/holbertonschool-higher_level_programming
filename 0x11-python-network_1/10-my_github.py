#!/usr/bin/python3
'''Get user id using Github api'''
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    try:
        r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
        json = r.json()
        print(json['id'])
    except:
        print('None')
