# kleister.ModApi

All URIs are relative to *http://try.kleister.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_mod_to_team**](ModApi.md#append_mod_to_team) | **POST** /mods/{mod_id}/teams | Assign a team to mod
[**append_mod_to_user**](ModApi.md#append_mod_to_user) | **POST** /mods/{mod_id}/users | Assign a user to mod
[**append_version_to_build**](ModApi.md#append_version_to_build) | **POST** /mods/{mod_id}/versions/{version_id}/builds | Assign a build to a version
[**create_mod**](ModApi.md#create_mod) | **POST** /mods | Create a new mod
[**create_version**](ModApi.md#create_version) | **POST** /mods/{mod_id}/versions | Create a new version for a mod
[**delete_mod**](ModApi.md#delete_mod) | **DELETE** /mods/{mod_id} | Delete a specific mod
[**delete_mod_from_team**](ModApi.md#delete_mod_from_team) | **DELETE** /mods/{mod_id}/teams | Remove a team from mod
[**delete_mod_from_user**](ModApi.md#delete_mod_from_user) | **DELETE** /mods/{mod_id}/users | Remove a user from mod
[**delete_version**](ModApi.md#delete_version) | **DELETE** /mods/{mod_id}/versions/{version_id} | Delete a specific version for a mod
[**delete_version_from_build**](ModApi.md#delete_version_from_build) | **DELETE** /mods/{mod_id}/versions/{version_id}/builds | Unlink a build from a version
[**list_mod_teams**](ModApi.md#list_mod_teams) | **GET** /mods/{mod_id}/teams | Fetch all teams assigned to mod
[**list_mod_users**](ModApi.md#list_mod_users) | **GET** /mods/{mod_id}/users | Fetch all users assigned to mod
[**list_mods**](ModApi.md#list_mods) | **GET** /mods | Fetch all available mods
[**list_version_builds**](ModApi.md#list_version_builds) | **GET** /mods/{mod_id}/versions/{version_id}/builds | Fetch all builds assigned to version
[**list_versions**](ModApi.md#list_versions) | **GET** /mods/{mod_id}/versions | Fetch all available versions for a mod
[**permit_mod_team**](ModApi.md#permit_mod_team) | **PUT** /mods/{mod_id}/teams | Update team perms for mod
[**permit_mod_user**](ModApi.md#permit_mod_user) | **PUT** /mods/{mod_id}/users | Update user perms for mod
[**show_mod**](ModApi.md#show_mod) | **GET** /mods/{mod_id} | Fetch a specific mod
[**show_version**](ModApi.md#show_version) | **GET** /mods/{mod_id}/versions/{version_id} | Fetch a specific version for a mod
[**update_mod**](ModApi.md#update_mod) | **PUT** /mods/{mod_id} | Update a specific mod
[**update_version**](ModApi.md#update_version) | **PUT** /mods/{mod_id}/versions/{version_id} | Update a specific version for a mod


# **append_mod_to_team**
> GeneralError append_mod_to_team(mod_id, mod_team)

Assign a team to mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.mod_team_params import ModTeamParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    mod_team = ModTeamParams(
        team="team_example",
        perm="user",
    ) # ModTeamParams | The mod team data to assign

    # example passing only required values which don't have defaults set
    try:
        # Assign a team to mod
        api_response = api_instance.append_mod_to_team(mod_id, mod_team)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->append_mod_to_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **mod_team** | [**ModTeamParams**](ModTeamParams.md)| The mod team data to assign |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Team is already assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_mod_to_user**
> GeneralError append_mod_to_user(mod_id, mod_user)

Assign a user to mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.mod_user_params import ModUserParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    mod_user = ModUserParams(
        user="user_example",
        perm="user",
    ) # ModUserParams | The mod user data to assign

    # example passing only required values which don't have defaults set
    try:
        # Assign a user to mod
        api_response = api_instance.append_mod_to_user(mod_id, mod_user)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->append_mod_to_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **mod_user** | [**ModUserParams**](ModUserParams.md)| The mod user data to assign |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | User is already assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_version_to_build**
> GeneralError append_version_to_build(mod_id, version_id, version_build)

Assign a build to a version

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.validation_error import ValidationError
from kleister.model.version_build_params import VersionBuildParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    version_id = "version_id_example" # str | A version UUID or slug
    version_build = VersionBuildParams(
        pack="pack_example",
        build="build_example",
    ) # VersionBuildParams | The build data to append to version

    # example passing only required values which don't have defaults set
    try:
        # Assign a build to a version
        api_response = api_instance.append_version_to_build(mod_id, version_id, version_build)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->append_version_to_build: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **version_id** | **str**| A version UUID or slug |
 **version_build** | [**VersionBuildParams**](VersionBuildParams.md)| The build data to append to version |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Build is already appended |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mod**
> Mod create_mod(mod)

Create a new mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.mod import Mod
from kleister.model.validation_error import ValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod = Mod(
        slug="slug_example",
        name="name_example",
        side="both",
        description="description_example",
        author="author_example",
        website="website_example",
        donate="donate_example",
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Mod | The mod data to create

    # example passing only required values which don't have defaults set
    try:
        # Create a new mod
        api_response = api_instance.create_mod(mod)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->create_mod: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod** | [**Mod**](Mod.md)| The mod data to create |

### Return type

[**Mod**](Mod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created mod data |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_version**
> Version create_version(mod_id, version)

Create a new version for a mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.validation_error import ValidationError
from kleister.model.version import Version
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    version = Version(
        mod_id="mod_id_example",
        slug="slug_example",
        name="name_example",
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Version | The version data to create

    # example passing only required values which don't have defaults set
    try:
        # Create a new version for a mod
        api_response = api_instance.create_version(mod_id, version)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->create_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **version** | [**Version**](Version.md)| The version data to create |

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created version data |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mod**
> GeneralError delete_mod(mod_id)

Delete a specific mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Delete a specific mod
        api_response = api_instance.delete_mod(mod_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->delete_mod: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to delete the mod |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mod_from_team**
> GeneralError delete_mod_from_team(mod_id, mod_team)

Remove a team from mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.mod_team_params import ModTeamParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    mod_team = ModTeamParams(
        team="team_example",
        perm="user",
    ) # ModTeamParams | The mod team data to delete

    # example passing only required values which don't have defaults set
    try:
        # Remove a team from mod
        api_response = api_instance.delete_mod_from_team(mod_id, mod_team)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->delete_mod_from_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **mod_team** | [**ModTeamParams**](ModTeamParams.md)| The mod team data to delete |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Team is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mod_from_user**
> GeneralError delete_mod_from_user(mod_id, mod_user)

Remove a user from mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.mod_user_params import ModUserParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    mod_user = ModUserParams(
        user="user_example",
        perm="user",
    ) # ModUserParams | The mod user data to delete

    # example passing only required values which don't have defaults set
    try:
        # Remove a user from mod
        api_response = api_instance.delete_mod_from_user(mod_id, mod_user)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->delete_mod_from_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **mod_user** | [**ModUserParams**](ModUserParams.md)| The mod user data to delete |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | User is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> GeneralError delete_version(mod_id, version_id)

Delete a specific version for a mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    version_id = "version_id_example" # str | A version UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Delete a specific version for a mod
        api_response = api_instance.delete_version(mod_id, version_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->delete_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **version_id** | **str**| A version UUID or slug |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to delete the version |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version_from_build**
> GeneralError delete_version_from_build(mod_id, version_id, version_build)

Unlink a build from a version

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.version_build_params import VersionBuildParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    version_id = "version_id_example" # str | A version UUID or slug
    version_build = VersionBuildParams(
        pack="pack_example",
        build="build_example",
    ) # VersionBuildParams | The build data to unlink from version

    # example passing only required values which don't have defaults set
    try:
        # Unlink a build from a version
        api_response = api_instance.delete_version_from_build(mod_id, version_id, version_build)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->delete_version_from_build: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **version_id** | **str**| A version UUID or slug |
 **version_build** | [**VersionBuildParams**](VersionBuildParams.md)| The build data to unlink from version |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to unlink build |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mod_teams**
> [TeamMod] list_mod_teams(mod_id)

Fetch all teams assigned to mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.team_mod import TeamMod
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all teams assigned to mod
        api_response = api_instance.list_mod_teams(mod_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->list_mod_teams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |

### Return type

[**[TeamMod]**](TeamMod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of mod teams |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mod_users**
> [UserMod] list_mod_users(mod_id)

Fetch all users assigned to mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.user_mod import UserMod
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all users assigned to mod
        api_response = api_instance.list_mod_users(mod_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->list_mod_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |

### Return type

[**[UserMod]**](UserMod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of mod users |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mods**
> [Mod] list_mods()

Fetch all available mods

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.mod import Mod
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all available mods
        api_response = api_instance.list_mods()
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->list_mods: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Mod]**](Mod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of mods |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_version_builds**
> [BuildVersion] list_version_builds(mod_id, version_id)

Fetch all builds assigned to version

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.build_version import BuildVersion
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    version_id = "version_id_example" # str | A version UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all builds assigned to version
        api_response = api_instance.list_version_builds(mod_id, version_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->list_version_builds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **version_id** | **str**| A version UUID or slug |

### Return type

[**[BuildVersion]**](BuildVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of version builds |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versions**
> [Version] list_versions(mod_id)

Fetch all available versions for a mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.version import Version
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all available versions for a mod
        api_response = api_instance.list_versions(mod_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->list_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |

### Return type

[**[Version]**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of versions |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_mod_team**
> GeneralError permit_mod_team(mod_id, mod_team)

Update team perms for mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.mod_team_params import ModTeamParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    mod_team = ModTeamParams(
        team="team_example",
        perm="user",
    ) # ModTeamParams | The mod team data to update

    # example passing only required values which don't have defaults set
    try:
        # Update team perms for mod
        api_response = api_instance.permit_mod_team(mod_id, mod_team)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->permit_mod_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **mod_team** | [**ModTeamParams**](ModTeamParams.md)| The mod team data to update |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Team is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_mod_user**
> GeneralError permit_mod_user(mod_id, mod_user)

Update user perms for mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.mod_user_params import ModUserParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    mod_user = ModUserParams(
        user="user_example",
        perm="user",
    ) # ModUserParams | The mod user data to update

    # example passing only required values which don't have defaults set
    try:
        # Update user perms for mod
        api_response = api_instance.permit_mod_user(mod_id, mod_user)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->permit_mod_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **mod_user** | [**ModUserParams**](ModUserParams.md)| The mod user data to update |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | User is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_mod**
> Mod show_mod(mod_id)

Fetch a specific mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.mod import Mod
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch a specific mod
        api_response = api_instance.show_mod(mod_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->show_mod: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |

### Return type

[**Mod**](Mod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetched mod details |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_version**
> Version show_version(mod_id, version_id)

Fetch a specific version for a mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.version import Version
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    version_id = "version_id_example" # str | A version UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch a specific version for a mod
        api_response = api_instance.show_version(mod_id, version_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->show_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **version_id** | **str**| A version UUID or slug |

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetched version details |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mod**
> Mod update_mod(mod_id, mod)

Update a specific mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.mod import Mod
from kleister.model.validation_error import ValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    mod = Mod(
        slug="slug_example",
        name="name_example",
        side="both",
        description="description_example",
        author="author_example",
        website="website_example",
        donate="donate_example",
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Mod | The mod data to update

    # example passing only required values which don't have defaults set
    try:
        # Update a specific mod
        api_response = api_instance.update_mod(mod_id, mod)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->update_mod: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **mod** | [**Mod**](Mod.md)| The mod data to update |

### Return type

[**Mod**](Mod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated mod details |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> Version update_version(mod_id, version_id, version)

Update a specific version for a mod

### Example


```python
import time
import kleister
from kleister.api import mod_api
from kleister.model.general_error import GeneralError
from kleister.model.validation_error import ValidationError
from kleister.model.version import Version
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mod_api.ModApi(api_client)
    mod_id = "mod_id_example" # str | A mod UUID or slug
    version_id = "version_id_example" # str | A version UUID or slug
    version = Version(
        mod_id="mod_id_example",
        slug="slug_example",
        name="name_example",
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Version | The version data to update

    # example passing only required values which don't have defaults set
    try:
        # Update a specific version for a mod
        api_response = api_instance.update_version(mod_id, version_id, version)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ModApi->update_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug |
 **version_id** | **str**| A version UUID or slug |
 **version** | [**Version**](Version.md)| The version data to update |

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated version details |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

