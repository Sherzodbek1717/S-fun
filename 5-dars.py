# import requests
# from pprint import pprint
# import json
# req = requests.get('https://jsonplaceholder.typicode.com/posts')
# posts = req.json()
# json_data = []
# for post in posts:
#     userId = post['userId']
#     post_id = post['id']
#     post_title = post['title']
#     post_body = post['body']
#
#     user_req = requests.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
#     user = user_req.json()
#     pprint(user_req.json())
#     name = user['name']
#     username = user['username']
#     email = user['email']
#     address = f"City: {user['address']['city']}, street: {user['address']['street']}"
#
#     json_data.append({
#         'post': {
#             'id': post_id,
#             'title': post_title,
#             'body': post_body
#         },
#         'user':{
#             'id': userId,
#             'name': name,
#             'username': username,
#             'email': email,
#             'address': address
#         }
#     })
# with open('posts_and_users.json', mode='w', encoding='utf-8') as json_file:
#     json.dump(json_data, json_file)

import requests
from pprint import pprint
parametrs = {
    'appid': 'c70298de0dd3baaebdcb81f392b59b90',
    'q': 'Tashkent'

}
data = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=parametrs).json()
pprint(data)
