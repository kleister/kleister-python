# kleister.ForgeApi

All URIs are relative to *http://try.kleister.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_forge_to_build**](ForgeApi.md#append_forge_to_build) | **POST** /forge/{forge_id}/builds | Assign a build to a Forge version
[**delete_forge_from_build**](ForgeApi.md#delete_forge_from_build) | **DELETE** /forge/{forge_id}/builds | Unlink a build from a Forge version
[**list_forge_builds**](ForgeApi.md#list_forge_builds) | **GET** /forge/{forge_id}/builds | Fetch the builds assigned to a Forge version
[**list_forges**](ForgeApi.md#list_forges) | **GET** /forge | Fetch the available Forge versions
[**search_forges**](ForgeApi.md#search_forges) | **GET** /forge/{forge_id} | Search for available Forge versions
[**update_forge**](ForgeApi.md#update_forge) | **PUT** /forge | Update the available Forge versions


# **append_forge_to_build**
> [Build] append_forge_to_build(forge_id, forge_build)

Assign a build to a Forge version

### Example


```python
import time
import kleister
from kleister.api import forge_api
from kleister.model.general_error import GeneralError
from kleister.model.build import Build
from kleister.model.forge_build_params import ForgeBuildParams
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
    api_instance = forge_api.ForgeApi(api_client)
    forge_id = "forge_id_example" # str | A forge UUID or slug
    forge_build = ForgeBuildParams(
        pack="pack_example",
        build="build_example",
    ) # ForgeBuildParams | The build data to append

    # example passing only required values which don't have defaults set
    try:
        # Assign a build to a Forge version
        api_response = api_instance.append_forge_to_build(forge_id, forge_build)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ForgeApi->append_forge_to_build: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forge_id** | **str**| A forge UUID or slug |
 **forge_build** | [**ForgeBuildParams**](ForgeBuildParams.md)| The build data to append |

### Return type

[**[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of assigned builds |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Build is already appended |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_forge_from_build**
> [Build] delete_forge_from_build(forge_id, forge_build)

Unlink a build from a Forge version

### Example


```python
import time
import kleister
from kleister.api import forge_api
from kleister.model.general_error import GeneralError
from kleister.model.build import Build
from kleister.model.forge_build_params import ForgeBuildParams
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
    api_instance = forge_api.ForgeApi(api_client)
    forge_id = "forge_id_example" # str | A forge UUID or slug
    forge_build = ForgeBuildParams(
        pack="pack_example",
        build="build_example",
    ) # ForgeBuildParams | The build data to unlink

    # example passing only required values which don't have defaults set
    try:
        # Unlink a build from a Forge version
        api_response = api_instance.delete_forge_from_build(forge_id, forge_build)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ForgeApi->delete_forge_from_build: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forge_id** | **str**| A forge UUID or slug |
 **forge_build** | [**ForgeBuildParams**](ForgeBuildParams.md)| The build data to unlink |

### Return type

[**[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of assigned builds |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Build is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_forge_builds**
> [Build] list_forge_builds(forge_id)

Fetch the builds assigned to a Forge version

### Example


```python
import time
import kleister
from kleister.api import forge_api
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
    api_instance = forge_api.ForgeApi(api_client)
    forge_id = "forge_id_example" # str | A forge UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch the builds assigned to a Forge version
        api_response = api_instance.list_forge_builds(forge_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ForgeApi->list_forge_builds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forge_id** | **str**| A forge UUID or slug |

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
**200** | A collection of assigned builds |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_forges**
> [Forge] list_forges()

Fetch the available Forge versions

### Example


```python
import time
import kleister
from kleister.api import forge_api
from kleister.model.general_error import GeneralError
from kleister.model.forge import Forge
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = forge_api.ForgeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch the available Forge versions
        api_response = api_instance.list_forges()
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ForgeApi->list_forges: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Forge]**](Forge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Forge versions |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_forges**
> [Forge] search_forges(forge_id)

Search for available Forge versions

### Example


```python
import time
import kleister
from kleister.api import forge_api
from kleister.model.general_error import GeneralError
from kleister.model.forge import Forge
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = forge_api.ForgeApi(api_client)
    forge_id = "forge_id_example" # str | A search token to search Forge versions

    # example passing only required values which don't have defaults set
    try:
        # Search for available Forge versions
        api_response = api_instance.search_forges(forge_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ForgeApi->search_forges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forge_id** | **str**| A search token to search Forge versions |

### Return type

[**[Forge]**](Forge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Forge versions |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_forge**
> GeneralError update_forge()

Update the available Forge versions

### Example


```python
import time
import kleister
from kleister.api import forge_api
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
    api_instance = forge_api.ForgeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update the available Forge versions
        api_response = api_instance.update_forge()
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling ForgeApi->update_forge: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**403** | User is not authorized |  -  |
**503** | If remote source is not available |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

