# kleister.PackApi

All URIs are relative to *http://try.kleister.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_build_to_version**](PackApi.md#append_build_to_version) | **POST** /packs/{pack_id}/builds/{build_id}/versions | Assign a version to a build
[**append_pack_to_team**](PackApi.md#append_pack_to_team) | **POST** /packs/{pack_id}/teams | Assign a team to pack
[**append_pack_to_user**](PackApi.md#append_pack_to_user) | **POST** /packs/{pack_id}/users | Assign a user to pack
[**create_build**](PackApi.md#create_build) | **POST** /packs/{pack_id}/builds | Create a new build for a pack
[**create_pack**](PackApi.md#create_pack) | **POST** /packs | Create a new pack
[**delete_build**](PackApi.md#delete_build) | **DELETE** /packs/{pack_id}/builds/{build_id} | Delete a specific build for a pack
[**delete_build_from_version**](PackApi.md#delete_build_from_version) | **DELETE** /packs/{pack_id}/builds/{build_id}/versions | Unlink a version from a build
[**delete_pack**](PackApi.md#delete_pack) | **DELETE** /packs/{pack_id} | Delete a specific pack
[**delete_pack_from_team**](PackApi.md#delete_pack_from_team) | **DELETE** /packs/{pack_id}/teams | Remove a team from pack
[**delete_pack_from_user**](PackApi.md#delete_pack_from_user) | **DELETE** /packs/{pack_id}/users | Remove a user from pack
[**list_build_versions**](PackApi.md#list_build_versions) | **GET** /packs/{pack_id}/builds/{build_id}/versions | Fetch all versions assigned to build
[**list_builds**](PackApi.md#list_builds) | **GET** /packs/{pack_id}/builds | Fetch all available builds for a pack
[**list_pack_teams**](PackApi.md#list_pack_teams) | **GET** /packs/{pack_id}/teams | Fetch all teams assigned to pack
[**list_pack_users**](PackApi.md#list_pack_users) | **GET** /packs/{pack_id}/users | Fetch all users assigned to pack
[**list_packs**](PackApi.md#list_packs) | **GET** /packs | Fetch all available packs
[**permit_pack_team**](PackApi.md#permit_pack_team) | **PUT** /packs/{pack_id}/teams | Update team perms for pack
[**permit_pack_user**](PackApi.md#permit_pack_user) | **PUT** /packs/{pack_id}/users | Update user perms for pack
[**show_build**](PackApi.md#show_build) | **GET** /packs/{pack_id}/builds/{build_id} | Fetch a specific build for a pack
[**show_pack**](PackApi.md#show_pack) | **GET** /packs/{pack_id} | Fetch a specific pack
[**update_build**](PackApi.md#update_build) | **PUT** /packs/{pack_id}/builds/{build_id} | Update a specific build for a pack
[**update_pack**](PackApi.md#update_pack) | **PUT** /packs/{pack_id} | Update a specific pack


# **append_build_to_version**
> GeneralError append_build_to_version(pack_id, build_id, build_version)

Assign a version to a build

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.build_version_params import BuildVersionParams
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
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    build_id = "build_id_example" # str | A build UUID or slug
    build_version = BuildVersionParams(
        mod="mod_example",
        version="version_example",
    ) # BuildVersionParams | The version data to append to build

    # example passing only required values which don't have defaults set
    try:
        # Assign a version to a build
        api_response = api_instance.append_build_to_version(pack_id, build_id, build_version)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->append_build_to_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **build_id** | **str**| A build UUID or slug |
 **build_version** | [**BuildVersionParams**](BuildVersionParams.md)| The version data to append to build |

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
**422** | Version is already appended |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_pack_to_team**
> GeneralError append_pack_to_team(pack_id, pack_team)

Assign a team to pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.pack_team_params import PackTeamParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    pack_team = PackTeamParams(
        team="team_example",
        perm="user",
    ) # PackTeamParams | The pack team data to assign

    # example passing only required values which don't have defaults set
    try:
        # Assign a team to pack
        api_response = api_instance.append_pack_to_team(pack_id, pack_team)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->append_pack_to_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **pack_team** | [**PackTeamParams**](PackTeamParams.md)| The pack team data to assign |

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

# **append_pack_to_user**
> GeneralError append_pack_to_user(pack_id, pack_user)

Assign a user to pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.pack_user_params import PackUserParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    pack_user = PackUserParams(
        user="user_example",
        perm="user",
    ) # PackUserParams | The pack user data to assign

    # example passing only required values which don't have defaults set
    try:
        # Assign a user to pack
        api_response = api_instance.append_pack_to_user(pack_id, pack_user)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->append_pack_to_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **pack_user** | [**PackUserParams**](PackUserParams.md)| The pack user data to assign |

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

# **create_build**
> Build create_build(pack_id, build)

Create a new build for a pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.build import Build
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
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    build = Build(
        pack_id="pack_id_example",
        minecraft_id="minecraft_id_example",
        forge_id="forge_id_example",
        slug="slug_example",
        name="name_example",
        min_java="min_java_example",
        min_memory="min_memory_example",
        published=True,
        hidden=True,
        private=True,
        public=True,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Build | The build data to create

    # example passing only required values which don't have defaults set
    try:
        # Create a new build for a pack
        api_response = api_instance.create_build(pack_id, build)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->create_build: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **build** | [**Build**](Build.md)| The build data to create |

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created build data |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pack**
> Pack create_pack(pack)

Create a new pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.pack import Pack
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
    api_instance = pack_api.PackApi(api_client)
    pack = Pack(
        recommended_id="recommended_id_example",
        latest_id="latest_id_example",
        slug="slug_example",
        name="name_example",
        website="website_example",
        published=True,
        hidden=True,
        private=True,
        public=True,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Pack | The pack data to create

    # example passing only required values which don't have defaults set
    try:
        # Create a new pack
        api_response = api_instance.create_pack(pack)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->create_pack: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack** | [**Pack**](Pack.md)| The pack data to create |

### Return type

[**Pack**](Pack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created pack data |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build**
> GeneralError delete_build(pack_id, build_id)

Delete a specific build for a pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
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
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    build_id = "build_id_example" # str | A build UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Delete a specific build for a pack
        api_response = api_instance.delete_build(pack_id, build_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->delete_build: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **build_id** | **str**| A build UUID or slug |

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
**400** | Failed to delete the build |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build_from_version**
> GeneralError delete_build_from_version(pack_id, build_id, build_version)

Unlink a version from a build

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.build_version_params import BuildVersionParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    build_id = "build_id_example" # str | A build UUID or slug
    build_version = BuildVersionParams(
        mod="mod_example",
        version="version_example",
    ) # BuildVersionParams | The version data to unlink from build

    # example passing only required values which don't have defaults set
    try:
        # Unlink a version from a build
        api_response = api_instance.delete_build_from_version(pack_id, build_id, build_version)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->delete_build_from_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **build_id** | **str**| A build UUID or slug |
 **build_version** | [**BuildVersionParams**](BuildVersionParams.md)| The version data to unlink from build |

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
**400** | Failed to unlink version |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pack**
> GeneralError delete_pack(pack_id)

Delete a specific pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
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
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Delete a specific pack
        api_response = api_instance.delete_pack(pack_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->delete_pack: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |

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
**400** | Failed to delete the pack |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pack_from_team**
> GeneralError delete_pack_from_team(pack_id, pack_team)

Remove a team from pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.pack_team_params import PackTeamParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    pack_team = PackTeamParams(
        team="team_example",
        perm="user",
    ) # PackTeamParams | The pack team data to delete

    # example passing only required values which don't have defaults set
    try:
        # Remove a team from pack
        api_response = api_instance.delete_pack_from_team(pack_id, pack_team)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->delete_pack_from_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **pack_team** | [**PackTeamParams**](PackTeamParams.md)| The pack team data to delete |

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

# **delete_pack_from_user**
> GeneralError delete_pack_from_user(pack_id, pack_user)

Remove a user from pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.pack_user_params import PackUserParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    pack_user = PackUserParams(
        user="user_example",
        perm="user",
    ) # PackUserParams | The pack user data to delete

    # example passing only required values which don't have defaults set
    try:
        # Remove a user from pack
        api_response = api_instance.delete_pack_from_user(pack_id, pack_user)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->delete_pack_from_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **pack_user** | [**PackUserParams**](PackUserParams.md)| The pack user data to delete |

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

# **list_build_versions**
> [BuildVersion] list_build_versions(pack_id, build_id)

Fetch all versions assigned to build

### Example


```python
import time
import kleister
from kleister.api import pack_api
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
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    build_id = "build_id_example" # str | A build UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all versions assigned to build
        api_response = api_instance.list_build_versions(pack_id, build_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->list_build_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **build_id** | **str**| A build UUID or slug |

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
**200** | A collection of build versions |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_builds**
> [Build] list_builds(pack_id)

Fetch all available builds for a pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.build import Build
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all available builds for a pack
        api_response = api_instance.list_builds(pack_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->list_builds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |

### Return type

[**[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of builds |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pack_teams**
> [TeamPack] list_pack_teams(pack_id)

Fetch all teams assigned to pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.team_pack import TeamPack
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all teams assigned to pack
        api_response = api_instance.list_pack_teams(pack_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->list_pack_teams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |

### Return type

[**[TeamPack]**](TeamPack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of pack teams |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pack_users**
> [UserPack] list_pack_users(pack_id)

Fetch all users assigned to pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.user_pack import UserPack
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all users assigned to pack
        api_response = api_instance.list_pack_users(pack_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->list_pack_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |

### Return type

[**[UserPack]**](UserPack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of pack users |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packs**
> [Pack] list_packs()

Fetch all available packs

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.pack import Pack
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all available packs
        api_response = api_instance.list_packs()
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->list_packs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Pack]**](Pack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of packs |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_pack_team**
> GeneralError permit_pack_team(pack_id, pack_team)

Update team perms for pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.pack_team_params import PackTeamParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    pack_team = PackTeamParams(
        team="team_example",
        perm="user",
    ) # PackTeamParams | The pack team data to update

    # example passing only required values which don't have defaults set
    try:
        # Update team perms for pack
        api_response = api_instance.permit_pack_team(pack_id, pack_team)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->permit_pack_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **pack_team** | [**PackTeamParams**](PackTeamParams.md)| The pack team data to update |

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

# **permit_pack_user**
> GeneralError permit_pack_user(pack_id, pack_user)

Update user perms for pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.pack_user_params import PackUserParams
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    pack_user = PackUserParams(
        user="user_example",
        perm="user",
    ) # PackUserParams | The pack user data to update

    # example passing only required values which don't have defaults set
    try:
        # Update user perms for pack
        api_response = api_instance.permit_pack_user(pack_id, pack_user)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->permit_pack_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **pack_user** | [**PackUserParams**](PackUserParams.md)| The pack user data to update |

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

# **show_build**
> Build show_build(pack_id, build_id)

Fetch a specific build for a pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.build import Build
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    build_id = "build_id_example" # str | A build UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch a specific build for a pack
        api_response = api_instance.show_build(pack_id, build_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->show_build: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **build_id** | **str**| A build UUID or slug |

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetched build details |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_pack**
> Pack show_pack(pack_id)

Fetch a specific pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.pack import Pack
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch a specific pack
        api_response = api_instance.show_pack(pack_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->show_pack: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |

### Return type

[**Pack**](Pack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetched pack details |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_build**
> Build update_build(pack_id, build_id, build)

Update a specific build for a pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.build import Build
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
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    build_id = "build_id_example" # str | A build UUID or slug
    build = Build(
        pack_id="pack_id_example",
        minecraft_id="minecraft_id_example",
        forge_id="forge_id_example",
        slug="slug_example",
        name="name_example",
        min_java="min_java_example",
        min_memory="min_memory_example",
        published=True,
        hidden=True,
        private=True,
        public=True,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Build | The build data to update

    # example passing only required values which don't have defaults set
    try:
        # Update a specific build for a pack
        api_response = api_instance.update_build(pack_id, build_id, build)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->update_build: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **build_id** | **str**| A build UUID or slug |
 **build** | [**Build**](Build.md)| The build data to update |

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated build details |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pack**
> Pack update_pack(pack_id, pack)

Update a specific pack

### Example


```python
import time
import kleister
from kleister.api import pack_api
from kleister.model.general_error import GeneralError
from kleister.model.pack import Pack
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
    api_instance = pack_api.PackApi(api_client)
    pack_id = "pack_id_example" # str | A pack UUID or slug
    pack = Pack(
        recommended_id="recommended_id_example",
        latest_id="latest_id_example",
        slug="slug_example",
        name="name_example",
        website="website_example",
        published=True,
        hidden=True,
        private=True,
        public=True,
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Pack | The pack data to update

    # example passing only required values which don't have defaults set
    try:
        # Update a specific pack
        api_response = api_instance.update_pack(pack_id, pack)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling PackApi->update_pack: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug |
 **pack** | [**Pack**](Pack.md)| The pack data to update |

### Return type

[**Pack**](Pack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated pack details |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

