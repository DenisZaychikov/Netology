import requests


def get_most_intelligence_superhero(superheroes_intelligence):
    max_val = 0
    superhero = ''
    for key in superheroes_intelligence:
        if superheroes_intelligence[key] > max_val:
            max_val = superheroes_intelligence[key]
            superhero = key

    return superhero


def get_supehoro_intelligence(hero_id, token):
    url = f'https://superheroapi.com/api/{token}/{hero_id}/powerstats'
    response = requests.get(url)
    response.raise_for_status()
    hero_data = response.json()
    intelligence = int(hero_data['intelligence'])

    return intelligence


def get_superhero_id(name, token):
    url = f'https://superheroapi.com/api/{token}/search/{name}'
    response = requests.get(url)
    response.raise_for_status()
    hero_data = response.json()
    hero_id = hero_data['results'][0]['id']

    return hero_id


if __name__ == '__main__':
    superheroes = ['Hulk', 'Captain America', 'Thanos']
    token = '2619421814940190'
    superheroes_intelligence = {}
    for superhero in superheroes:
        hero_id = get_superhero_id(superhero, token)
        hero_intelligence = get_supehoro_intelligence(hero_id, token)
        superheroes_intelligence[superhero] = hero_intelligence
    most_intelligence_superhero = get_most_intelligence_superhero(
        superheroes_intelligence)
    print(f'Самый умный из супергероев это {most_intelligence_superhero}')
