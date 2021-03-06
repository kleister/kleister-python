"""
    Kleister OpenAPI

    API definition for Kleister, manage mod packs for Minecraft  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


import unittest

import kleister
from kleister.api.profile_api import ProfileApi  # noqa: E501


class TestProfileApi(unittest.TestCase):
    """ProfileApi unit test stubs"""

    def setUp(self):
        self.api = ProfileApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_show_profile(self):
        """Test case for show_profile

        Retrieve an unlimited auth token  # noqa: E501
        """
        pass

    def test_token_profile(self):
        """Test case for token_profile

        Retrieve an unlimited auth token  # noqa: E501
        """
        pass

    def test_update_profile(self):
        """Test case for update_profile

        Retrieve an unlimited auth token  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
