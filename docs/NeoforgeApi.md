# kleister.NeoforgeApi

All URIs are relative to *https://try.kleister.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_neoforge_to_build**](NeoforgeApi.md#attach_neoforge_to_build) | **POST** /neoforge/{neoforge_id}/builds | Attach a build to a Neoforge version
[**delete_neoforge_from_build**](NeoforgeApi.md#delete_neoforge_from_build) | **DELETE** /neoforge/{neoforge_id}/builds | Unlink a build from a Neoforge version
[**list_neoforge_builds**](NeoforgeApi.md#list_neoforge_builds) | **GET** /neoforge/{neoforge_id}/builds | Fetch the builds attached to a Neoforge version
[**list_neoforges**](NeoforgeApi.md#list_neoforges) | **GET** /neoforge | Fetch the available Neoforge versions
[**update_neoforge**](NeoforgeApi.md#update_neoforge) | **PUT** /neoforge | Update the available Neoforge versions


# **attach_neoforge_to_build**
> Notification attach_neoforge_to_build(neoforge_id, attach_minecraft_to_build_request)

Attach a build to a Neoforge version

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
    api_instance = kleister.NeoforgeApi(api_client)
    neoforge_id = 'neoforge_id_example' # str | A neoforge identifier or slug
    attach_minecraft_to_build_request = kleister.AttachMinecraftToBuildRequest() # AttachMinecraftToBuildRequest | The neoforge build data to create or update

    try:
        # Attach a build to a Neoforge version
        api_response = api_instance.attach_neoforge_to_build(neoforge_id, attach_minecraft_to_build_request)
        print("The response of NeoforgeApi->attach_neoforge_to_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeoforgeApi->attach_neoforge_to_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **neoforge_id** | **str**| A neoforge identifier or slug | 
 **attach_minecraft_to_build_request** | [**AttachMinecraftToBuildRequest**](AttachMinecraftToBuildRequest.md)| The neoforge build data to create or update | 

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

# **delete_neoforge_from_build**
> Notification delete_neoforge_from_build(neoforge_id, attach_minecraft_to_build_request)

Unlink a build from a Neoforge version

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
    api_instance = kleister.NeoforgeApi(api_client)
    neoforge_id = 'neoforge_id_example' # str | A neoforge identifier or slug
    attach_minecraft_to_build_request = kleister.AttachMinecraftToBuildRequest() # AttachMinecraftToBuildRequest | The neoforge build data to create or update

    try:
        # Unlink a build from a Neoforge version
        api_response = api_instance.delete_neoforge_from_build(neoforge_id, attach_minecraft_to_build_request)
        print("The response of NeoforgeApi->delete_neoforge_from_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeoforgeApi->delete_neoforge_from_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **neoforge_id** | **str**| A neoforge identifier or slug | 
 **attach_minecraft_to_build_request** | [**AttachMinecraftToBuildRequest**](AttachMinecraftToBuildRequest.md)| The neoforge build data to create or update | 

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

# **list_neoforge_builds**
> ListNeoforgeBuilds200Response list_neoforge_builds(neoforge_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch the builds attached to a Neoforge version

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.list_neoforge_builds200_response import ListNeoforgeBuilds200Response
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
    api_instance = kleister.NeoforgeApi(api_client)
    neoforge_id = 'neoforge_id_example' # str | A neoforge identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'sort_example' # str | Sorting column (optional)
    order = asc # str | Sorting order (optional) (default to asc)
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch the builds attached to a Neoforge version
        api_response = api_instance.list_neoforge_builds(neoforge_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of NeoforgeApi->list_neoforge_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeoforgeApi->list_neoforge_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **neoforge_id** | **str**| A neoforge identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] 
 **order** | **str**| Sorting order | [optional] [default to asc]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**ListNeoforgeBuilds200Response**](ListNeoforgeBuilds200Response.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of neoforge builds |  -  |
**403** | User is not authorized |  -  |
**404** | Resource not found |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_neoforges**
> ListNeoforges200Response list_neoforges(search=search)

Fetch the available Neoforge versions

### Example

* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.list_neoforges200_response import ListNeoforges200Response
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
    api_instance = kleister.NeoforgeApi(api_client)
    search = 'search_example' # str | Search query (optional)

    try:
        # Fetch the available Neoforge versions
        api_response = api_instance.list_neoforges(search=search)
        print("The response of NeoforgeApi->list_neoforges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeoforgeApi->list_neoforges: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query | [optional] 

### Return type

[**ListNeoforges200Response**](ListNeoforges200Response.md)

### Authorization

[Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of neoforges |  -  |
**403** | User is not authorized |  -  |
**500** | Some internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_neoforge**
> Notification update_neoforge()

Update the available Neoforge versions

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
    api_instance = kleister.NeoforgeApi(api_client)

    try:
        # Update the available Neoforge versions
        api_response = api_instance.update_neoforge()
        print("The response of NeoforgeApi->update_neoforge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NeoforgeApi->update_neoforge: %s\n" % e)
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

