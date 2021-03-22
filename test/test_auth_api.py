"""
    Kleister OpenAPI

    API definition for Kleister, manage mod packs for Minecraft  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


import unittest

import kleister
from kleister.api.auth_api import AuthApi  # noqa: E501


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_login_user(self):
        """Test case for login_user

        Authenticate an user by credentials  # noqa: E501
        """
        pass

    def test_refresh_auth(self):
        """Test case for refresh_auth

        Refresh an auth token before it expires  # noqa: E501
        """
        pass

    def test_verify_auth(self):
        """Test case for verify_auth

        Verify validity for an authentication token  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()