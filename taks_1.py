import requests

superheros = ["Hulk", "Captain America", "Thanos"]
url = 'https://akabab.github.io/superhero-api/api/all.json'
dict_super = {}

res = requests.get(url).json()

for name in res:
    if name['name'] in superheros:
        intelligence = name['powerstats']['intelligence']
        dict_super[name['name']] = intelligence
for name in superheros:
    if max(dict_super.values()) == dict_super[name]:
        print(f'Самый умный супергерой {name}')


