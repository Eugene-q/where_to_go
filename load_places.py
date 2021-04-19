"""
a script for quickly uploading test data 
to the "where to go" project database.
"""

import subprocess
import requests

JSON_LIST = \
    'https://github.com/devmanorg/where-to-go-places/tree/master/places'
JSON_FOLDER = \
    'https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/'

resp = requests.get(JSON_LIST)
text = resp.text
while text:
    trash, sep, text = text.partition('class="js-navigation-open Link--primary" title="')
    if text:
        file_name, sep, text = text.partition('"')
        json_url = ''.join((JSON_FOLDER, file_name.replace(' ', '%20')))
        subprocess.call(['python3', 'manage.py', 'load_place', json_url])
