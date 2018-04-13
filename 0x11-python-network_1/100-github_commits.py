#!/usr/bin/python3
'''Get user commit from GitHub api'''
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'\
          .format(sys.argv[2], sys.argv[1])
    r = requests.get(url)
    json = r.json()
    result = []
    for obj in json:
        sha = obj.get('sha')
        name = obj.get('commit').get('author').get('name')
        add = sha + ': ' + name
        result.append(add)
    for i in range(10):
        try:
            print(result[i])
        except:
            pass
