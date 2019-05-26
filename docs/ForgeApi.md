# kleister.ForgeApi

All URIs are relative to *http://http:/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_forge_to_build**](ForgeApi.md#append_forge_to_build) | **POST** /forge/{forge_id}/builds | Assign a build to a Forge version
[**delete_forge_from_build**](ForgeApi.md#delete_forge_from_build) | **DELETE** /forge/{forge_id}/builds | Unlink a build from a Forge version
[**list_forge_builds**](ForgeApi.md#list_forge_builds) | **GET** /forge/{forge_id}/builds | Fetch the builds assigned to a Forge version
[**list_forges**](ForgeApi.md#list_forges) | **GET** /forge | Fetch the available Forge versions
[**search_forges**](ForgeApi.md#search_forges) | **GET** /forge/{forge_id} | Search for available Forge versions
[**update_forge**](ForgeApi.md#update_forge) | **PUT** /forge | Update the available Forge versions


# **append_forge_to_build**
> list[Build] append_forge_to_build(forge_id, params)

Assign a build to a Forge version

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ForgeApi()
forge_id = 'forge_id_example' # str | A forge UUID or slug
params = kleister.ForgeBuildParams() # ForgeBuildParams | The build data to append

try:
    # Assign a build to a Forge version
    api_response = api_instance.append_forge_to_build(forge_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForgeApi->append_forge_to_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forge_id** | **str**| A forge UUID or slug | 
 **params** | [**ForgeBuildParams**](ForgeBuildParams.md)| The build data to append | 

### Return type

[**list[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_forge_from_build**
> list[Build] delete_forge_from_build(forge_id, params)

Unlink a build from a Forge version

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ForgeApi()
forge_id = 'forge_id_example' # str | A forge UUID or slug
params = kleister.ForgeBuildParams() # ForgeBuildParams | The build data to unlink

try:
    # Unlink a build from a Forge version
    api_response = api_instance.delete_forge_from_build(forge_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForgeApi->delete_forge_from_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forge_id** | **str**| A forge UUID or slug | 
 **params** | [**ForgeBuildParams**](ForgeBuildParams.md)| The build data to unlink | 

### Return type

[**list[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_forge_builds**
> list[Build] list_forge_builds(forge_id)

Fetch the builds assigned to a Forge version

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ForgeApi()
forge_id = 'forge_id_example' # str | A forge UUID or slug

try:
    # Fetch the builds assigned to a Forge version
    api_response = api_instance.list_forge_builds(forge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForgeApi->list_forge_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forge_id** | **str**| A forge UUID or slug | 

### Return type

[**list[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_forges**
> list[Forge] list_forges()

Fetch the available Forge versions

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ForgeApi()

try:
    # Fetch the available Forge versions
    api_response = api_instance.list_forges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForgeApi->list_forges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Forge]**](Forge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_forges**
> list[Forge] search_forges(forge_id)

Search for available Forge versions

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ForgeApi()
forge_id = 'forge_id_example' # str | A search token to search Forge versions

try:
    # Search for available Forge versions
    api_response = api_instance.search_forges(forge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForgeApi->search_forges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forge_id** | **str**| A search token to search Forge versions | 

### Return type

[**list[Forge]**](Forge.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_forge**
> object update_forge()

Update the available Forge versions

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ForgeApi()

try:
    # Update the available Forge versions
    api_response = api_instance.update_forge()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ForgeApi->update_forge: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

