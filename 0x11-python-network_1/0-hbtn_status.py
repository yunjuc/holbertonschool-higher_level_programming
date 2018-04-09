#!/usr/bin/python3
'''Open an url and read response'''
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        body = r.read()
        print('Body resonse:')
        print('    -type: {}'.format(type(body)))
        print('    -content: {}'.format(body))
        print('    -utf8 content: {}'.format(body.decode()))
