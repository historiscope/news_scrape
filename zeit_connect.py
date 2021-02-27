import requests
import newspapers

# settings for the general site
my_token = 'e95117f10bc2a32e551d4bbbcf3e2d78a3d60c4b1421a65aa75e'
base_url = 'http://api.zeit.de'
# settings for the specific endpoint
endpoint = 'content'
endpoint_url = f'{base_url}/{endpoint}?api_key={my_token}'
#headers = {'X-Authorization': my_token}

# settings for the specific search query
keyword_search = 'Migranten+Merkel' # search for all occurrences of 'Migrant' and 'Merkel'
limit = 100 # limit the result set to 100

# pass the settings and parameters to the get request
search_params = {'q':keyword_search, 'limit':limit} # format the parameters to work with Zeit
response = requests.get(endpoint_url, params=search_params) # send the request!

# look at the keys for the dictionary produced by the pull request
print(response.json().keys())

# the data itself is in 'matches'. Select that element from the dictionary and convert it to a dataframe:
df = pd.DataFrame(response.json()['matches'])

