import json
import requests
import schedule, time

def load_config(filename = 'conf.json'):
    data = {}
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


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