import requests

endpoint_url = 'http://api.zeit.de/content'
my_token = 'e95117f10bc2a32e551d4bbbcf3e2d78a3d60c4b1421a65aa75e'
headers = {'Host': 'http://api.zeit.de',
           'X-Authorization': my_token)}

response = requests.get(endpoint_url, headers=headers)



