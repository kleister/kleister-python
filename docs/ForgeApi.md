# kleister.ForgeApi

All URIs are relative to *https://try.kleister.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_forge_to_build**](ForgeApi.md#attach_forge_to_build) | **POST** /forge/{forge_id}/builds | Attach a build to a Forge version
[**delete_forge_from_build**](ForgeApi.md#delete_forge_from_build) | **DELETE** /forge/{forge_id}/builds | Unlink a build from a Forge version
[**list_forge_builds**](ForgeApi.md#list_forge_builds) | **GET** /forge/{forge_id}/builds | Fetch the builds attached to a Forge version
[**list_forges**](ForgeApi.md#list_forges) | **GET** /forge | Fetch the available Forge versions
[**update_forge**](ForgeApi.md#update_forge) | **PUT** /forge | Update the available Forge versions


# **attach_forge_to_build**
> Notification attach_forge_to_build(forge_id, attach_minecraft_to_build_request)

Attach a build to a Forge version

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.attach_minecraft_to_build_request import AttachMinecraftToBuildRequest
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
    api_instance = kleister.ForgeApi(api_client)
    forge_id = 'forge_id_example' # str | A forge identifier or slug
    attach_minecraft_to_build_request = kleister.AttachMinecraftToBuildRequest() # AttachMinecraftToBuildRequest | The forge build data to create or update

    try:
        # Attach a build to a Forge version
        api_response = api_instance.attach_forge_to_build(forge_id, attach_minecraft_to_build_request)
        print("The response of ForgeApi->attach_forge_to_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForgeApi->attach_forge_to_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forge_id** | **str**| A forge identifier or slug | 
 **attach_minecraft_to_build_request** | [**AttachMinecraftToBuildRequest**](AttachMinecraftToBuildRequest.md)| The forge build data to create or update | 

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

# **delete_forge_from_build**
> Notification delete_forge_from_build(forge_id, attach_minecraft_to_build_request)

Unlink a build from a Forge version

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.attach_minecraft_to_build_request import AttachMinecraftToBuildRequest
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
    api_instance = kleister.ForgeApi(api_client)
    forge_id = 'forge_id_example' # str | A forge identifier or slug
    attach_minecraft_to_build_request = kleister.AttachMinecraftToBuildRequest() # AttachMinecraftToBuildRequest | The forge build data to create or update

    try:
        # Unlink a build from a Forge version
        api_response = api_instance.delete_forge_from_build(forge_id, attach_minecraft_to_build_request)
        print("The response of ForgeApi->delete_forge_from_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForgeApi->delete_forge_from_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forge_id** | **str**| A forge identifier or slug | 
 **attach_minecraft_to_build_request** | [**AttachMinecraftToBuildRequest**](AttachMinecraftToBuildRequest.md)| The forge build data to create or update | 

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

# **list_forge_builds**
> InlineObject4 list_forge_builds(forge_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch the builds attached to a Forge version

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.inline_object4 import InlineObject4
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
    api_instance = kleister.ForgeApi(api_client)
    forge_id = 'forge_id_example' # str | A forge identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'sort_example' # str | Sorting column (optional)
    order = asc # str | Sorting order (optional) (default to asc)
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch the builds attached to a Forge version
        api_response = api_instance.list_forge_builds(forge_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of ForgeApi->list_forge_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForgeApi->list_forge_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forge_id** | **str**| A forge identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] 
 **order** | **str**| Sorting order | [optional] [default to asc]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**InlineObject4**](InlineObject4.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of forge builds |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_forges**
> InlineObject3 list_forges(search=search)

Fetch the available Forge versions

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.inline_object3 import InlineObject3
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
    api_instance = kleister.ForgeApi(api_client)
    search = 'search_example' # str | Search query (optional)

    try:
        # Fetch the available Forge versions
        api_response = api_instance.list_forges(search=search)
        print("The response of ForgeApi->list_forges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForgeApi->list_forges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query | [optional] 

### Return type

[**InlineObject3**](InlineObject3.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of forges |  -  |
**403** | User is not authorized |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_forge**
> Notification update_forge()

Update the available Forge versions

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
    api_instance = kleister.ForgeApi(api_client)

    try:
        # Update the available Forge versions
        api_response = api_instance.update_forge()
        print("The response of ForgeApi->update_forge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForgeApi->update_forge: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**503** | Remote source is nit available |  -  |
**403** | User is not authorized |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

