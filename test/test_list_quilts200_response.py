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

from kleister.models.list_quilts200_response import ListQuilts200Response

class TestListQuilts200Response(unittest.TestCase):
    """ListQuilts200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListQuilts200Response:
        """Test ListQuilts200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListQuilts200Response`
        """
        model = ListQuilts200Response()
        if include_optional:
            return ListQuilts200Response(
                total = 56,
                limit = 56,
                offset = 56,
                versions = [
                    kleister.models.quilt.Quilt(
                        id = '', 
                        name = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return ListQuilts200Response(
                total = 56,
                limit = 56,
                offset = 56,
                versions = [
                    kleister.models.quilt.Quilt(
                        id = '', 
                        name = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testListQuilts200Response(self):
        """Test ListQuilts200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
