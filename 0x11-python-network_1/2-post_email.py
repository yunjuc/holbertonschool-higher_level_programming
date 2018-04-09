#!/usr/bin/python3
'''Send a POST request to an url'''
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    post = urllib.request.Request(url, data)
    with urllib.request.urlopen(post) as r:
        print(r.read().decode())
