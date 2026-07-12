import requests 

# Url that I will make the request.
# urls = [];
url = 'https://medium.com/'

response = requests.get(url)
print(response.headers['content-type'])
print(response.text)

#r.headers['']

