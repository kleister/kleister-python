# kleister.MinecraftApi

All URIs are relative to *http://try.kleister.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_minecraft_to_build**](MinecraftApi.md#append_minecraft_to_build) | **POST** /minecraft/{minecraft_id}/builds | Assign a build to a Minecraft version
[**delete_minecraft_from_build**](MinecraftApi.md#delete_minecraft_from_build) | **DELETE** /minecraft/{minecraft_id}/builds | Unlink a build from a Minecraft version
[**list_minecraft_builds**](MinecraftApi.md#list_minecraft_builds) | **GET** /minecraft/{minecraft_id}/builds | Fetch the builds assigned to a Minecraft version
[**list_minecrafts**](MinecraftApi.md#list_minecrafts) | **GET** /minecraft | Fetch the available Minecraft versions
[**search_minecrafts**](MinecraftApi.md#search_minecrafts) | **GET** /minecraft/{minecraft_id} | Search for available Minecraft versions
[**update_minecraft**](MinecraftApi.md#update_minecraft) | **PUT** /minecraft | Update the available Minecraft versions


# **append_minecraft_to_build**
> [Build] append_minecraft_to_build(minecraft_id, minecraft_build)

Assign a build to a Minecraft version

### Example


```python
import time
import kleister
from kleister.api import minecraft_api
from kleister.model.general_error import GeneralError
from kleister.model.build import Build
from kleister.model.minecraft_build_params import MinecraftBuildParams
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
    api_instance = minecraft_api.MinecraftApi(api_client)
    minecraft_id = "minecraft_id_example" # str | A minecraft UUID or slug
    minecraft_build = MinecraftBuildParams(
        pack="pack_example",
        build="build_example",
    ) # MinecraftBuildParams | The build data to append

    # example passing only required values which don't have defaults set
    try:
        # Assign a build to a Minecraft version
        api_response = api_instance.append_minecraft_to_build(minecraft_id, minecraft_build)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling MinecraftApi->append_minecraft_to_build: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minecraft_id** | **str**| A minecraft UUID or slug |
 **minecraft_build** | [**MinecraftBuildParams**](MinecraftBuildParams.md)| The build data to append |

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

# **delete_minecraft_from_build**
> [Build] delete_minecraft_from_build(minecraft_id, minecraft_build)

Unlink a build from a Minecraft version

### Example


```python
import time
import kleister
from kleister.api import minecraft_api
from kleister.model.general_error import GeneralError
from kleister.model.build import Build
from kleister.model.minecraft_build_params import MinecraftBuildParams
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
    api_instance = minecraft_api.MinecraftApi(api_client)
    minecraft_id = "minecraft_id_example" # str | A minecraft UUID or slug
    minecraft_build = MinecraftBuildParams(
        pack="pack_example",
        build="build_example",
    ) # MinecraftBuildParams | The build data to unlink

    # example passing only required values which don't have defaults set
    try:
        # Unlink a build from a Minecraft version
        api_response = api_instance.delete_minecraft_from_build(minecraft_id, minecraft_build)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling MinecraftApi->delete_minecraft_from_build: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minecraft_id** | **str**| A minecraft UUID or slug |
 **minecraft_build** | [**MinecraftBuildParams**](MinecraftBuildParams.md)| The build data to unlink |

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

# **list_minecraft_builds**
> [Build] list_minecraft_builds(minecraft_id)

Fetch the builds assigned to a Minecraft version

### Example


```python
import time
import kleister
from kleister.api import minecraft_api
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
    api_instance = minecraft_api.MinecraftApi(api_client)
    minecraft_id = "minecraft_id_example" # str | A minecraft UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch the builds assigned to a Minecraft version
        api_response = api_instance.list_minecraft_builds(minecraft_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling MinecraftApi->list_minecraft_builds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minecraft_id** | **str**| A minecraft UUID or slug |

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

# **list_minecrafts**
> [Minecraft] list_minecrafts()

Fetch the available Minecraft versions

### Example


```python
import time
import kleister
from kleister.api import minecraft_api
from kleister.model.general_error import GeneralError
from kleister.model.minecraft import Minecraft
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = minecraft_api.MinecraftApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch the available Minecraft versions
        api_response = api_instance.list_minecrafts()
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling MinecraftApi->list_minecrafts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Minecraft]**](Minecraft.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Minecraft versions |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_minecrafts**
> [Minecraft] search_minecrafts(minecraft_id)

Search for available Minecraft versions

### Example


```python
import time
import kleister
from kleister.api import minecraft_api
from kleister.model.general_error import GeneralError
from kleister.model.minecraft import Minecraft
from pprint import pprint
# Defining the host is optional and defaults to http://try.kleister.tech/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = minecraft_api.MinecraftApi(api_client)
    minecraft_id = "minecraft_id_example" # str | A search token to search Minecraft versions

    # example passing only required values which don't have defaults set
    try:
        # Search for available Minecraft versions
        api_response = api_instance.search_minecrafts(minecraft_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling MinecraftApi->search_minecrafts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minecraft_id** | **str**| A search token to search Minecraft versions |

### Return type

[**[Minecraft]**](Minecraft.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of Minecraft versions |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_minecraft**
> GeneralError update_minecraft()

Update the available Minecraft versions

### Example


```python
import time
import kleister
from kleister.api import minecraft_api
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
    api_instance = minecraft_api.MinecraftApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Update the available Minecraft versions
        api_response = api_instance.update_minecraft()
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling MinecraftApi->update_minecraft: %s\n" % e)
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

