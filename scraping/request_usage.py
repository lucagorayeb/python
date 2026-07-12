import requests

# GET
""" get = requests.get('https://httpbin.org/');
print(get) """

# POST
""" post = requests.post('https://httpbin.org/post', data={'nome': 'Luca'})
print(post) """

# PUT
""" put = requests.put('https://httpbin.org/put', data={'nome': 'Larissa'})
print(put) """

# DELETE 
""" delete = requests.delete('https://httpbin.org/delete')
print(delete) """

# HEAD 
""" head = requests.head('https://httpbin.org/get')
print(head) """

# OPTIONS
""" options = requests.options('https://httpbin.org/get')
print(options) """

# Passing Params through requests
""" url = 'https://httpbin.org/post'
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, params=payload)
print(response.url) """

# Passing a dict param request
""" url = 'https://httpbin.org/post'
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
response = requests.post(url, params=payload)
print(response.url) """

# Requests Response 
r = requests.get('https://api.github.com/events', stream = True)
# The enconding could be changed, because when the response of the server
# return it will be in the write encoding.
""" print(r.encoding) # Encode return
print(r.text) # Text content returned 
print(r.content) # Contente returned
print(r.json()) # JSON returned  """
print(r.raw.read(10))