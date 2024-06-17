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

from kleister.models.minecraft_build_params import MinecraftBuildParams

class TestMinecraftBuildParams(unittest.TestCase):
    """MinecraftBuildParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MinecraftBuildParams:
        """Test MinecraftBuildParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MinecraftBuildParams`
        """
        model = MinecraftBuildParams()
        if include_optional:
            return MinecraftBuildParams(
                pack = '',
                build = ''
            )
        else:
            return MinecraftBuildParams(
                pack = '',
                build = '',
        )
        """

    def testMinecraftBuildParams(self):
        """Test MinecraftBuildParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()