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
> list[Build] append_minecraft_to_build(minecraft_id, params)

Assign a build to a Minecraft version

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.MinecraftApi()
minecraft_id = 'minecraft_id_example' # str | A minecraft UUID or slug
params = kleister.MinecraftBuildParams() # MinecraftBuildParams | The build data to append

try:
    # Assign a build to a Minecraft version
    api_response = api_instance.append_minecraft_to_build(minecraft_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinecraftApi->append_minecraft_to_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minecraft_id** | **str**| A minecraft UUID or slug | 
 **params** | [**MinecraftBuildParams**](MinecraftBuildParams.md)| The build data to append | 

### Return type

[**list[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_minecraft_from_build**
> list[Build] delete_minecraft_from_build(minecraft_id, params)

Unlink a build from a Minecraft version

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.MinecraftApi()
minecraft_id = 'minecraft_id_example' # str | A minecraft UUID or slug
params = kleister.MinecraftBuildParams() # MinecraftBuildParams | The build data to unlink

try:
    # Unlink a build from a Minecraft version
    api_response = api_instance.delete_minecraft_from_build(minecraft_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinecraftApi->delete_minecraft_from_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minecraft_id** | **str**| A minecraft UUID or slug | 
 **params** | [**MinecraftBuildParams**](MinecraftBuildParams.md)| The build data to unlink | 

### Return type

[**list[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_minecraft_builds**
> list[Build] list_minecraft_builds(minecraft_id)

Fetch the builds assigned to a Minecraft version

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.MinecraftApi()
minecraft_id = 'minecraft_id_example' # str | A minecraft UUID or slug

try:
    # Fetch the builds assigned to a Minecraft version
    api_response = api_instance.list_minecraft_builds(minecraft_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinecraftApi->list_minecraft_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minecraft_id** | **str**| A minecraft UUID or slug | 

### Return type

[**list[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_minecrafts**
> list[Minecraft] list_minecrafts()

Fetch the available Minecraft versions

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.MinecraftApi()

try:
    # Fetch the available Minecraft versions
    api_response = api_instance.list_minecrafts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinecraftApi->list_minecrafts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Minecraft]**](Minecraft.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_minecrafts**
> list[Minecraft] search_minecrafts(minecraft_id)

Search for available Minecraft versions

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.MinecraftApi()
minecraft_id = 'minecraft_id_example' # str | A search token to search Minecraft versions

try:
    # Search for available Minecraft versions
    api_response = api_instance.search_minecrafts(minecraft_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MinecraftApi->search_minecrafts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minecraft_id** | **str**| A search token to search Minecraft versions | 

### Return type

[**list[Minecraft]**](Minecraft.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_minecraft**
> GeneralError update_minecraft()

Update the available Minecraft versions

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.MinecraftApi()

try:
    # Update the available Minecraft versions
    api_response = api_instance.update_minecraft()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

