habilidades = {"abilities": [
    {
    "ability": {
    "name": "limber",
    "url": "https://pokeapi.co/api/v2/ability/7/"
    },
    "is_hidden": False,
    "slot": 1
    },
    {
    "ability": {
    "name": "imposter",
    "url": "https://pokeapi.co/api/v2/ability/150/"
    },
    "is_hidden": True,
    "slot": 3
    }
    ]

}
abilities = habilidades["abilities"][0]["ability"]["url"]
print(abilities)
#print(type(habilidades["abilities"][0]))
#print(habilidades["abilities"][0])