"""
    Kleister OpenAPI

    API definition for Kleister, manage mod packs for Minecraft  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


import unittest

import kleister
from kleister.api.mod_api import ModApi  # noqa: E501


class TestModApi(unittest.TestCase):
    """ModApi unit test stubs"""

    def setUp(self):
        self.api = ModApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_append_mod_to_team(self):
        """Test case for append_mod_to_team

        Assign a team to mod  # noqa: E501
        """
        pass

    def test_append_mod_to_user(self):
        """Test case for append_mod_to_user

        Assign a user to mod  # noqa: E501
        """
        pass

    def test_append_version_to_build(self):
        """Test case for append_version_to_build

        Assign a build to a version  # noqa: E501
        """
        pass

    def test_create_mod(self):
        """Test case for create_mod

        Create a new mod  # noqa: E501
        """
        pass

    def test_create_version(self):
        """Test case for create_version

        Create a new version for a mod  # noqa: E501
        """
        pass

    def test_delete_mod(self):
        """Test case for delete_mod

        Delete a specific mod  # noqa: E501
        """
        pass

    def test_delete_mod_from_team(self):
        """Test case for delete_mod_from_team

        Remove a team from mod  # noqa: E501
        """
        pass

    def test_delete_mod_from_user(self):
        """Test case for delete_mod_from_user

        Remove a user from mod  # noqa: E501
        """
        pass

    def test_delete_version(self):
        """Test case for delete_version

        Delete a specific version for a mod  # noqa: E501
        """
        pass

    def test_delete_version_from_build(self):
        """Test case for delete_version_from_build

        Unlink a build from a version  # noqa: E501
        """
        pass

    def test_list_mod_teams(self):
        """Test case for list_mod_teams

        Fetch all teams assigned to mod  # noqa: E501
        """
        pass

    def test_list_mod_users(self):
        """Test case for list_mod_users

        Fetch all users assigned to mod  # noqa: E501
        """
        pass

    def test_list_mods(self):
        """Test case for list_mods

        Fetch all available mods  # noqa: E501
        """
        pass

    def test_list_version_builds(self):
        """Test case for list_version_builds

        Fetch all builds assigned to version  # noqa: E501
        """
        pass

    def test_list_versions(self):
        """Test case for list_versions

        Fetch all available versions for a mod  # noqa: E501
        """
        pass

    def test_permit_mod_team(self):
        """Test case for permit_mod_team

        Update team perms for mod  # noqa: E501
        """
        pass

    def test_permit_mod_user(self):
        """Test case for permit_mod_user

        Update user perms for mod  # noqa: E501
        """
        pass

    def test_show_mod(self):
        """Test case for show_mod

        Fetch a specific mod  # noqa: E501
        """
        pass

    def test_show_version(self):
        """Test case for show_version

        Fetch a specific version for a mod  # noqa: E501
        """
        pass

    def test_update_mod(self):
        """Test case for update_mod

        Update a specific mod  # noqa: E501
        """
        pass

    def test_update_version(self):
        """Test case for update_version

        Update a specific version for a mod  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()