# kleister.PackApi

All URIs are relative to *https://try.kleister.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_build_to_version**](PackApi.md#attach_build_to_version) | **POST** /packs/{pack_id}/builds/{build_id}/versions | Attach a version to a build
[**attach_pack_to_team**](PackApi.md#attach_pack_to_team) | **POST** /packs/{pack_id}/teams | Attach a team to pack
[**attach_pack_to_user**](PackApi.md#attach_pack_to_user) | **POST** /packs/{pack_id}/users | Attach a user to pack
[**create_build**](PackApi.md#create_build) | **POST** /packs/{pack_id}/builds | Create a new build for a pack
[**create_pack**](PackApi.md#create_pack) | **POST** /packs | Create a new pack
[**delete_build**](PackApi.md#delete_build) | **DELETE** /packs/{pack_id}/builds/{build_id} | Delete a specific build for a pack
[**delete_build_from_version**](PackApi.md#delete_build_from_version) | **DELETE** /packs/{pack_id}/builds/{build_id}/versions | Unlink a version from a build
[**delete_pack**](PackApi.md#delete_pack) | **DELETE** /packs/{pack_id} | Delete a specific pack
[**delete_pack_from_team**](PackApi.md#delete_pack_from_team) | **DELETE** /packs/{pack_id}/teams | Unlink a team from pack
[**delete_pack_from_user**](PackApi.md#delete_pack_from_user) | **DELETE** /packs/{pack_id}/users | Unlink a user from pack
[**list_build_versions**](PackApi.md#list_build_versions) | **GET** /packs/{pack_id}/builds/{build_id}/versions | Fetch all versions attached to build
[**list_builds**](PackApi.md#list_builds) | **GET** /packs/{pack_id}/builds | Fetch all available builds for a pack
[**list_pack_teams**](PackApi.md#list_pack_teams) | **GET** /packs/{pack_id}/teams | Fetch all teams attached to pack
[**list_pack_users**](PackApi.md#list_pack_users) | **GET** /packs/{pack_id}/users | Fetch all users attached to pack
[**list_packs**](PackApi.md#list_packs) | **GET** /packs | Fetch all available packs
[**permit_pack_team**](PackApi.md#permit_pack_team) | **PUT** /packs/{pack_id}/teams | Update team perms for pack
[**permit_pack_user**](PackApi.md#permit_pack_user) | **PUT** /packs/{pack_id}/users | Update user perms for pack
[**show_build**](PackApi.md#show_build) | **GET** /packs/{pack_id}/builds/{build_id} | Fetch a specific build for a pack
[**show_pack**](PackApi.md#show_pack) | **GET** /packs/{pack_id} | Fetch a specific pack
[**update_build**](PackApi.md#update_build) | **PUT** /packs/{pack_id}/builds/{build_id} | Update a specific build for a pack
[**update_pack**](PackApi.md#update_pack) | **PUT** /packs/{pack_id} | Update a specific pack


# **attach_build_to_version**
> Notification attach_build_to_version(pack_id, build_id, build_version_params)

Attach a version to a build

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.build_version_params import BuildVersionParams
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    build_id = 'build_id_example' # str | A build identifier or slug
    build_version_params = kleister.BuildVersionParams() # BuildVersionParams | The build version data to attach

    try:
        # Attach a version to a build
        api_response = api_instance.attach_build_to_version(pack_id, build_id, build_version_params)
        print("The response of PackApi->attach_build_to_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->attach_build_to_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **build_id** | **str**| A build identifier or slug | 
 **build_version_params** | [**BuildVersionParams**](BuildVersionParams.md)| The build version data to attach | 

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
**404** | Version, build or pack not found |  -  |
**412** | Version is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_pack_to_team**
> Notification attach_pack_to_team(pack_id, pack_team_params)

Attach a team to pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.pack_team_params import PackTeamParams
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    pack_team_params = kleister.PackTeamParams() # PackTeamParams | The team data to attach

    try:
        # Attach a team to pack
        api_response = api_instance.attach_pack_to_team(pack_id, pack_team_params)
        print("The response of PackApi->attach_pack_to_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->attach_pack_to_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **pack_team_params** | [**PackTeamParams**](PackTeamParams.md)| The team data to attach | 

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
**404** | Pack or team not found |  -  |
**412** | Team is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_pack_to_user**
> Notification attach_pack_to_user(pack_id, pack_user_params)

Attach a user to pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.pack_user_params import PackUserParams
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    pack_user_params = kleister.PackUserParams() # PackUserParams | The user data to attach

    try:
        # Attach a user to pack
        api_response = api_instance.attach_pack_to_user(pack_id, pack_user_params)
        print("The response of PackApi->attach_pack_to_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->attach_pack_to_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **pack_user_params** | [**PackUserParams**](PackUserParams.md)| The user data to attach | 

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
**404** | Pack or user not found |  -  |
**412** | User is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build**
> Build create_build(pack_id, build)

Create a new build for a pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.build import Build
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    build = kleister.Build() # Build | The build data to create

    try:
        # Create a new build for a pack
        api_response = api_instance.create_build(pack_id, build)
        print("The response of PackApi->create_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->create_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **build** | [**Build**](Build.md)| The build data to create | 

### Return type

[**Build**](Build.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created build build |  -  |
**403** | User is not authorized |  -  |
**404** | Pack not found |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pack**
> Pack create_pack(pack)

Create a new pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.pack import Pack
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
    api_instance = kleister.PackApi(api_client)
    pack = kleister.Pack() # Pack | The pack data to create

    try:
        # Create a new pack
        api_response = api_instance.create_pack(pack)
        print("The response of PackApi->create_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->create_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack** | [**Pack**](Pack.md)| The pack data to create | 

### Return type

[**Pack**](Pack.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created pack data |  -  |
**403** | User is not authorized |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build**
> Notification delete_build(pack_id, build_id)

Delete a specific build for a pack

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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    build_id = 'build_id_example' # str | A build identifier or slug

    try:
        # Delete a specific build for a pack
        api_response = api_instance.delete_build(pack_id, build_id)
        print("The response of PackApi->delete_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->delete_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **build_id** | **str**| A build identifier or slug | 

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
**404** | Build or pack not found |  -  |
**400** | Failed to delete the build |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build_from_version**
> Notification delete_build_from_version(pack_id, build_id, build_version_params)

Unlink a version from a build

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.build_version_params import BuildVersionParams
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    build_id = 'build_id_example' # str | A build identifier or slug
    build_version_params = kleister.BuildVersionParams() # BuildVersionParams | The build version data to unlink

    try:
        # Unlink a version from a build
        api_response = api_instance.delete_build_from_version(pack_id, build_id, build_version_params)
        print("The response of PackApi->delete_build_from_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->delete_build_from_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **build_id** | **str**| A build identifier or slug | 
 **build_version_params** | [**BuildVersionParams**](BuildVersionParams.md)| The build version data to unlink | 

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
**404** | Version, build or pack not found |  -  |
**412** | Version is not attached |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pack**
> Notification delete_pack(pack_id)

Delete a specific pack

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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug

    try:
        # Delete a specific pack
        api_response = api_instance.delete_pack(pack_id)
        print("The response of PackApi->delete_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->delete_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 

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
**404** | Pack not found |  -  |
**400** | Failed to delete the pack |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pack_from_team**
> Notification delete_pack_from_team(pack_id, pack_team_params)

Unlink a team from pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.pack_team_params import PackTeamParams
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    pack_team_params = kleister.PackTeamParams() # PackTeamParams | The pack team data to unlink

    try:
        # Unlink a team from pack
        api_response = api_instance.delete_pack_from_team(pack_id, pack_team_params)
        print("The response of PackApi->delete_pack_from_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->delete_pack_from_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **pack_team_params** | [**PackTeamParams**](PackTeamParams.md)| The pack team data to unlink | 

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
**404** | Pack or team not found |  -  |
**412** | Team is not attached |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pack_from_user**
> Notification delete_pack_from_user(pack_id, pack_user_params)

Unlink a user from pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.pack_user_params import PackUserParams
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    pack_user_params = kleister.PackUserParams() # PackUserParams | The pack user data to unlink

    try:
        # Unlink a user from pack
        api_response = api_instance.delete_pack_from_user(pack_id, pack_user_params)
        print("The response of PackApi->delete_pack_from_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->delete_pack_from_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **pack_user_params** | [**PackUserParams**](PackUserParams.md)| The pack user data to unlink | 

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
**404** | Pack or user not found |  -  |
**412** | User is not attached |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_build_versions**
> BuildVersions list_build_versions(pack_id, build_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all versions attached to build

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.build_versions import BuildVersions
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    build_id = 'build_id_example' # str | A build identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'name' # str | Sorting column (optional) (default to 'name')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 56 # int | Paging limit (optional)
    offset = 56 # int | Paging offset (optional)

    try:
        # Fetch all versions attached to build
        api_response = api_instance.list_build_versions(pack_id, build_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of PackApi->list_build_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->list_build_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **build_id** | **str**| A build identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;name&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] 
 **offset** | **int**| Paging offset | [optional] 

### Return type

[**BuildVersions**](BuildVersions.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of build versions |  -  |
**403** | User is not authorized |  -  |
**404** | Build or pack not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_builds**
> Builds list_builds(pack_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all available builds for a pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.builds import Builds
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'name' # str | Sorting column (optional) (default to 'name')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 56 # int | Paging limit (optional)
    offset = 56 # int | Paging offset (optional)

    try:
        # Fetch all available builds for a pack
        api_response = api_instance.list_builds(pack_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of PackApi->list_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->list_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;name&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] 
 **offset** | **int**| Paging offset | [optional] 

### Return type

[**Builds**](Builds.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of builds |  -  |
**403** | User is not authorized |  -  |
**404** | Pack not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pack_teams**
> PackTeams list_pack_teams(pack_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all teams attached to pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.pack_teams import PackTeams
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'name' # str | Sorting column (optional) (default to 'name')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all teams attached to pack
        api_response = api_instance.list_pack_teams(pack_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of PackApi->list_pack_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->list_pack_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;name&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**PackTeams**](PackTeams.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of pack teams |  -  |
**403** | User is not authorized |  -  |
**404** | Pack not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pack_users**
> PackUsers list_pack_users(pack_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all users attached to pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.pack_users import PackUsers
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'username' # str | Sorting column (optional) (default to 'username')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all users attached to pack
        api_response = api_instance.list_pack_users(pack_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of PackApi->list_pack_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->list_pack_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;username&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**PackUsers**](PackUsers.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of pack users |  -  |
**403** | User is not authorized |  -  |
**404** | Pack not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packs**
> Packs list_packs(search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all available packs

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.packs import Packs
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
    api_instance = kleister.PackApi(api_client)
    search = 'search_example' # str | Search query (optional)
    sort = 'name' # str | Sorting column (optional) (default to 'name')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all available packs
        api_response = api_instance.list_packs(search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of PackApi->list_packs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->list_packs: %s\n" % e)
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

[**Packs**](Packs.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of packs |  -  |
**403** | User is not authorized |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_pack_team**
> Notification permit_pack_team(pack_id, pack_team_params)

Update team perms for pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.pack_team_params import PackTeamParams
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    pack_team_params = kleister.PackTeamParams() # PackTeamParams | The team data to update

    try:
        # Update team perms for pack
        api_response = api_instance.permit_pack_team(pack_id, pack_team_params)
        print("The response of PackApi->permit_pack_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->permit_pack_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **pack_team_params** | [**PackTeamParams**](PackTeamParams.md)| The team data to update | 

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
**404** | Pack or team not found |  -  |
**412** | Team is not attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_pack_user**
> Notification permit_pack_user(pack_id, pack_user_params)

Update user perms for pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.pack_user_params import PackUserParams
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    pack_user_params = kleister.PackUserParams() # PackUserParams | The user data to update

    try:
        # Update user perms for pack
        api_response = api_instance.permit_pack_user(pack_id, pack_user_params)
        print("The response of PackApi->permit_pack_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->permit_pack_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **pack_user_params** | [**PackUserParams**](PackUserParams.md)| The user data to update | 

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
**404** | Pack or user not found |  -  |
**412** | User is not attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_build**
> Build show_build(pack_id, build_id)

Fetch a specific build for a pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.build import Build
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    build_id = 'build_id_example' # str | A build identifier or slug

    try:
        # Fetch a specific build for a pack
        api_response = api_instance.show_build(pack_id, build_id)
        print("The response of PackApi->show_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->show_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **build_id** | **str**| A build identifier or slug | 

### Return type

[**Build**](Build.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetched build details |  -  |
**403** | User is not authorized |  -  |
**404** | Build or pack not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_pack**
> Pack show_pack(pack_id)

Fetch a specific pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.pack import Pack
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug

    try:
        # Fetch a specific pack
        api_response = api_instance.show_pack(pack_id)
        print("The response of PackApi->show_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->show_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 

### Return type

[**Pack**](Pack.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetched pack details |  -  |
**403** | User is not authorized |  -  |
**404** | Pack not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_build**
> Build update_build(pack_id, build_id, build)

Update a specific build for a pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.build import Build
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    build_id = 'build_id_example' # str | A build identifier or slug
    build = kleister.Build() # Build | The build data to update

    try:
        # Update a specific build for a pack
        api_response = api_instance.update_build(pack_id, build_id, build)
        print("The response of PackApi->update_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->update_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **build_id** | **str**| A build identifier or slug | 
 **build** | [**Build**](Build.md)| The build data to update | 

### Return type

[**Build**](Build.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated build details |  -  |
**403** | User is not authorized |  -  |
**404** | Build or pack not found |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pack**
> Pack update_pack(pack_id, pack)

Update a specific pack

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.pack import Pack
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
    api_instance = kleister.PackApi(api_client)
    pack_id = 'pack_id_example' # str | A pack identifier or slug
    pack = kleister.Pack() # Pack | The pack data to update

    try:
        # Update a specific pack
        api_response = api_instance.update_pack(pack_id, pack)
        print("The response of PackApi->update_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackApi->update_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack identifier or slug | 
 **pack** | [**Pack**](Pack.md)| The pack data to update | 

### Return type

[**Pack**](Pack.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated pack details |  -  |
**403** | User is not authorized |  -  |
**404** | Pack not found |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

