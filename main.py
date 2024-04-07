import requests
import random

def get_random_disney_character():
    page = random.randint(1, 7438)
    pageSize = 1
    url = f'https://api.disneyapi.dev/character?pageSize={pageSize}&page={page}'
    response = requests.get(url)
    if response.ok:
        data = response.json()['data']
        character_info = {
            "Ім'я": data['name'],
            "Фільми": data['films'],
            "Короткометражки": data['shortFilms'],
            "Серіали": data['tvShows'],
            "Відеоігри": data['videoGames']
        }
        return character_info
    else:
        print('Щось пішло не так...')
        print(f'{response.status_code=}')

if __name__ == "__main__":
    character = get_random_disney_character()
    if character:
        print("Ім'я:", character["Ім'я"])
        print("Фільми:", ', '.join(character["Фільми"]))
        print("Короткометражки:", ', '.join(character["Короткометражки"]))
        print("Серіали:", ', '.join(character["Серіали"]))
        print("Відеоігри:", ', '.join(character["Відеоігри"]))
