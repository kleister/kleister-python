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

from kleister.models.packs import Packs

class TestPacks(unittest.TestCase):
    """Packs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Packs:
        """Test Packs
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Packs`
        """
        model = Packs()
        if include_optional:
            return Packs(
                total = 56,
                packs = [
                    kleister.models.pack.Pack(
                        id = '', 
                        icon = kleister.models.pack_icon.Pack Icon(
                            id = '', 
                            slug = '', 
                            content_type = '', 
                            md5 = '', 
                            path = '', 
                            url = '', 
                            upload = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        logo = kleister.models.pack_logo.Pack Logo(
                            id = '', 
                            slug = '', 
                            content_type = '', 
                            md5 = '', 
                            path = '', 
                            url = '', 
                            upload = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        back = kleister.models.pack_background.Pack Background(
                            id = '', 
                            slug = '', 
                            content_type = '', 
                            md5 = '', 
                            path = '', 
                            url = '', 
                            upload = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        slug = '', 
                        name = '', 
                        website = '', 
                        public = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return Packs(
        )
        """

    def testPacks(self):
        """Test Packs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
