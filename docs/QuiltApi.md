# kleister.QuiltApi

All URIs are relative to *https://try.kleister.eu/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_quilt_to_build**](QuiltApi.md#attach_quilt_to_build) | **POST** /quilt/{quilt_id}/builds | Attach a build to a Quilt version
[**delete_quilt_from_build**](QuiltApi.md#delete_quilt_from_build) | **DELETE** /quilt/{quilt_id}/builds | Unlink a build from a Quilt version
[**list_quilt_builds**](QuiltApi.md#list_quilt_builds) | **GET** /quilt/{quilt_id}/builds | Fetch the builds attached to a Quilt version
[**list_quilts**](QuiltApi.md#list_quilts) | **GET** /quilt | Fetch the available Quilt versions
[**update_quilt**](QuiltApi.md#update_quilt) | **PUT** /quilt | Update the available Quilt versions


# **attach_quilt_to_build**
> Notification attach_quilt_to_build(quilt_id, quilt_build_params)

Attach a build to a Quilt version

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.quilt_build_params import QuiltBuildParams
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
    api_instance = kleister.QuiltApi(api_client)
    quilt_id = 'quilt_id_example' # str | A quilt identifier or slug
    quilt_build_params = kleister.QuiltBuildParams() # QuiltBuildParams | The build data to attach

    try:
        # Attach a build to a Quilt version
        api_response = api_instance.attach_quilt_to_build(quilt_id, quilt_build_params)
        print("The response of QuiltApi->attach_quilt_to_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuiltApi->attach_quilt_to_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quilt_id** | **str**| A quilt identifier or slug | 
 **quilt_build_params** | [**QuiltBuildParams**](QuiltBuildParams.md)| The build data to attach | 

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
**404** | Quilt or build not found |  -  |
**412** | Build is already attached |  -  |
**422** | Failed to validate request |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quilt_from_build**
> Notification delete_quilt_from_build(quilt_id, quilt_build_params)

Unlink a build from a Quilt version

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.notification import Notification
from kleister.models.quilt_build_params import QuiltBuildParams
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
    api_instance = kleister.QuiltApi(api_client)
    quilt_id = 'quilt_id_example' # str | A quilt identifier or slug
    quilt_build_params = kleister.QuiltBuildParams() # QuiltBuildParams | The build data to unlink

    try:
        # Unlink a build from a Quilt version
        api_response = api_instance.delete_quilt_from_build(quilt_id, quilt_build_params)
        print("The response of QuiltApi->delete_quilt_from_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuiltApi->delete_quilt_from_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quilt_id** | **str**| A quilt identifier or slug | 
 **quilt_build_params** | [**QuiltBuildParams**](QuiltBuildParams.md)| The build data to unlink | 

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
**404** | Quilt or build not found |  -  |
**412** | Build is not attached |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quilt_builds**
> QuiltBuilds list_quilt_builds(quilt_id, search=search, sort=sort, order=order, limit=limit, offset=offset)

Fetch the builds attached to a Quilt version

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.quilt_builds import QuiltBuilds
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
    api_instance = kleister.QuiltApi(api_client)
    quilt_id = 'quilt_id_example' # str | A quilt identifier or slug
    search = 'search_example' # str | Search query (optional)
    sort = 'name' # str | Sorting column (optional) (default to 'name')
    order = 'asc' # str | Sorting order (optional) (default to 'asc')
    limit = 100 # int | Paging limit (optional) (default to 100)
    offset = 0 # int | Paging offset (optional) (default to 0)

    try:
        # Fetch the builds attached to a Quilt version
        api_response = api_instance.list_quilt_builds(quilt_id, search=search, sort=sort, order=order, limit=limit, offset=offset)
        print("The response of QuiltApi->list_quilt_builds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuiltApi->list_quilt_builds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quilt_id** | **str**| A quilt identifier or slug | 
 **search** | **str**| Search query | [optional] 
 **sort** | **str**| Sorting column | [optional] [default to &#39;name&#39;]
 **order** | **str**| Sorting order | [optional] [default to &#39;asc&#39;]
 **limit** | **int**| Paging limit | [optional] [default to 100]
 **offset** | **int**| Paging offset | [optional] [default to 0]

### Return type

[**QuiltBuilds**](QuiltBuilds.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of attached builds |  -  |
**403** | User is not authorized |  -  |
**404** | Quilt or build not found |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quilts**
> Quilts list_quilts(search=search)

Fetch the available Quilt versions

### Example

* Api Key Authentication (Cookie):
* Basic Authentication (Basic):
* Api Key Authentication (Header):
* Bearer Authentication (Bearer):

```python
import kleister
from kleister.models.quilts import Quilts
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
    api_instance = kleister.QuiltApi(api_client)
    search = 'search_example' # str | Search query (optional)

    try:
        # Fetch the available Quilt versions
        api_response = api_instance.list_quilts(search=search)
        print("The response of QuiltApi->list_quilts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuiltApi->list_quilts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query | [optional] 

### Return type

[**Quilts**](Quilts.md)

### Authorization

[Cookie](../README.md#Cookie), [Basic](../README.md#Basic), [Header](../README.md#Header), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of quilt versions |  -  |
**403** | User is not authorized |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quilt**
> Notification update_quilt()

Update the available Quilt versions

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
    api_instance = kleister.QuiltApi(api_client)

    try:
        # Update the available Quilt versions
        api_response = api_instance.update_quilt()
        print("The response of QuiltApi->update_quilt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuiltApi->update_quilt: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**503** | If remote source is not available |  -  |
**403** | User is not authorized |  -  |
**500** | Some internal server error |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

