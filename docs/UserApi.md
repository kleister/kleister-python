# kleister.UserApi

All URIs are relative to *https://try.kleister.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_user_to_group**](UserApi.md#attach_user_to_group) | **POST** /users/{user_id}/groups | Attach a group to user
[**attach_user_to_mod**](UserApi.md#attach_user_to_mod) | **POST** /users/{user_id}/mods | Attach a mod to user
[**attach_user_to_pack**](UserApi.md#attach_user_to_pack) | **POST** /users/{user_id}/packs | Attach a pack to user
[**create_user**](UserApi.md#create_user) | **POST** /users | Create a new user
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{user_id} | Delete a specific user
[**delete_user_from_group**](UserApi.md#delete_user_from_group) | **DELETE** /users/{user_id}/groups | Unlink a group from user
[**delete_user_from_mod**](UserApi.md#delete_user_from_mod) | **DELETE** /users/{user_id}/mods | Unlink a mod from user
[**delete_user_from_pack**](UserApi.md#delete_user_from_pack) | **DELETE** /users/{user_id}/packs | Unlink a pack from user
[**list_user_groups**](UserApi.md#list_user_groups) | **GET** /users/{user_id}/groups | Fetch all groups attached to user
[**list_user_mods**](UserApi.md#list_user_mods) | **GET** /users/{user_id}/mods | Fetch all mods attached to user
[**list_user_packs**](UserApi.md#list_user_packs) | **GET** /users/{user_id}/packs | Fetch all packs attached to user
[**list_users**](UserApi.md#list_users) | **GET** /users | Fetch all available users
[**permit_user_group**](UserApi.md#permit_user_group) | **PUT** /users/{user_id}/groups | Update group perms for user
[**permit_user_mod**](UserApi.md#permit_user_mod) | **PUT** /users/{user_id}/mods | Update mod perms for user
[**permit_user_pack**](UserApi.md#permit_user_pack) | **PUT** /users/{user_id}/packs | Update pack perms for user
[**show_user**](UserApi.md#show_user) | **GET** /users/{user_id} | Fetch a specific user
[**update_user**](UserApi.md#update_user) | **PUT** /users/{user_id} | Update a specific user


# **attach_user_to_group**
> Notification attach_user_to_group(user_id, permit_pack_group_request)

Attach a group to user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.permit_pack_group_request import PermitPackGroupRequest
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    permit_pack_group_request = kleister.PermitPackGroupRequest() # PermitPackGroupRequest | The user group data to permit

    try:
        # Attach a group to user
        api_response = api_instance.attach_user_to_group(user_id, permit_pack_group_request)
        print("The response of UserApi->attach_user_to_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->attach_user_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **permit_pack_group_request** | [**PermitPackGroupRequest**](PermitPackGroupRequest.md)| The user group data to permit | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_user_to_mod**
> Notification attach_user_to_mod(user_id, permit_group_mod_request)

Attach a mod to user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.permit_group_mod_request import PermitGroupModRequest
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    permit_group_mod_request = kleister.PermitGroupModRequest() # PermitGroupModRequest | The user mod data to permit

    try:
        # Attach a mod to user
        api_response = api_instance.attach_user_to_mod(user_id, permit_group_mod_request)
        print("The response of UserApi->attach_user_to_mod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->attach_user_to_mod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **permit_group_mod_request** | [**PermitGroupModRequest**](PermitGroupModRequest.md)| The user mod data to permit | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_user_to_pack**
> Notification attach_user_to_pack(user_id, permit_group_pack_request)

Attach a pack to user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.permit_group_pack_request import PermitGroupPackRequest
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    permit_group_pack_request = kleister.PermitGroupPackRequest() # PermitGroupPackRequest | The user pack data to permit

    try:
        # Attach a pack to user
        api_response = api_instance.attach_user_to_pack(user_id, permit_group_pack_request)
        print("The response of UserApi->attach_user_to_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->attach_user_to_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **permit_group_pack_request** | [**PermitGroupPackRequest**](PermitGroupPackRequest.md)| The user pack data to permit | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(create_user_request)

Create a new user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.create_user_request import CreateUserRequest
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
    api_instance = kleister.UserApi(api_client)
    create_user_request = kleister.CreateUserRequest() # CreateUserRequest | The user data to create

    try:
        # Create a new user
        api_response = api_instance.create_user(create_user_request)
        print("The response of UserApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)| The user data to create | 

### Return type

[**User**](User.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details for an user |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> Notification delete_user(user_id)

Delete a specific user

### Example

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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug

    try:
        # Delete a specific user
        api_response = api_instance.delete_user(user_id)
        print("The response of UserApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**400** | Failed to execute action for resource |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_group**
> Notification delete_user_from_group(user_id, delete_pack_from_group_request)

Unlink a group from user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.delete_pack_from_group_request import DeletePackFromGroupRequest
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    delete_pack_from_group_request = kleister.DeletePackFromGroupRequest() # DeletePackFromGroupRequest | The user group data to unlink

    try:
        # Unlink a group from user
        api_response = api_instance.delete_user_from_group(user_id, delete_pack_from_group_request)
        print("The response of UserApi->delete_user_from_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_user_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **delete_pack_from_group_request** | [**DeletePackFromGroupRequest**](DeletePackFromGroupRequest.md)| The user group data to unlink | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is not attached |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_mod**
> Notification delete_user_from_mod(user_id, delete_group_from_mod_request)

Unlink a mod from user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.delete_group_from_mod_request import DeleteGroupFromModRequest
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    delete_group_from_mod_request = kleister.DeleteGroupFromModRequest() # DeleteGroupFromModRequest | The user mod data to unlink

    try:
        # Unlink a mod from user
        api_response = api_instance.delete_user_from_mod(user_id, delete_group_from_mod_request)
        print("The response of UserApi->delete_user_from_mod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_user_from_mod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **delete_group_from_mod_request** | [**DeleteGroupFromModRequest**](DeleteGroupFromModRequest.md)| The user mod data to unlink | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is not attached |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_pack**
> Notification delete_user_from_pack(user_id, delete_group_from_pack_request)

Unlink a pack from user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.delete_group_from_pack_request import DeleteGroupFromPackRequest
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    delete_group_from_pack_request = kleister.DeleteGroupFromPackRequest() # DeleteGroupFromPackRequest | The user pack data to unlink

    try:
        # Unlink a pack from user
        api_response = api_instance.delete_user_from_pack(user_id, delete_group_from_pack_request)
        print("The response of UserApi->delete_user_from_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_user_from_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **delete_group_from_pack_request** | [**DeleteGroupFromPackRequest**](DeleteGroupFromPackRequest.md)| The user pack data to unlink | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is not attached |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_groups**
> ListUserGroups200Response list_user_groups(user_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all groups attached to user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.list_user_groups200_response import ListUserGroups200Response
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'sort_example' # str | Sorting column (optional)
    order = asc # str | Sorting order (optional) (default to asc)
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all groups attached to user
        api_response = api_instance.list_user_groups(user_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of UserApi->list_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] 
 **order** | **str**| Sorting order | [optional] [default to asc]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**ListUserGroups200Response**](ListUserGroups200Response.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of user groups |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_mods**
> ListUserMods200Response list_user_mods(user_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all mods attached to user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.list_user_mods200_response import ListUserMods200Response
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'sort_example' # str | Sorting column (optional)
    order = asc # str | Sorting order (optional) (default to asc)
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all mods attached to user
        api_response = api_instance.list_user_mods(user_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of UserApi->list_user_mods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_user_mods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] 
 **order** | **str**| Sorting order | [optional] [default to asc]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**ListUserMods200Response**](ListUserMods200Response.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of user mods |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_packs**
> ListUserPacks200Response list_user_packs(user_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all packs attached to user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.list_user_packs200_response import ListUserPacks200Response
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'sort_example' # str | Sorting column (optional)
    order = asc # str | Sorting order (optional) (default to asc)
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all packs attached to user
        api_response = api_instance.list_user_packs(user_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of UserApi->list_user_packs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_user_packs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] 
 **order** | **str**| Sorting order | [optional] [default to asc]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**ListUserPacks200Response**](ListUserPacks200Response.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of user packs |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsers200Response list_users(search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all available users

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.list_users200_response import ListUsers200Response
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
    api_instance = kleister.UserApi(api_client)
    search = 'search_example' # str | Search query (optional)
    sort = 'sort_example' # str | Sorting column (optional)
    order = asc # str | Sorting order (optional) (default to asc)
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all available users
        api_response = api_instance.list_users(search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of UserApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] 
 **order** | **str**| Sorting order | [optional] [default to asc]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**ListUsers200Response**](ListUsers200Response.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of users |  -  |
**403** | User is not authorized |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_user_group**
> Notification permit_user_group(user_id, permit_pack_group_request)

Update group perms for user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.permit_pack_group_request import PermitPackGroupRequest
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    permit_pack_group_request = kleister.PermitPackGroupRequest() # PermitPackGroupRequest | The user group data to permit

    try:
        # Update group perms for user
        api_response = api_instance.permit_user_group(user_id, permit_pack_group_request)
        print("The response of UserApi->permit_user_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->permit_user_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **permit_pack_group_request** | [**PermitPackGroupRequest**](PermitPackGroupRequest.md)| The user group data to permit | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is not attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_user_mod**
> Notification permit_user_mod(user_id, permit_group_mod_request)

Update mod perms for user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.permit_group_mod_request import PermitGroupModRequest
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    permit_group_mod_request = kleister.PermitGroupModRequest() # PermitGroupModRequest | The user mod data to permit

    try:
        # Update mod perms for user
        api_response = api_instance.permit_user_mod(user_id, permit_group_mod_request)
        print("The response of UserApi->permit_user_mod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->permit_user_mod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **permit_group_mod_request** | [**PermitGroupModRequest**](PermitGroupModRequest.md)| The user mod data to permit | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is not attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_user_pack**
> Notification permit_user_pack(user_id, permit_group_pack_request)

Update pack perms for user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.permit_group_pack_request import PermitGroupPackRequest
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    permit_group_pack_request = kleister.PermitGroupPackRequest() # PermitGroupPackRequest | The user pack data to permit

    try:
        # Update pack perms for user
        api_response = api_instance.permit_user_pack(user_id, permit_group_pack_request)
        print("The response of UserApi->permit_user_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->permit_user_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **permit_group_pack_request** | [**PermitGroupPackRequest**](PermitGroupPackRequest.md)| The user pack data to permit | 

### Return type

[**Notification**](Notification.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**412** | Resource is not attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_user**
> User show_user(user_id)

Fetch a specific user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug

    try:
        # Fetch a specific user
        api_response = api_instance.show_user(user_id)
        print("The response of UserApi->show_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->show_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 

### Return type

[**User**](User.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details for an user |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, update_user_request)

Update a specific user

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.update_user_request import UpdateUserRequest
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
    api_instance = kleister.UserApi(api_client)
    user_id = 'user_id_example' # str | A user identifier or slug
    update_user_request = kleister.UpdateUserRequest() # UpdateUserRequest | The user data to update

    try:
        # Update a specific user
        api_response = api_instance.update_user(user_id, update_user_request)
        print("The response of UserApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user identifier or slug | 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)| The user data to update | 

### Return type

[**User**](User.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The details for an user |  -  |
**400** | Failed to parse request |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

