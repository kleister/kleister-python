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

from kleister.models.user_pack import UserPack

class TestUserPack(unittest.TestCase):
    """UserPack unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserPack:
        """Test UserPack
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserPack`
        """
        model = UserPack()
        if include_optional:
            return UserPack(
                user_id = '',
                user = kleister.models.user.User(
                    id = '', 
                    username = '', 
                    password = '', 
                    email = '', 
                    fullname = '', 
                    profile = '', 
                    admin = True, 
                    active = True, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    auths = [
                        kleister.models.user_auth.User Auth(
                            provider = '', 
                            ref = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    teams = [
                        kleister.models.user_team.User Team(
                            user_id = '', 
                            team_id = '', 
                            team = kleister.models.team.Team(
                                id = '', 
                                slug = '', 
                                name = '', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                users = [
                                    kleister.models.user_team.User Team(
                                        user_id = '', 
                                        team_id = '', 
                                        perm = 'user', 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                    ], 
                                packs = [
                                    kleister.models.team_pack.Team Pack(
                                        team_id = '', 
                                        pack_id = '', 
                                        pack = kleister.models.pack.Pack(
                                            id = '', 
                                            icon = kleister.models.pack_icon.Pack Icon(
                                                id = '', 
                                                pack_id = '', 
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
                                                pack_id = '', 
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
                                                pack_id = '', 
                                                slug = '', 
                                                content_type = '', 
                                                md5 = '', 
                                                path = '', 
                                                url = '', 
                                                upload = '', 
                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                            recommended_id = '', 
                                            recommended = kleister.models.build.Build(
                                                id = '', 
                                                pack_id = '', 
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
                                                public = True, 
                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                versions = [
                                                    kleister.models.build_version.Build Version(
                                                        build_id = '', 
                                                        build = kleister.models.build.Build(
                                                            id = '', 
                                                            pack_id = '', 
                                                            minecraft_id = '', 
                                                            forge_id = '', 
                                                            neoforge_id = '', 
                                                            quilt_id = '', 
                                                            fabric_id = '', 
                                                            slug = '', 
                                                            name = '', 
                                                            java = '', 
                                                            memory = '', 
                                                            public = True, 
                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                                        version_id = '', 
                                                        version = kleister.models.version.Version(
                                                            id = '', 
                                                            file = kleister.models.version_file.Version File(
                                                                id = '', 
                                                                version_id = '', 
                                                                slug = '', 
                                                                content_type = '', 
                                                                md5 = '', 
                                                                path = '', 
                                                                url = '', 
                                                                upload = '', 
                                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                                            mod_id = '', 
                                                            mod = kleister.models.mod.Mod(
                                                                id = '', 
                                                                slug = '', 
                                                                name = '', 
                                                                side = 'both', 
                                                                description = '', 
                                                                author = '', 
                                                                website = '', 
                                                                donate = '', 
                                                                public = True, 
                                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                                            slug = '', 
                                                            name = '', 
                                                            public = True, 
                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            builds = [
                                                                kleister.models.build_version.Build Version(
                                                                    build_id = '', 
                                                                    version_id = '', 
                                                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                                ], ), 
                                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                    ], ), 
                                            latest_id = '', 
                                            latest = , 
                                            slug = '', 
                                            name = '', 
                                            website = '', 
                                            public = True, 
                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            builds = [
                                                
                                                ], ), 
                                        perm = 'team', 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                    ], 
                                mods = [
                                    kleister.models.team_mod.Team Mod(
                                        team_id = '', 
                                        mod_id = '', 
                                        perm = 'team', 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                    ], ), 
                            perm = 'user', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    packs = [
                        kleister.models.user_pack.User Pack(
                            user_id = '', 
                            pack_id = '', 
                            perm = 'user', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    mods = [
                        kleister.models.user_mod.User Mod(
                            user_id = '', 
                            mod_id = '', 
                            perm = 'user', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ),
                pack_id = '',
                pack = kleister.models.pack.Pack(
                    id = '', 
                    icon = kleister.models.pack_icon.Pack Icon(
                        id = '', 
                        pack_id = '', 
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
                        pack_id = '', 
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
                        pack_id = '', 
                        slug = '', 
                        content_type = '', 
                        md5 = '', 
                        path = '', 
                        url = '', 
                        upload = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    recommended_id = '', 
                    recommended = kleister.models.build.Build(
                        id = '', 
                        pack_id = '', 
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
                        public = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        versions = [
                            kleister.models.build_version.Build Version(
                                build_id = '', 
                                build = kleister.models.build.Build(
                                    id = '', 
                                    pack_id = '', 
                                    minecraft_id = '', 
                                    forge_id = '', 
                                    neoforge_id = '', 
                                    quilt_id = '', 
                                    fabric_id = '', 
                                    slug = '', 
                                    name = '', 
                                    java = '', 
                                    memory = '', 
                                    public = True, 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                version_id = '', 
                                version = kleister.models.version.Version(
                                    id = '', 
                                    file = kleister.models.version_file.Version File(
                                        id = '', 
                                        version_id = '', 
                                        slug = '', 
                                        content_type = '', 
                                        md5 = '', 
                                        path = '', 
                                        url = '', 
                                        upload = '', 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                    mod_id = '', 
                                    mod = kleister.models.mod.Mod(
                                        id = '', 
                                        slug = '', 
                                        name = '', 
                                        side = 'both', 
                                        description = '', 
                                        author = '', 
                                        website = '', 
                                        donate = '', 
                                        public = True, 
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        users = [
                                            kleister.models.user_mod.User Mod(
                                                user_id = '', 
                                                user = kleister.models.user.User(
                                                    id = '', 
                                                    username = '', 
                                                    password = '', 
                                                    email = '', 
                                                    fullname = '', 
                                                    profile = '', 
                                                    admin = True, 
                                                    active = True, 
                                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                    auths = [
                                                        kleister.models.user_auth.User Auth(
                                                            provider = '', 
                                                            ref = '', 
                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                        ], 
                                                    teams = [
                                                        kleister.models.user_team.User Team(
                                                            user_id = '', 
                                                            team_id = '', 
                                                            team = kleister.models.team.Team(
                                                                id = '', 
                                                                slug = '', 
                                                                name = '', 
                                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                packs = [
                                                                    kleister.models.team_pack.Team Pack(
                                                                        team_id = '', 
                                                                        pack_id = '', 
                                                                        perm = 'team', 
                                                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                                    ], 
                                                                mods = [
                                                                    kleister.models.team_mod.Team Mod(
                                                                        team_id = '', 
                                                                        mod_id = '', 
                                                                        perm = 'team', 
                                                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                                    ], ), 
                                                            perm = 'user', 
                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                        ], 
                                                    packs = [
                                                        kleister.models.user_pack.User Pack(
                                                            user_id = '', 
                                                            pack_id = '', 
                                                            perm = 'user', 
                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                        ], 
                                                    mods = [
                                                        kleister.models.user_mod.User Mod(
                                                            user_id = '', 
                                                            mod_id = '', 
                                                            perm = 'user', 
                                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                                        ], ), 
                                                mod_id = '', 
                                                perm = 'user', 
                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                            ], 
                                        teams = [
                                            kleister.models.team_mod.Team Mod(
                                                team_id = '', 
                                                mod_id = '', 
                                                perm = 'team', 
                                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                            ], ), 
                                    slug = '', 
                                    name = '', 
                                    public = True, 
                                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    builds = [
                                        kleister.models.build_version.Build Version(
                                            build_id = '', 
                                            version_id = '', 
                                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                        ], ), 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], ), 
                    latest_id = '', 
                    latest = , 
                    slug = '', 
                    name = '', 
                    website = '', 
                    public = True, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    builds = [
                        
                        ], 
                    users = [
                        kleister.models.user_pack.User Pack(
                            user_id = '', 
                            pack_id = '', 
                            perm = 'user', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    teams = [
                        kleister.models.team_pack.Team Pack(
                            team_id = '', 
                            pack_id = '', 
                            perm = 'team', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], ),
                perm = 'user',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return UserPack(
                user_id = '',
                pack_id = '',
        )
        """

    def testUserPack(self):
        """Test UserPack"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
