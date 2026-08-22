import os
import re

import requests
import urllib.request as req

url = 'https://tw.portal-pokemon.com/play/pokedex/api/v1?pokemon_ability_id=&zukan_id_from=1&zukan_id_to=1025'
img_url = 'https://tw.portal-pokemon.com/play/resources/pokedex'

response = requests.get(url)
pokemons = response.json()
os.makedirs('qqq', exist_ok=True)

# print(len(pokemons['pokemons']))
for pokemon in pokemons['pokemons']:

    name = pokemon['pokemon_name']
    sub_name = pokemon['pokemon_sub_name']
    if sub_name != '':
        fullname =f'{name}_{sub_name}'
    else:
        fullname = name
    fullname=re.sub(r'[|\/?:<>]','_',fullname)
    img = f'{img_url}{pokemon["file_name"]}'
    ext = os.path.splitext(img)[1]
    # print(f'pokemons/{name}{ext}')
    req.urlretrieve(img, f'qqq/{fullname}{ext}')
    # print(count,fullname)
