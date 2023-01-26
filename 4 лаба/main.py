import json

import requests
from pprint import pprint

username = "ktsaou"
url = f"https://api.github.com/users/{username}"

user_data = requests.get(url).json()
res = requests.get('https://scotch.io')
user_data = requests.get(url).json()
pprint(user_data)

with open("data_file.json", "w") as write_file:
    json.dump(user_data, write_file)

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
pprint(data)
print(type(data))

with open("out.txt", 'w') as out:
    out.write('company: '+str(data['company'])+'\n')
    out.write('created_at: ' + str(data['created_at']) + '\n')
    out.write('email: ' + str(data['email']) + '\n')
    out.write('id: ' + str(data['id']) + '\n')
    out.write('name: ' + str(data['name']) + '\n')
    out.write('url: ' + str(data['url']) + '\n')