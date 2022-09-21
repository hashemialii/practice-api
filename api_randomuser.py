import requests
import os

response = requests.get('https://randomuser.me/api/?nat=ir')
print(response)  # Response [200]: has been sent correctly
print(response.text)

base_url = 'https://randomuser.me/'
end_point = 'api/?nat=ir&gender=female'

# HTTP status codes: # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# Informational responses (100–199)
# Successful responses (200–299)
# Redirection messages (300–399)
# Client error responses (400–499)
# Server error responses (500–599)

# HTTP Methods:     https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
# GET, POST, PUT, DELETE, PATH, TRACE, HEAD, OPTION, CONNECT

print(40 * '=')

print(response.content)  # binary (it is good for image data)
print(response.text)

print(40 * '=')

print(response.status_code)    # get status code
print(response.reason)

print(40 * '=')

print(response.headers)     # details of your request (query)


req = response.request
print(req.headers)      # User-Agent: What did you submit your application with?
print(req.path_url)     # endpoint
print(req.url)          # full request url
print(req.method)       # which method I have used

print(40 * '=')


base_url = 'https://randomuser.me/'
end_point = 'api/?nat=ir&gender=female'

# when you write like this, you can iteration on end_point

# 1:

api_url = os.path.join(base_url, end_point)
print(api_url)     # when you write like this, you can iteration on end_point

print(40 * '=')

# 2:

base_url = 'https://randomuser.me/'
query_parameter = {'nat': 'ir',
                   'gender': 'female',
                   }
response = requests.get(api_url, params=query_parameter)
print(response.json())












