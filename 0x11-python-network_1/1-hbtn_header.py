#!/usr/bin/python3
'''Open an url and display X-Request-Id value'''
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.getheader('X-Request-Id'))
