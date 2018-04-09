#!/usr/bin/python3
'''Open an url and read response'''
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body resonse:')
    print('    -type: {}'.format(type(r.text)))
    print('    -content: {}'.format(r.text))
