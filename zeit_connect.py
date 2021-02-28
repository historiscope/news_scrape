import requests
import pandas as pd 
import urllib
from bs4 import BeautifulSoup

# settings for the general site
my_token = 'e95117f10bc2a32e551d4bbbcf3e2d78a3d60c4b1421a65aa75e'
base_url = 'http://api.zeit.de'
# settings for the specific endpoint
endpoint = 'content'
endpoint_url = f'{base_url}/{endpoint}?api_key={my_token}'
#headers = {'X-Authorization': my_token}

# settings for the specific search query
keyword_search = 'Migranten' # search for all occurrences of 'Migrant'
limit = 100 # limit the result set to 100 for now

# pass the settings and parameters to the get request
search_params = {'q':keyword_search, 'limit':limit} # see Zeit site for additional options http://developer.zeit.de/docs/content/
response = requests.get(endpoint_url, params=search_params) # send the request!

# look at the keys for the json dictionary produced by the pull request
print(response.json().keys())

# the data itself is in 'matches'. Select the matches element from the dictionary and convert it to a dataframe:
df = pd.DataFrame(response.json()['matches'])

print(f'Your options are: {df.columns}')
print(df[['title','href','release_date']])

url_lst = df['href'].tolist()[0:10]

# iterate over the url list -- > for every url in the list
u = url_lst[0]

# retrieve the page
page = urllib.request.urlopen(u)
# convert it to soup
soup = BeautifulSoup(page)
# find the article div
t = soup.find("div", {"class":"article-body"})
# for every paragraph in that div, return the text
paras = t.findAll('p')
paras[0].text