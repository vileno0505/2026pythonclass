import requests
import os
import urllib.request as req

url='https://tw.portal-pokemon.com/play/pokedex/api/v1?pokemon_ability_id=&zukan_id_from=1&zukan_id_to=1025'
img_url='https://tw.portal-pokemon.com/play/resources/pokedex'

response = requests.get(url)
pokemons=response.json()
os.makedirs('pokemons',exist_ok=True)
for pokemon in pokemons['pokemons']:
    name=pokemon['pokemon_name']
    img = f'{img_url}{pokemon["file_name"]}'
    req.urlretrieve(img,f'pokemons/{name}.png')