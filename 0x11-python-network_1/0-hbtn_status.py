#!/usr/bin/python3
'''Open an url and read response'''
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        body = r.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode()))
