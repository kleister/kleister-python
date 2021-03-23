# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.auth_api import AuthApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from kleister.api.auth_api import AuthApi
from kleister.api.forge_api import ForgeApi
from kleister.api.minecraft_api import MinecraftApi
from kleister.api.mod_api import ModApi
from kleister.api.pack_api import PackApi
from kleister.api.profile_api import ProfileApi
from kleister.api.team_api import TeamApi
from kleister.api.user_api import UserApi
