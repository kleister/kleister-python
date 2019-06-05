# kleister.PackApi

All URIs are relative to *http://try.kleister.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_build_to_version**](PackApi.md#append_build_to_version) | **POST** /packs/{pack_id}/builds/{build_id}/versions | Assign a version to a build
[**append_pack_to_team**](PackApi.md#append_pack_to_team) | **POST** /packs/{pack_id}/teams | Assign a team to pack
[**append_pack_to_user**](PackApi.md#append_pack_to_user) | **POST** /packs/{pack_id}/users | Assign a user to pack
[**create_build**](PackApi.md#create_build) | **POST** /packs/{pack_id}/builds | Create a new build for a pack
[**create_pack**](PackApi.md#create_pack) | **POST** /packs | Create a new pack
[**delete_build**](PackApi.md#delete_build) | **DELETE** /packs/{pack_id}/builds/{build_id} | Delete a specific build for a pack
[**delete_build_from_version**](PackApi.md#delete_build_from_version) | **DELETE** /packs/{pack_id}/builds/{build_id}/versions | Unlink a version from a build
[**delete_pack**](PackApi.md#delete_pack) | **DELETE** /packs/{pack_id} | Delete a specific pack
[**delete_pack_from_team**](PackApi.md#delete_pack_from_team) | **DELETE** /packs/{pack_id}/teams | Remove a team from pack
[**delete_pack_from_user**](PackApi.md#delete_pack_from_user) | **DELETE** /packs/{pack_id}/users | Remove a user from pack
[**list_build_versions**](PackApi.md#list_build_versions) | **GET** /packs/{pack_id}/builds/{build_id}/versions | Fetch all versions assigned to build
[**list_builds**](PackApi.md#list_builds) | **GET** /packs/{pack_id}/builds | Fetch all available builds for a pack
[**list_pack_teams**](PackApi.md#list_pack_teams) | **GET** /packs/{pack_id}/teams | Fetch all teams assigned to pack
[**list_pack_users**](PackApi.md#list_pack_users) | **GET** /packs/{pack_id}/users | Fetch all users assigned to pack
[**list_packs**](PackApi.md#list_packs) | **GET** /packs | Fetch all available packs
[**permit_pack_team**](PackApi.md#permit_pack_team) | **PUT** /packs/{pack_id}/teams | Update team perms for pack
[**permit_pack_user**](PackApi.md#permit_pack_user) | **PUT** /packs/{pack_id}/users | Update user perms for pack
[**show_build**](PackApi.md#show_build) | **GET** /packs/{pack_id}/builds/{build_id} | Fetch a specific build for a pack
[**show_pack**](PackApi.md#show_pack) | **GET** /packs/{pack_id} | Fetch a specific pack
[**update_build**](PackApi.md#update_build) | **PUT** /packs/{pack_id}/builds/{build_id} | Update a specific build for a pack
[**update_pack**](PackApi.md#update_pack) | **PUT** /packs/{pack_id} | Update a specific pack


# **append_build_to_version**
> GeneralError append_build_to_version(pack_id, build_id, params)

Assign a version to a build

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
build_id = 'build_id_example' # str | A build UUID or slug
params = kleister.BuildVersionParams() # BuildVersionParams | The version data to append to build

try:
    # Assign a version to a build
    api_response = api_instance.append_build_to_version(pack_id, build_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->append_build_to_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **build_id** | **str**| A build UUID or slug | 
 **params** | [**BuildVersionParams**](BuildVersionParams.md)| The version data to append to build | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_pack_to_team**
> GeneralError append_pack_to_team(pack_id, params)

Assign a team to pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
params = kleister.PackTeamParams() # PackTeamParams | The pack team data to assign

try:
    # Assign a team to pack
    api_response = api_instance.append_pack_to_team(pack_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->append_pack_to_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **params** | [**PackTeamParams**](PackTeamParams.md)| The pack team data to assign | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_pack_to_user**
> GeneralError append_pack_to_user(pack_id, params)

Assign a user to pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
params = kleister.PackUserParams() # PackUserParams | The pack user data to assign

try:
    # Assign a user to pack
    api_response = api_instance.append_pack_to_user(pack_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->append_pack_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **params** | [**PackUserParams**](PackUserParams.md)| The pack user data to assign | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build**
> Build create_build(pack_id, params)

Create a new build for a pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
params = kleister.Build() # Build | The build data to create

try:
    # Create a new build for a pack
    api_response = api_instance.create_build(pack_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->create_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **params** | [**Build**](Build.md)| The build data to create | 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pack**
> Pack create_pack(params)

Create a new pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
params = kleister.Pack() # Pack | The pack data to create

try:
    # Create a new pack
    api_response = api_instance.create_pack(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->create_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**Pack**](Pack.md)| The pack data to create | 

### Return type

[**Pack**](Pack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build**
> GeneralError delete_build(pack_id, build_id)

Delete a specific build for a pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
build_id = 'build_id_example' # str | A build UUID or slug

try:
    # Delete a specific build for a pack
    api_response = api_instance.delete_build(pack_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->delete_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **build_id** | **str**| A build UUID or slug | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build_from_version**
> GeneralError delete_build_from_version(pack_id, build_id, params)

Unlink a version from a build

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
build_id = 'build_id_example' # str | A build UUID or slug
params = kleister.BuildVersionParams() # BuildVersionParams | The version data to unlink from build

try:
    # Unlink a version from a build
    api_response = api_instance.delete_build_from_version(pack_id, build_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->delete_build_from_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **build_id** | **str**| A build UUID or slug | 
 **params** | [**BuildVersionParams**](BuildVersionParams.md)| The version data to unlink from build | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pack**
> GeneralError delete_pack(pack_id)

Delete a specific pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug

try:
    # Delete a specific pack
    api_response = api_instance.delete_pack(pack_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->delete_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pack_from_team**
> GeneralError delete_pack_from_team(pack_id, params)

Remove a team from pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
params = kleister.PackTeamParams() # PackTeamParams | The pack team data to delete

try:
    # Remove a team from pack
    api_response = api_instance.delete_pack_from_team(pack_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->delete_pack_from_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **params** | [**PackTeamParams**](PackTeamParams.md)| The pack team data to delete | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pack_from_user**
> GeneralError delete_pack_from_user(pack_id, params)

Remove a user from pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
params = kleister.PackUserParams() # PackUserParams | The pack user data to delete

try:
    # Remove a user from pack
    api_response = api_instance.delete_pack_from_user(pack_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->delete_pack_from_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **params** | [**PackUserParams**](PackUserParams.md)| The pack user data to delete | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_build_versions**
> list[BuildVersion] list_build_versions(pack_id, build_id)

Fetch all versions assigned to build

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
build_id = 'build_id_example' # str | A build UUID or slug

try:
    # Fetch all versions assigned to build
    api_response = api_instance.list_build_versions(pack_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->list_build_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **build_id** | **str**| A build UUID or slug | 

### Return type

[**list[BuildVersion]**](BuildVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_builds**
> list[Build] list_builds(pack_id)

Fetch all available builds for a pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug

try:
    # Fetch all available builds for a pack
    api_response = api_instance.list_builds(pack_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->list_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 

### Return type

[**list[Build]**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pack_teams**
> list[TeamPack] list_pack_teams(pack_id)

Fetch all teams assigned to pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug

try:
    # Fetch all teams assigned to pack
    api_response = api_instance.list_pack_teams(pack_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->list_pack_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 

### Return type

[**list[TeamPack]**](TeamPack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pack_users**
> list[UserPack] list_pack_users(pack_id)

Fetch all users assigned to pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug

try:
    # Fetch all users assigned to pack
    api_response = api_instance.list_pack_users(pack_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->list_pack_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 

### Return type

[**list[UserPack]**](UserPack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packs**
> list[Pack] list_packs()

Fetch all available packs

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()

try:
    # Fetch all available packs
    api_response = api_instance.list_packs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->list_packs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Pack]**](Pack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_pack_team**
> GeneralError permit_pack_team(pack_id, params)

Update team perms for pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
params = kleister.PackTeamParams() # PackTeamParams | The pack team data to update

try:
    # Update team perms for pack
    api_response = api_instance.permit_pack_team(pack_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->permit_pack_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **params** | [**PackTeamParams**](PackTeamParams.md)| The pack team data to update | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_pack_user**
> GeneralError permit_pack_user(pack_id, params)

Update user perms for pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
params = kleister.PackUserParams() # PackUserParams | The pack user data to update

try:
    # Update user perms for pack
    api_response = api_instance.permit_pack_user(pack_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->permit_pack_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **params** | [**PackUserParams**](PackUserParams.md)| The pack user data to update | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_build**
> Build show_build(pack_id, build_id)

Fetch a specific build for a pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
build_id = 'build_id_example' # str | A build UUID or slug

try:
    # Fetch a specific build for a pack
    api_response = api_instance.show_build(pack_id, build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->show_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **build_id** | **str**| A build UUID or slug | 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_pack**
> Pack show_pack(pack_id)

Fetch a specific pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug

try:
    # Fetch a specific pack
    api_response = api_instance.show_pack(pack_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->show_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 

### Return type

[**Pack**](Pack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_build**
> Build update_build(pack_id, build_id, params)

Update a specific build for a pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
build_id = 'build_id_example' # str | A build UUID or slug
params = kleister.Build() # Build | The build data to update

try:
    # Update a specific build for a pack
    api_response = api_instance.update_build(pack_id, build_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->update_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **build_id** | **str**| A build UUID or slug | 
 **params** | [**Build**](Build.md)| The build data to update | 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pack**
> Pack update_pack(pack_id, params)

Update a specific pack

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.PackApi()
pack_id = 'pack_id_example' # str | A pack UUID or slug
params = kleister.Pack() # Pack | The pack data to update

try:
    # Update a specific pack
    api_response = api_instance.update_pack(pack_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackApi->update_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pack_id** | **str**| A pack UUID or slug | 
 **params** | [**Pack**](Pack.md)| The pack data to update | 

### Return type

[**Pack**](Pack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

