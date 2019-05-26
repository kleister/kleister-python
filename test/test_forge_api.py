# coding: utf-8

"""
    Kleister OpenAPI

    API definition for Kleister, manage mod packs for Minecraft  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kleister
from kleister.api.forge_api import ForgeApi  # noqa: E501
from kleister.rest import ApiException


class TestForgeApi(unittest.TestCase):
    """ForgeApi unit test stubs"""

    def setUp(self):
        self.api = kleister.api.forge_api.ForgeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_append_forge_to_build(self):
        """Test case for append_forge_to_build

        Assign a build to a Forge version  # noqa: E501
        """
        pass

    def test_delete_forge_from_build(self):
        """Test case for delete_forge_from_build

        Unlink a build from a Forge version  # noqa: E501
        """
        pass

    def test_list_forge_builds(self):
        """Test case for list_forge_builds

        Fetch the builds assigned to a Forge version  # noqa: E501
        """
        pass

    def test_list_forges(self):
        """Test case for list_forges

        Fetch the available Forge versions  # noqa: E501
        """
        pass

    def test_search_forges(self):
        """Test case for search_forges

        Search for available Forge versions  # noqa: E501
        """
        pass

    def test_update_forge(self):
        """Test case for update_forge

        Update the available Forge versions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
