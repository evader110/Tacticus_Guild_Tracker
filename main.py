"""This is the main module used for running the Guild Hit Tracker"""

import time
import json
import requests
import schedule

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
        self.mow = config['mow']
        self.config = config
        self.current_season = -1
        self.current_season_entries = {}
        self.current_season_hits = {}

    def load_guild(self):
        guild_res = requests.get(self.config['endpoints']['guild'], headers=self.headers['guild'])
        guild_season = requests.get(self.config['endpoints']['guildRaid'], headers=self.headers['guild'])

        if guild_res.status_code != 200:
            raise RuntimeError(guild_res.text)
        if guild_season.status_code != 200:
            raise RuntimeError(guild_season.text)

        guild_data = guild_res.json()
        raid_data = guild_season.json()
        self.name = guild_data['guild']['name']
        self.members = guild_data['guild']['members']
        self.current_season = raid_data['season']
        self.current_season_entries = raid_data['entries']

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
    guild.load_guild()
    print(guild.name)
    # pprint_list(guild.members)
    print(f'Season {guild.current_season}')
    # pprint_list(guild.current_season_entries)
    guild.print_entries()
    # schedule.every(1).hours.do(guild.load_units)
    # r = requests.get(guild.config['endpoints']['player'], headers=guild.headers['personal'])
    # print(r.text)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
