import unittest

from main import Guild, load_config


class TestGuild(unittest.TestCase):
    def setUp(self):
        self.guild = Guild(load_config('tests/test_config.json'))

    def test_guild(self):
        self.assertEqual(self.guild.name, '')
        self.assertEqual(self.guild.members, {})
        self.assertEqual(self.guild.headers['personal'], {'X-Api-Key': 'test-123232-33434343'})
        self.assertEqual(self.guild.headers['guild'], {'X-Api-Key': 'guild-2342525-25253524'})
        self.assertDictEqual(self.guild.mow, {
            "astraOrdnanceBattery": "Malleus Rocket Launcher",
            "tyranBiovore": "Biovore",
            "blackForgefiend": "Forgefiend",
            "ultraDreadnought": "Galatian",
            "tauBroadside": "Tson'ji",
            "deathCrawler": "Plagueburst Crawler"
        })


    def test_load_guild_fails(self):
        with self.assertRaises(RuntimeError):
            self.guild.load_guild()
        self.assertEqual(self.guild.name, '')
        self.assertEqual(self.guild.members, {})

    # def test_load_guild_pass(self):
    #     self.guild = Guild('conf.json')
    #     self.guild.load_guild()
    #     self.assertEqual(self.guild.name, '')
    #     self.assertEqual(self.guild.members, {})



if __name__ == '__main__':
    unittest.main()
