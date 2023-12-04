#!/usr/bin/python3
"""A python script that fetches https://intranet.hbtn.io/status."""
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        htmlPg = response.read()

        print('Body response:')
        print('\t- type: {}'.format(type(htmlPg)))
        print('\t- content: {}'.format(htmlPg))
        print('\t- utf8 content: {}'.format(htmlPg.decode("utf-8", "replace")))
