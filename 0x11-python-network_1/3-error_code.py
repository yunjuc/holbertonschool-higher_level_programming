#!/usr/bin/python3
'''Send a request to an URL and handle error code'''
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as r:
            print(r.read().decode())
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
