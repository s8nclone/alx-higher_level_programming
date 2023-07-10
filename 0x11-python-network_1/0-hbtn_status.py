#!/usr/bin/python3
"""A python script that fetches https://intranet.hbtn.io/status."""
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        htmlFile = response.read()

        print('Body response:')
        print('\t- type: {}'.format(type(htmlFile)))
        print('\t- content: {}'.format(htmlFile))
        print('\t- utf8 content: {}'.format(htmlFile.decode("utf-8", "replace")))
