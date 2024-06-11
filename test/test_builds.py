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

from kleister.models.builds import Builds

class TestBuilds(unittest.TestCase):
    """Builds unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Builds:
        """Test Builds
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Builds`
        """
        model = Builds()
        if include_optional:
            return Builds(
                total = 56,
                pack = kleister.models.pack.Pack(
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
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                builds = [
                    kleister.models.build.Build(
                        id = '', 
                        pack = kleister.models.pack.Pack(
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
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        minecraft_id = '', 
                        minecraft = kleister.models.minecraft.Minecraft(
                            id = '', 
                            name = '', 
                            type = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        forge_id = '', 
                        forge = kleister.models.forge.Forge(
                            id = '', 
                            name = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        neoforge_id = '', 
                        neoforge = kleister.models.neoforge.Neoforge(
                            id = '', 
                            name = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        quilt_id = '', 
                        quilt = kleister.models.quilt.Quilt(
                            id = '', 
                            name = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        fabric_id = '', 
                        fabric = kleister.models.fabric.Fabric(
                            id = '', 
                            name = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        slug = '', 
                        name = '', 
                        java = '', 
                        memory = '', 
                        latest = True, 
                        recommended = True, 
                        public = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return Builds(
        )
        """

    def testBuilds(self):
        """Test Builds"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
