import json
import requests
import schedule, time

heroes = {}

def get_hero_name(hero_id):
    return heroes[hero_id]

def pprint_list(i_list):
    for item in i_list:
        print(item)

def load_config(filename = 'conf.json'):
    data = {}
    with open(filename) as json_file:
        data = json.load(json_file)
    global heroes
    heroes = data['heroes'] # Not good. Is repeated...
    return data


def get_entry_hero_names(entry):
    l = []
    for hero in entry['heroDetails']:
        l.append(get_hero_name(hero['unitId']))
    return l

class Guild:
    def __init__(self, config):
        self.name = ''
        # Members:
        #   Name
        #   Hits
        #   Boss
        #       Level
        #           Team
        #           Damage
        #           Season
        #       SideBoss
        #           Level
        #               Team
        #               Damage
        #               Season
        self.members = {}
        self.headers = {
            'personal': {
                'X-Api-Key': config['api-keys']['personal'],
            },
            'guild': {
                'X-Api-Key': config['api-keys']['guild'],
            },
        }
        self.heroes = config['heroes']
        self.mow = config['mow']
        self.config = config


    def load_guild(self):
        response = requests.get(self.config['endpoints']['guild'], headers=self.headers['guild'])
        if response.status_code != 200:
            raise RuntimeError(response.text)
        data = response.json()
        self.name = data['guild']['name']
        self.members = data['guild']['members']
    def print_entries(self):
        for entry in self.current_season_entries:
            boss = entry['type']
            boss_rarity = entry['rarity']
            damage_dealt = entry['damageDealt']
            hero_names = get_entry_hero_names(entry)
            if len(hero_names) > 0:
                print([[boss, boss_rarity], hero_names, damage_dealt])

    # def display_team(self):

if __name__ == '__main__':
    guild = Guild(config=load_config())
    print(guild.heroes)
    print(guild.mow)
    # schedule.every(1).hours.do(guild.load_units)
    # r = requests.get(guild.config['endpoints']['player'], headers=guild.headers['personal'])
    # print(r.text)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)