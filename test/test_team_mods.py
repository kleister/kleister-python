# coding: utf-8

"""
    Kleister OpenAPI

    API definition for Kleister, manage mod packs for Minecraft

    The version of the OpenAPI document: 1.0.0-alpha1
    Contact: kleister@webhippie.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kleister.models.team_mods import TeamMods

class TestTeamMods(unittest.TestCase):
    """TeamMods unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamMods:
        """Test TeamMods
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamMods`
        """
        model = TeamMods()
        if include_optional:
            return TeamMods(
                team = kleister.models.team.Team(
                    id = '', 
                    slug = '', 
                    name = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                total = 56,
                mods = [
                    kleister.models.team_mod.Team Mod(
                        team_id = '', 
                        team = kleister.models.team.Team(
                            id = '', 
                            slug = '', 
                            name = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        mod_id = '', 
                        mod = kleister.models.mod.Mod(
                            id = '', 
                            slug = '', 
                            name = '', 
                            side = 'both', 
                            description = '', 
                            author = '', 
                            website = '', 
                            donate = '', 
                            public = True, 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        perm = 'team', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return TeamMods(
        )
        """

    def testTeamMods(self):
        """Test TeamMods"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
