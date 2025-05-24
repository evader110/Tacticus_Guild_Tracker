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
        self.assertDictEqual(self.guild.heroes, {
            "ultraTigurius": "Tigurius",
            "ultraInceptorSgt": "Bellator",
            "ultraEliminatorSgt": "Certus",
            "adeptRetributor": "Vindicta",
            "ultraApothecary": "Incisus",
            "necroWarden": "Makhotep",
            "necroDestroyer": "Imospekh",
            "deathBlightlord": "Maladus",
            "eldarFarseer": "Eldryon",
            "eldarRanger": "Calandis",
            "necroSpyder": "Aleph-Null",
            "adeptHospitaller": "Isabella",
            "deathPutrifier": "Pestillian",
            "darkaHellblaster": "Sarquael",
            "blackHaarken": "Haarken",
            "eldarAutarch": "Aethana",
            "orksKillaKan": "Snappawrecka",
            "adeptCanoness": "Roswitha",
            "blackTerminator": "Angrax",
            "thousTzaangor": "Yazaghor",
            "orksBigMek": "Gibbascrapz",
            "tauMarksman": "Sho'syl",
            "blackPossession": "Archimatos",
            "tauDarkstrider": "Darkstrider",
            "necroPlasmancer": "Thutmose",
            "admecMarshall": "Tan Gi'da",
            "orksRuntherd": "Snotflogga",
            "worldEightbound": "Azkor",
            "templSwordBrother": "Godswyl",
            "astraPrimarisPsy": "Sibyll",
            "spaceHound": "Tjark",
            "worldTerminator": "Wrask",
            "thousTerminator": "Toth",
            "darkaTerminator": "Baraqiel",
            "tyranNeurothrope": "Neurothrope",
            "thousInfernalMaster": "Abraxas",
            "darkaAzrael": "Azrael",
            "orksWarboss": "Gulgortz",
            "spaceWulfen": "Ulf",
            "orksNob": "Tanksmasha",
            "bloodIntercessor": "Mataneo",
            "tyranTyrantGuard": "Tyrant Guard",
            "deathRotbone": "Nauseous",
            "templAggressor": "Burchard",
            "astraYarrick": "Yarrick",
            "bloodDeathCompany": "Lucien",
            "ultraTitus": "Titus",
            "tauAunShi": "Aun'Shi",
            "admecDominus": "Vitruvius",
            "genesMagus": "Xybia",
            "thousAhriman": "Ahriman",
            "tyranWingedPrime": "Winged Prime",
            "genesPatriarch": "The Patermine",
            "genesBiophagus": "Hollan",
            "necroOverlord": "Anuphet",
            "admecManipulus": "Actus",
            "admecRuststalker": "Exitor-Rho",
            "worldJakhal": "Macer",
            "tauCrisis": "Re'vas",
            "worldKharn": "Kharn",
            "adeptMorvenn": "Morvenn Vahl",
            "spaceBlackmane": "Ragnar",
            "astraBullgryn": "Kut",
            "templAncient": "Thoread",
            "tyranDeathleaper": "Deathleaper",
            "bloodSanguinary": "Nicodemus",
            "tyranParasite": "Parasite of Mortrex",
            "deathBlightbringer": "Corrodius",
            "astraOrdnance": "Thaddeus",
            "bloodMephiston": "Mephiston",
            "blackObliterator": "Volk",
            "genesPrimus": "Isaak",
            "admecDestroyer": "Sy-gex",
            "spaceRockfist": "Arjac",
            "thousSorcerer": "Thaumachus",
            "bloodDante": "Dante",
            "worldExecutions": "Tarvakh",
            "genesKelermorph": "Judh",
            "darkaCompanion": "Forcas"
        })
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
