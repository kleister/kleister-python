"""
    Kleister OpenAPI

    API definition for Kleister, manage mod packs for Minecraft  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


import unittest

import kleister
from kleister.api.minecraft_api import MinecraftApi  # noqa: E501


class TestMinecraftApi(unittest.TestCase):
    """MinecraftApi unit test stubs"""

    def setUp(self):
        self.api = MinecraftApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_append_minecraft_to_build(self):
        """Test case for append_minecraft_to_build

        Assign a build to a Minecraft version  # noqa: E501
        """
        pass

    def test_delete_minecraft_from_build(self):
        """Test case for delete_minecraft_from_build

        Unlink a build from a Minecraft version  # noqa: E501
        """
        pass

    def test_list_minecraft_builds(self):
        """Test case for list_minecraft_builds

        Fetch the builds assigned to a Minecraft version  # noqa: E501
        """
        pass

    def test_list_minecrafts(self):
        """Test case for list_minecrafts

        Fetch the available Minecraft versions  # noqa: E501
        """
        pass

    def test_search_minecrafts(self):
        """Test case for search_minecrafts

        Search for available Minecraft versions  # noqa: E501
        """
        pass

    def test_update_minecraft(self):
        """Test case for update_minecraft

        Update the available Minecraft versions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
