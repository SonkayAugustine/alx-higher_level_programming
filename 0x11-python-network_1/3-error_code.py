#!/usr/bin/python3
'''
Take in a URL, send a request to URL, and dispaly body
'''

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.error

    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as er:
        print("Error code:".format(er.code))
