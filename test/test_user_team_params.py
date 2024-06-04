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

from kleister.models.user_team_params import UserTeamParams

class TestUserTeamParams(unittest.TestCase):
    """UserTeamParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserTeamParams:
        """Test UserTeamParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserTeamParams`
        """
        model = UserTeamParams()
        if include_optional:
            return UserTeamParams(
                team = '',
                perm = 'user'
            )
        else:
            return UserTeamParams(
                team = '',
        )
        """

    def testUserTeamParams(self):
        """Test UserTeamParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
