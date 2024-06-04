# kleister.TeamApi

All URIs are relative to *https://try.kleister.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_team_to_mod**](TeamApi.md#attach_team_to_mod) | **POST** /teams/{team_id}/mods | Attach a mod to team
[**attach_team_to_pack**](TeamApi.md#attach_team_to_pack) | **POST** /teams/{team_id}/packs | Attach a pack to team
[**attach_team_to_user**](TeamApi.md#attach_team_to_user) | **POST** /teams/{team_id}/users | Attach a user to team
[**create_team**](TeamApi.md#create_team) | **POST** /teams | Create a new team
[**delete_team**](TeamApi.md#delete_team) | **DELETE** /teams/{team_id} | Delete a specific team
[**delete_team_from_mod**](TeamApi.md#delete_team_from_mod) | **DELETE** /teams/{team_id}/mods | Unlink a mod from team
[**delete_team_from_pack**](TeamApi.md#delete_team_from_pack) | **DELETE** /teams/{team_id}/packs | Unlink a pack from team
[**delete_team_from_user**](TeamApi.md#delete_team_from_user) | **DELETE** /teams/{team_id}/users | Unlink a user from team
[**list_team_mods**](TeamApi.md#list_team_mods) | **GET** /teams/{team_id}/mods | Fetch all mods attached to team
[**list_team_packs**](TeamApi.md#list_team_packs) | **GET** /teams/{team_id}/packs | Fetch all packs attached to team
[**list_team_users**](TeamApi.md#list_team_users) | **GET** /teams/{team_id}/users | Fetch all users attached to team
[**list_teams**](TeamApi.md#list_teams) | **GET** /teams | Fetch all available teams
[**permit_team_mod**](TeamApi.md#permit_team_mod) | **PUT** /teams/{team_id}/mods | Update mod perms for team
[**permit_team_pack**](TeamApi.md#permit_team_pack) | **PUT** /teams/{team_id}/packs | Update pack perms for team
[**permit_team_user**](TeamApi.md#permit_team_user) | **PUT** /teams/{team_id}/users | Update user perms for team
[**show_team**](TeamApi.md#show_team) | **GET** /teams/{team_id} | Fetch a specific team
[**update_team**](TeamApi.md#update_team) | **PUT** /teams/{team_id} | Update a specific team


# **attach_team_to_mod**
> Notification attach_team_to_mod(team_id, team_mod_params)

Attach a mod to team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.team_mod_params import TeamModParams
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    team_mod_params = kleister.TeamModParams() # TeamModParams | The team mod data to attach

    try:
        # Attach a mod to team
        api_response = api_instance.attach_team_to_mod(team_id, team_mod_params)
        print("The response of TeamApi->attach_team_to_mod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->attach_team_to_mod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **team_mod_params** | [**TeamModParams**](TeamModParams.md)| The team mod data to attach | 

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
**404** | Team or mod not found |  -  |
**412** | Mod is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_team_to_pack**
> Notification attach_team_to_pack(team_id, team_pack_params)

Attach a pack to team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.team_pack_params import TeamPackParams
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    team_pack_params = kleister.TeamPackParams() # TeamPackParams | The team pack data to attach

    try:
        # Attach a pack to team
        api_response = api_instance.attach_team_to_pack(team_id, team_pack_params)
        print("The response of TeamApi->attach_team_to_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->attach_team_to_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **team_pack_params** | [**TeamPackParams**](TeamPackParams.md)| The team pack data to attach | 

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
**404** | Team or pack not found |  -  |
**412** | Pack is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_team_to_user**
> Notification attach_team_to_user(team_id, team_user_params)

Attach a user to team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.team_user_params import TeamUserParams
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    team_user_params = kleister.TeamUserParams() # TeamUserParams | The team user data to attach

    try:
        # Attach a user to team
        api_response = api_instance.attach_team_to_user(team_id, team_user_params)
        print("The response of TeamApi->attach_team_to_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->attach_team_to_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **team_user_params** | [**TeamUserParams**](TeamUserParams.md)| The team user data to attach | 

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
**404** | Team or user not found |  -  |
**412** | User is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team**
> Team create_team(team)

Create a new team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.team import Team
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
    api_instance = kleister.TeamApi(api_client)
    team = kleister.Team() # Team | The team data to create

    try:
        # Create a new team
        api_response = api_instance.create_team(team)
        print("The response of TeamApi->create_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->create_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | [**Team**](Team.md)| The team data to create | 

### Return type

[**Team**](Team.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created team data |  -  |
**403** | User is not authorized |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> Notification delete_team(team_id)

Delete a specific team

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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug

    try:
        # Delete a specific team
        api_response = api_instance.delete_team(team_id)
        print("The response of TeamApi->delete_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->delete_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 

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
**404** | Team not found |  -  |
**400** | Failed to delete the team |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_from_mod**
> Notification delete_team_from_mod(team_id, team_mod_params)

Unlink a mod from team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.team_mod_params import TeamModParams
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    team_mod_params = kleister.TeamModParams() # TeamModParams | The team mod data to unlink

    try:
        # Unlink a mod from team
        api_response = api_instance.delete_team_from_mod(team_id, team_mod_params)
        print("The response of TeamApi->delete_team_from_mod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->delete_team_from_mod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **team_mod_params** | [**TeamModParams**](TeamModParams.md)| The team mod data to unlink | 

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
**404** | Team or mod not found |  -  |
**412** | Mod is not attached |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_from_pack**
> Notification delete_team_from_pack(team_id, team_pack_params)

Unlink a pack from team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.team_pack_params import TeamPackParams
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    team_pack_params = kleister.TeamPackParams() # TeamPackParams | The team pack data to unlink

    try:
        # Unlink a pack from team
        api_response = api_instance.delete_team_from_pack(team_id, team_pack_params)
        print("The response of TeamApi->delete_team_from_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->delete_team_from_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **team_pack_params** | [**TeamPackParams**](TeamPackParams.md)| The team pack data to unlink | 

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
**404** | Team or pack not found |  -  |
**412** | Pack is not attached |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_from_user**
> Notification delete_team_from_user(team_id, team_user_params)

Unlink a user from team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.team_user_params import TeamUserParams
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    team_user_params = kleister.TeamUserParams() # TeamUserParams | The team user data to unlink

    try:
        # Unlink a user from team
        api_response = api_instance.delete_team_from_user(team_id, team_user_params)
        print("The response of TeamApi->delete_team_from_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->delete_team_from_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **team_user_params** | [**TeamUserParams**](TeamUserParams.md)| The team user data to unlink | 

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
**404** | Team or user not found |  -  |
**412** | User is not attached |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_mods**
> TeamMods list_team_mods(team_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all mods attached to team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.team_mods import TeamMods
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'modname' # str | Sorting column (optional) (default to 'modname')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all mods attached to team
        api_response = api_instance.list_team_mods(team_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of TeamApi->list_team_mods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->list_team_mods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;modname&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**TeamMods**](TeamMods.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of team mods |  -  |
**403** | User is not authorized |  -  |
**404** | Team not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_packs**
> TeamPacks list_team_packs(team_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all packs attached to team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.team_packs import TeamPacks
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'packname' # str | Sorting column (optional) (default to 'packname')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all packs attached to team
        api_response = api_instance.list_team_packs(team_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of TeamApi->list_team_packs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->list_team_packs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;packname&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**TeamPacks**](TeamPacks.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of team packs |  -  |
**403** | User is not authorized |  -  |
**404** | Team not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_users**
> TeamUsers list_team_users(team_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all users attached to team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.team_users import TeamUsers
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'username' # str | Sorting column (optional) (default to 'username')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all users attached to team
        api_response = api_instance.list_team_users(team_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of TeamApi->list_team_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->list_team_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;username&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**TeamUsers**](TeamUsers.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of team users |  -  |
**403** | User is not authorized |  -  |
**404** | Team not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_teams**
> Teams list_teams(search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch all available teams

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.teams import Teams
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
    api_instance = kleister.TeamApi(api_client)
    search = 'search_example' # str | Search query (optional)
    sort = 'name' # str | Sorting column (optional) (default to 'name')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch all available teams
        api_response = api_instance.list_teams(search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of TeamApi->list_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->list_teams: %s\n" % e)
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

[**Teams**](Teams.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of teams |  -  |
**403** | User is not authorized |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_team_mod**
> Notification permit_team_mod(team_id, team_mod_params)

Update mod perms for team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.team_mod_params import TeamModParams
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    team_mod_params = kleister.TeamModParams() # TeamModParams | The team mod data to update

    try:
        # Update mod perms for team
        api_response = api_instance.permit_team_mod(team_id, team_mod_params)
        print("The response of TeamApi->permit_team_mod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->permit_team_mod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **team_mod_params** | [**TeamModParams**](TeamModParams.md)| The team mod data to update | 

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
**404** | Team or mod not found |  -  |
**412** | Mod is not attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_team_pack**
> Notification permit_team_pack(team_id, team_pack_params)

Update pack perms for team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.team_pack_params import TeamPackParams
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    team_pack_params = kleister.TeamPackParams() # TeamPackParams | The team pack data to update

    try:
        # Update pack perms for team
        api_response = api_instance.permit_team_pack(team_id, team_pack_params)
        print("The response of TeamApi->permit_team_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->permit_team_pack: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **team_pack_params** | [**TeamPackParams**](TeamPackParams.md)| The team pack data to update | 

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
**404** | Team or pack not found |  -  |
**412** | Pack is not attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_team_user**
> Notification permit_team_user(team_id, team_user_params)

Update user perms for team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.team_user_params import TeamUserParams
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    team_user_params = kleister.TeamUserParams() # TeamUserParams | The team user data to update

    try:
        # Update user perms for team
        api_response = api_instance.permit_team_user(team_id, team_user_params)
        print("The response of TeamApi->permit_team_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->permit_team_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **team_user_params** | [**TeamUserParams**](TeamUserParams.md)| The team user data to update | 

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
**404** | Team or user not found |  -  |
**412** | User is not attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_team**
> Team show_team(team_id)

Fetch a specific team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.team import Team
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug

    try:
        # Fetch a specific team
        api_response = api_instance.show_team(team_id)
        print("The response of TeamApi->show_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->show_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 

### Return type

[**Team**](Team.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetched team details |  -  |
**403** | User is not authorized |  -  |
**404** | Team not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> Team update_team(team_id, team)

Update a specific team

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.team import Team
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
    api_instance = kleister.TeamApi(api_client)
    team_id = 'team_id_example' # str | A team identifier or slug
    team = kleister.Team() # Team | The team data to update

    try:
        # Update a specific team
        api_response = api_instance.update_team(team_id, team)
        print("The response of TeamApi->update_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamApi->update_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team identifier or slug | 
 **team** | [**Team**](Team.md)| The team data to update | 

### Return type

[**Team**](Team.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated team details |  -  |
**403** | User is not authorized |  -  |
**404** | Team not found |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

