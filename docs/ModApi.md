# kleister.ModApi

All URIs are relative to *https://try.kleister.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_mod_to_team**](ModApi.md#attach_mod_to_team) | **POST** /mods/{mod_id}/teams | Attach a team to mod
[**attach_mod_to_user**](ModApi.md#attach_mod_to_user) | **POST** /mods/{mod_id}/users | Attach a user to mod
[**attach_version_to_build**](ModApi.md#attach_version_to_build) | **POST** /mods/{mod_id}/versions/{version_id}/builds | Attach a build to a version
[**create_mod**](ModApi.md#create_mod) | **POST** /mods | Create a new mod
[**create_version**](ModApi.md#create_version) | **POST** /mods/{mod_id}/versions | Create a new version for a mod
[**delete_mod**](ModApi.md#delete_mod) | **DELETE** /mods/{mod_id} | Delete a specific mod
[**delete_mod_from_team**](ModApi.md#delete_mod_from_team) | **DELETE** /mods/{mod_id}/teams | Unlink a team from mod
[**delete_mod_from_user**](ModApi.md#delete_mod_from_user) | **DELETE** /mods/{mod_id}/users | Unlink a user from mod
[**delete_version**](ModApi.md#delete_version) | **DELETE** /mods/{mod_id}/versions/{version_id} | Delete a specific version for a mod
[**delete_version_from_build**](ModApi.md#delete_version_from_build) | **DELETE** /mods/{mod_id}/versions/{version_id}/builds | Unlink a build from a version
[**list_mod_teams**](ModApi.md#list_mod_teams) | **GET** /mods/{mod_id}/teams | Fetch all teams attached to mod
[**list_mod_users**](ModApi.md#list_mod_users) | **GET** /mods/{mod_id}/users | Fetch all users attached to mod
[**list_mods**](ModApi.md#list_mods) | **GET** /mods | Fetch all available mods
[**list_version_builds**](ModApi.md#list_version_builds) | **GET** /mods/{mod_id}/versions/{version_id}/builds | Fetch all builds attached to version
[**list_versions**](ModApi.md#list_versions) | **GET** /mods/{mod_id}/versions | Fetch all available versions for a mod
[**permit_mod_team**](ModApi.md#permit_mod_team) | **PUT** /mods/{mod_id}/teams | Update team perms for mod
[**permit_mod_user**](ModApi.md#permit_mod_user) | **PUT** /mods/{mod_id}/users | Update user perms for mod
[**show_mod**](ModApi.md#show_mod) | **GET** /mods/{mod_id} | Fetch a specific mod
[**show_version**](ModApi.md#show_version) | **GET** /mods/{mod_id}/versions/{version_id} | Fetch a specific version for a mod
[**update_mod**](ModApi.md#update_mod) | **PUT** /mods/{mod_id} | Update a specific mod
[**update_version**](ModApi.md#update_version) | **PUT** /mods/{mod_id}/versions/{version_id} | Update a specific version for a mod


# **attach_mod_to_team**
> Notification attach_mod_to_team(mod_id, mod_team_params)

Attach a team to mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mod_team_params import ModTeamParams
from kleister.models.notification import Notification
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    mod_team_params = kleister.ModTeamParams() # ModTeamParams | The team data to attach

    try:
        # Attach a team to mod
        api_response = api_instance.attach_mod_to_team(mod_id, mod_team_params)
        print("The response of ModApi->attach_mod_to_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->attach_mod_to_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **mod_team_params** | [**ModTeamParams**](ModTeamParams.md)| The team data to attach | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Mod or team not found |  -  |
**412** | Team is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_mod_to_user**
> Notification attach_mod_to_user(mod_id, mod_user_params)

Attach a user to mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mod_user_params import ModUserParams
from kleister.models.notification import Notification
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    mod_user_params = kleister.ModUserParams() # ModUserParams | The user data to attach

    try:
        # Attach a user to mod
        api_response = api_instance.attach_mod_to_user(mod_id, mod_user_params)
        print("The response of ModApi->attach_mod_to_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->attach_mod_to_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **mod_user_params** | [**ModUserParams**](ModUserParams.md)| The user data to attach | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Mod or user not found |  -  |
**412** | User is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_version_to_build**
> Notification attach_version_to_build(mod_id, version_id, version_build_params)

Attach a build to a version

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.version_build_params import VersionBuildParams
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    version_id = 'version_id_example' # str | A version identifier or slug
    version_build_params = kleister.VersionBuildParams() # VersionBuildParams | The version build data to attach

    try:
        # Attach a build to a version
        api_response = api_instance.attach_version_to_build(mod_id, version_id, version_build_params)
        print("The response of ModApi->attach_version_to_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->attach_version_to_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **version_id** | **str**| A version identifier or slug | 
 **version_build_params** | [**VersionBuildParams**](VersionBuildParams.md)| The version build data to attach | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Build, version or mod not found |  -  |
**412** | Build is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mod**
> User create_mod(mod)

Create a new mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mod import Mod
from kleister.models.user import User
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod = kleister.Mod() # Mod | The mod data to create

    try:
        # Create a new mod
        api_response = api_instance.create_mod(mod)
        print("The response of ModApi->create_mod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->create_mod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod** | [**Mod**](Mod.md)| The mod data to create | 

### Return type

[**User**](User.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created user data |  -  |
**403** | User is not authorized |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_version**
> Version create_version(mod_id, version)

Create a new version for a mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.version import Version
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    version = kleister.Version() # Version | The version data to create

    try:
        # Create a new version for a mod
        api_response = api_instance.create_version(mod_id, version)
        print("The response of ModApi->create_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->create_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **version** | [**Version**](Version.md)| The version data to create | 

### Return type

[**Version**](Version.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created version data |  -  |
**403** | User is not authorized |  -  |
**404** | Mod not found |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mod**
> Notification delete_mod(mod_id)

Delete a specific mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug

    try:
        # Delete a specific mod
        api_response = api_instance.delete_mod(mod_id)
        print("The response of ModApi->delete_mod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->delete_mod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Mod not found |  -  |
**400** | Failed to delete the mod |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mod_from_team**
> Notification delete_mod_from_team(mod_id, mod_team_params)

Unlink a team from mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mod_team_params import ModTeamParams
from kleister.models.notification import Notification
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    mod_team_params = kleister.ModTeamParams() # ModTeamParams | The mod team data to unlink

    try:
        # Unlink a team from mod
        api_response = api_instance.delete_mod_from_team(mod_id, mod_team_params)
        print("The response of ModApi->delete_mod_from_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->delete_mod_from_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **mod_team_params** | [**ModTeamParams**](ModTeamParams.md)| The mod team data to unlink | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Mod or team not found |  -  |
**412** | Team is not attached |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mod_from_user**
> Notification delete_mod_from_user(mod_id, mod_user_params)

Unlink a user from mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mod_user_params import ModUserParams
from kleister.models.notification import Notification
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    mod_user_params = kleister.ModUserParams() # ModUserParams | The mod user data to unlink

    try:
        # Unlink a user from mod
        api_response = api_instance.delete_mod_from_user(mod_id, mod_user_params)
        print("The response of ModApi->delete_mod_from_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->delete_mod_from_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **mod_user_params** | [**ModUserParams**](ModUserParams.md)| The mod user data to unlink | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Mod or user not found |  -  |
**412** | User is not attached |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> Notification delete_version(mod_id, version_id)

Delete a specific version for a mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    version_id = 'version_id_example' # str | A version identifier or slug

    try:
        # Delete a specific version for a mod
        api_response = api_instance.delete_version(mod_id, version_id)
        print("The response of ModApi->delete_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->delete_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **version_id** | **str**| A version identifier or slug | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Version or mod not found |  -  |
**400** | Failed to delete the version |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version_from_build**
> Notification delete_version_from_build(mod_id, version_id, version_build_params)

Unlink a build from a version

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.version_build_params import VersionBuildParams
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    version_id = 'version_id_example' # str | A version identifier or slug
    version_build_params = kleister.VersionBuildParams() # VersionBuildParams | The version build data to unlink

    try:
        # Unlink a build from a version
        api_response = api_instance.delete_version_from_build(mod_id, version_id, version_build_params)
        print("The response of ModApi->delete_version_from_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->delete_version_from_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **version_id** | **str**| A version identifier or slug | 
 **version_build_params** | [**VersionBuildParams**](VersionBuildParams.md)| The version build data to unlink | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Build, version or mod not found |  -  |
**412** | Build is not attached |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mod_teams**
> ModTeams list_mod_teams(mod_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all teams attached to mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mod_teams import ModTeams
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'name' # str | Sorting column (optional) (default to 'name')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all teams attached to mod
        api_response = api_instance.list_mod_teams(mod_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of ModApi->list_mod_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->list_mod_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;name&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**ModTeams**](ModTeams.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of mod teams |  -  |
**403** | User is not authorized |  -  |
**404** | Mod not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mod_users**
> ModUsers list_mod_users(mod_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all users attached to mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mod_users import ModUsers
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'username' # str | Sorting column (optional) (default to 'username')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all users attached to mod
        api_response = api_instance.list_mod_users(mod_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of ModApi->list_mod_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->list_mod_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;username&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**ModUsers**](ModUsers.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of mod users |  -  |
**403** | User is not authorized |  -  |
**404** | Mod not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mods**
> Mods list_mods(search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all available mods

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mods import Mods
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    search = 'search_example' # str | Search query (optional)
    sort = 'name' # str | Sorting column (optional) (default to 'name')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all available mods
        api_response = api_instance.list_mods(search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of ModApi->list_mods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->list_mods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;name&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**Mods**](Mods.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of mods |  -  |
**403** | User is not authorized |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_version_builds**
> VersionBuilds list_version_builds(mod_id, version_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all builds attached to version

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.version_builds import VersionBuilds
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    version_id = 'version_id_example' # str | A version identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'name' # str | Sorting column (optional) (default to 'name')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all builds attached to version
        api_response = api_instance.list_version_builds(mod_id, version_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of ModApi->list_version_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->list_version_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **version_id** | **str**| A version identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;name&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**VersionBuilds**](VersionBuilds.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of version builds |  -  |
**403** | User is not authorized |  -  |
**404** | Version or mod not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versions**
> Versions list_versions(mod_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all available versions for a mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.versions import Versions
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'name' # str | Sorting column (optional) (default to 'name')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all available versions for a mod
        api_response = api_instance.list_versions(mod_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of ModApi->list_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->list_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;name&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**Versions**](Versions.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of versions |  -  |
**403** | User is not authorized |  -  |
**404** | Mod not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_mod_team**
> Notification permit_mod_team(mod_id, mod_team_params)

Update team perms for mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mod_team_params import ModTeamParams
from kleister.models.notification import Notification
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    mod_team_params = kleister.ModTeamParams() # ModTeamParams | The team data to update

    try:
        # Update team perms for mod
        api_response = api_instance.permit_mod_team(mod_id, mod_team_params)
        print("The response of ModApi->permit_mod_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->permit_mod_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **mod_team_params** | [**ModTeamParams**](ModTeamParams.md)| The team data to update | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Mod or team not found |  -  |
**412** | Team is not attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_mod_user**
> Notification permit_mod_user(mod_id, mod_user_params)

Update user perms for mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mod_user_params import ModUserParams
from kleister.models.notification import Notification
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    mod_user_params = kleister.ModUserParams() # ModUserParams | The user data to update

    try:
        # Update user perms for mod
        api_response = api_instance.permit_mod_user(mod_id, mod_user_params)
        print("The response of ModApi->permit_mod_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->permit_mod_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **mod_user_params** | [**ModUserParams**](ModUserParams.md)| The user data to update | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Mod or user not found |  -  |
**412** | User is not attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_mod**
> Mod show_mod(mod_id)

Fetch a specific mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mod import Mod
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug

    try:
        # Fetch a specific mod
        api_response = api_instance.show_mod(mod_id)
        print("The response of ModApi->show_mod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->show_mod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 

### Return type

[**Mod**](Mod.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetched mod details |  -  |
**403** | User is not authorized |  -  |
**404** | Mod not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_version**
> Version show_version(mod_id, version_id)

Fetch a specific version for a mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.version import Version
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    version_id = 'version_id_example' # str | A version identifier or slug

    try:
        # Fetch a specific version for a mod
        api_response = api_instance.show_version(mod_id, version_id)
        print("The response of ModApi->show_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->show_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **version_id** | **str**| A version identifier or slug | 

### Return type

[**Version**](Version.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetched version details |  -  |
**403** | User is not authorized |  -  |
**404** | Version or mod not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mod**
> Mod update_mod(mod_id, mod)

Update a specific mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.mod import Mod
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    mod = kleister.Mod() # Mod | The mod data to update

    try:
        # Update a specific mod
        api_response = api_instance.update_mod(mod_id, mod)
        print("The response of ModApi->update_mod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->update_mod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **mod** | [**Mod**](Mod.md)| The mod data to update | 

### Return type

[**Mod**](Mod.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated mod details |  -  |
**403** | User is not authorized |  -  |
**404** | Mod not found |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> Version update_version(mod_id, version_id, version)

Update a specific version for a mod

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.version import Version
from kleister.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://try.kleister.eu/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "https://try.kleister.eu/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Cookie
configuration.api_key['Cookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookie'] = 'Bearer'

# Configure HTTP basic authorization: Basic
configuration = kleister.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: Header
configuration.api_key['Header'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Header'] = 'Bearer'

# Configure Bearer authorization: Bearer
configuration = kleister.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with kleister.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kleister.ModApi(api_client)
    mod_id = 'mod_id_example' # str | A mod identifier or slug
    version_id = 'version_id_example' # str | A version identifier or slug
    version = kleister.Version() # Version | The version data to update

    try:
        # Update a specific version for a mod
        api_response = api_instance.update_version(mod_id, version_id, version)
        print("The response of ModApi->update_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModApi->update_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod identifier or slug | 
 **version_id** | **str**| A version identifier or slug | 
 **version** | [**Version**](Version.md)| The version data to update | 

### Return type

[**Version**](Version.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated version details |  -  |
**403** | User is not authorized |  -  |
**404** | Version or mod not found |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

