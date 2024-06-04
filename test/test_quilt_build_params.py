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

from kleister.models.quilt_build_params import QuiltBuildParams

class TestQuiltBuildParams(unittest.TestCase):
    """QuiltBuildParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuiltBuildParams:
        """Test QuiltBuildParams
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuiltBuildParams`
        """
        model = QuiltBuildParams()
        if include_optional:
            return QuiltBuildParams(
                pack = '',
                build = ''
            )
        else:
            return QuiltBuildParams(
                pack = '',
                build = '',
        )
        """

    def testQuiltBuildParams(self):
        """Test QuiltBuildParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
