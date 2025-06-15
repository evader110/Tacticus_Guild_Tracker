"""This script generates the config files needed for the main module"""

import json
import sys
import requests

MOW = {
    "astraOrdnanceBattery": "Malleus Rocket Launcher",
    "tyranBiovore": "Biovore",
    "blackForgefiend": "Forgefiend",
    "ultraDreadnought": "Galatian",
    "tauBroadside": "Tson'ji",
    "deathCrawler": "Plagueburst Crawler"
}

NotImplementedHeroes = {
    "custoTrajann": "Trajann",
    "custoAesoth": "Aesoth",
}

ENDPOINTS = {
    "guild": "https://api.tacticusgame.com/api/v1/guild",
    "guildRaid": "https://api.tacticusgame.com/api/v1/guildRaid",
    "player": "https://api.tacticusgame.com/api/v1/player"
}

def generate_data(personal_api_key='', guild_api_key='', output_file='../conf.json'):
    headers = {
        'X-Api-key': personal_api_key
    }
    response = requests.get('https://api.tacticusgame.com/api/v1/player', headers=headers, timeout=5)
    if response.status_code != 200:
        print(f"Failed with status code {response.status_code}:")
        print(response.text)
    data=response.json()
    output = {
        'api-keys': {
            'personal': personal_api_key,
            'guild': guild_api_key
        },
        'heroes': {},
        'mow': MOW,
        'endpoints': ENDPOINTS,
    }
    for unit in data['player']['inventory']['shards']:
        if unit['id'] not in MOW:
            output['heroes'][unit['id']] = unit['name'].split(' Shards')[0]
    output['heroes'] = output['heroes'] | NotImplementedHeroes
    with open(output_file, 'w') as f:
        json.dump(output, f, indent=4)

if __name__ == '__main__':
    generate_data(sys.argv[1], sys.argv[2])
