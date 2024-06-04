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

from kleister.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_attach_user_to_mod(self) -> None:
        """Test case for attach_user_to_mod

        Attach a mod to user
        """
        pass

    def test_attach_user_to_pack(self) -> None:
        """Test case for attach_user_to_pack

        Attach a pack to user
        """
        pass

    def test_attach_user_to_team(self) -> None:
        """Test case for attach_user_to_team

        Attach a team to user
        """
        pass

    def test_create_user(self) -> None:
        """Test case for create_user

        Create a new user
        """
        pass

    def test_delete_user(self) -> None:
        """Test case for delete_user

        Delete a specific user
        """
        pass

    def test_delete_user_from_mod(self) -> None:
        """Test case for delete_user_from_mod

        Unlink a mod from user
        """
        pass

    def test_delete_user_from_pack(self) -> None:
        """Test case for delete_user_from_pack

        Unlink a pack from user
        """
        pass

    def test_delete_user_from_team(self) -> None:
        """Test case for delete_user_from_team

        Unlink a team from user
        """
        pass

    def test_list_user_mods(self) -> None:
        """Test case for list_user_mods

        Fetch all mods attached to user
        """
        pass

    def test_list_user_packs(self) -> None:
        """Test case for list_user_packs

        Fetch all packs attached to user
        """
        pass

    def test_list_user_teams(self) -> None:
        """Test case for list_user_teams

        Fetch all teams attached to user
        """
        pass

    def test_list_users(self) -> None:
        """Test case for list_users

        Fetch all available users
        """
        pass

    def test_permit_user_mod(self) -> None:
        """Test case for permit_user_mod

        Update mod perms for user
        """
        pass

    def test_permit_user_pack(self) -> None:
        """Test case for permit_user_pack

        Update pack perms for user
        """
        pass

    def test_permit_user_team(self) -> None:
        """Test case for permit_user_team

        Update team perms for user
        """
        pass

    def test_show_user(self) -> None:
        """Test case for show_user

        Fetch a specific user
        """
        pass

    def test_update_user(self) -> None:
        """Test case for update_user

        Update a specific user
        """
        pass


if __name__ == '__main__':
    unittest.main()
