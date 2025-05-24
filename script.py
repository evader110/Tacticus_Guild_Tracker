import json
import requests
import schedule, time

def load_conf(filename = 'conf.json'):
    data = {}
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

conf = load_conf()

bosses = {

}

class Guild:
    def __init__(self):
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
        self.headers = {}
        self.heroes = {}
        self.mow = {}

    def set_api_keys(self, filename):
        with open(filename) as f:
            data = json.load(f)
            self.headers = {
                'personal': {
                    'X-Api-Key': data['Personal'],
                },
                'guild': {
                    'X-Api-Key': data['Guild'],
                },
            }

    def load_guild(self):
        response = requests.get(self.api_url + self.endpoints['Guild'], headers=self.headers['guild'])
        if response.status_code != 200:
            print(f"Failed with status code {response.status_code}:")
            print(response.text)

        data = response.json()
        self.name = data['guild']['name']
        self.members = data['guild']['members']

    def load_units(self, filename):
        with open(filename) as f:
            data = json.load(f)
            self.heroes = data['heroes']
            self.mow = data['mow']

    # def display_team(self):



if __name__ == '__main__':
    guild = Guild()
    guild.set_api_keys(api_keys)
    guild.load_units(units_file)
    print(guild.heroes)
    print(guild.mow)
    schedule.every(1).hours.do(guild.load_units)
    response = requests.get(guild.endpoints['player'], headers=guild.headers['personal'])
    print(response.text)

    while True:
        schedule.run_pending()
        time.sleep(1)