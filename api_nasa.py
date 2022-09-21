import requests


api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
query_parameter = {'earth_date': '2022-09-18',
                   'api_key': 'VkMldfZFEzVIO1alQnJEzvHBIedaoxxmhisgXVco',
                   }
response = requests.get(api_url, params=query_parameter)
print(response.json())
print(response)


print(response.json().get('photos'))   # to see the photo taken
print(len(response.json().get('photos')))       # number of photos taken that day

print(response.json().get('photos')[0]['img_src'])      # to see first photo
print(response.X-RateLimit-Remaining)












