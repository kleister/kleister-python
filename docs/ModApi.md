# kleister.ModApi

All URIs are relative to *http://try.kleister.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_mod_to_team**](ModApi.md#append_mod_to_team) | **POST** /mods/{mod_id}/teams | Assign a team to mod
[**append_mod_to_user**](ModApi.md#append_mod_to_user) | **POST** /mods/{mod_id}/users | Assign a user to mod
[**append_version_to_build**](ModApi.md#append_version_to_build) | **POST** /mods/{mod_id}/versions/{version_id}/builds | Assign a build to a version
[**create_mod**](ModApi.md#create_mod) | **POST** /mods | Create a new mod
[**create_version**](ModApi.md#create_version) | **POST** /mods/{mod_id}/versions | Create a new version for a mod
[**delete_mod**](ModApi.md#delete_mod) | **DELETE** /mods/{mod_id} | Delete a specific mod
[**delete_mod_from_team**](ModApi.md#delete_mod_from_team) | **DELETE** /mods/{mod_id}/teams | Remove a team from mod
[**delete_mod_from_user**](ModApi.md#delete_mod_from_user) | **DELETE** /mods/{mod_id}/users | Remove a user from mod
[**delete_version**](ModApi.md#delete_version) | **DELETE** /mods/{mod_id}/versions/{version_id} | Delete a specific version for a mod
[**delete_version_from_build**](ModApi.md#delete_version_from_build) | **DELETE** /mods/{mod_id}/versions/{version_id}/builds | Unlink a build from a version
[**list_mod_teams**](ModApi.md#list_mod_teams) | **GET** /mods/{mod_id}/teams | Fetch all teams assigned to mod
[**list_mod_users**](ModApi.md#list_mod_users) | **GET** /mods/{mod_id}/users | Fetch all users assigned to mod
[**list_mods**](ModApi.md#list_mods) | **GET** /mods | Fetch all available mods
[**list_version_builds**](ModApi.md#list_version_builds) | **GET** /mods/{mod_id}/versions/{version_id}/builds | Fetch all builds assigned to version
[**list_versions**](ModApi.md#list_versions) | **GET** /mods/{mod_id}/versions | Fetch all available versions for a mod
[**permit_mod_team**](ModApi.md#permit_mod_team) | **PUT** /mods/{mod_id}/teams | Update team perms for mod
[**permit_mod_user**](ModApi.md#permit_mod_user) | **PUT** /mods/{mod_id}/users | Update user perms for mod
[**show_mod**](ModApi.md#show_mod) | **GET** /mods/{mod_id} | Fetch a specific mod
[**show_version**](ModApi.md#show_version) | **GET** /mods/{mod_id}/versions/{version_id} | Fetch a specific version for a mod
[**update_mod**](ModApi.md#update_mod) | **PUT** /mods/{mod_id} | Update a specific mod
[**update_version**](ModApi.md#update_version) | **PUT** /mods/{mod_id}/versions/{version_id} | Update a specific version for a mod


# **append_mod_to_team**
> GeneralError append_mod_to_team(mod_id, params)

Assign a team to mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
params = kleister.ModTeamParams() # ModTeamParams | The mod team data to assign

try:
    # Assign a team to mod
    api_response = api_instance.append_mod_to_team(mod_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->append_mod_to_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **params** | [**ModTeamParams**](ModTeamParams.md)| The mod team data to assign | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_mod_to_user**
> GeneralError append_mod_to_user(mod_id, params)

Assign a user to mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
params = kleister.ModUserParams() # ModUserParams | The mod user data to assign

try:
    # Assign a user to mod
    api_response = api_instance.append_mod_to_user(mod_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->append_mod_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **params** | [**ModUserParams**](ModUserParams.md)| The mod user data to assign | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_version_to_build**
> GeneralError append_version_to_build(mod_id, version_id, params)

Assign a build to a version

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
version_id = 'version_id_example' # str | A version UUID or slug
params = kleister.VersionBuildParams() # VersionBuildParams | The build data to append to version

try:
    # Assign a build to a version
    api_response = api_instance.append_version_to_build(mod_id, version_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->append_version_to_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **version_id** | **str**| A version UUID or slug | 
 **params** | [**VersionBuildParams**](VersionBuildParams.md)| The build data to append to version | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mod**
> Mod create_mod(params)

Create a new mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
params = kleister.Mod() # Mod | The mod data to create

try:
    # Create a new mod
    api_response = api_instance.create_mod(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->create_mod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**Mod**](Mod.md)| The mod data to create | 

### Return type

[**Mod**](Mod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_version**
> Version create_version(mod_id, params)

Create a new version for a mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
params = kleister.Version() # Version | The version data to create

try:
    # Create a new version for a mod
    api_response = api_instance.create_version(mod_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->create_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **params** | [**Version**](Version.md)| The version data to create | 

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mod**
> GeneralError delete_mod(mod_id)

Delete a specific mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug

try:
    # Delete a specific mod
    api_response = api_instance.delete_mod(mod_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->delete_mod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mod_from_team**
> GeneralError delete_mod_from_team(mod_id, params)

Remove a team from mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
params = kleister.ModTeamParams() # ModTeamParams | The mod team data to delete

try:
    # Remove a team from mod
    api_response = api_instance.delete_mod_from_team(mod_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->delete_mod_from_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **params** | [**ModTeamParams**](ModTeamParams.md)| The mod team data to delete | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mod_from_user**
> GeneralError delete_mod_from_user(mod_id, params)

Remove a user from mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
params = kleister.ModUserParams() # ModUserParams | The mod user data to delete

try:
    # Remove a user from mod
    api_response = api_instance.delete_mod_from_user(mod_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->delete_mod_from_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **params** | [**ModUserParams**](ModUserParams.md)| The mod user data to delete | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version**
> GeneralError delete_version(mod_id, version_id)

Delete a specific version for a mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
version_id = 'version_id_example' # str | A version UUID or slug

try:
    # Delete a specific version for a mod
    api_response = api_instance.delete_version(mod_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->delete_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **version_id** | **str**| A version UUID or slug | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_version_from_build**
> GeneralError delete_version_from_build(mod_id, version_id, params)

Unlink a build from a version

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
version_id = 'version_id_example' # str | A version UUID or slug
params = kleister.VersionBuildParams() # VersionBuildParams | The build data to unlink from version

try:
    # Unlink a build from a version
    api_response = api_instance.delete_version_from_build(mod_id, version_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->delete_version_from_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **version_id** | **str**| A version UUID or slug | 
 **params** | [**VersionBuildParams**](VersionBuildParams.md)| The build data to unlink from version | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mod_teams**
> list[TeamMod] list_mod_teams(mod_id)

Fetch all teams assigned to mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug

try:
    # Fetch all teams assigned to mod
    api_response = api_instance.list_mod_teams(mod_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->list_mod_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 

### Return type

[**list[TeamMod]**](TeamMod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mod_users**
> list[UserMod] list_mod_users(mod_id)

Fetch all users assigned to mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug

try:
    # Fetch all users assigned to mod
    api_response = api_instance.list_mod_users(mod_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->list_mod_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 

### Return type

[**list[UserMod]**](UserMod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mods**
> list[Mod] list_mods()

Fetch all available mods

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()

try:
    # Fetch all available mods
    api_response = api_instance.list_mods()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->list_mods: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Mod]**](Mod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_version_builds**
> list[BuildVersion] list_version_builds(mod_id, version_id)

Fetch all builds assigned to version

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
version_id = 'version_id_example' # str | A version UUID or slug

try:
    # Fetch all builds assigned to version
    api_response = api_instance.list_version_builds(mod_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->list_version_builds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **version_id** | **str**| A version UUID or slug | 

### Return type

[**list[BuildVersion]**](BuildVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versions**
> list[Version] list_versions(mod_id)

Fetch all available versions for a mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug

try:
    # Fetch all available versions for a mod
    api_response = api_instance.list_versions(mod_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->list_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 

### Return type

[**list[Version]**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_mod_team**
> GeneralError permit_mod_team(mod_id, params)

Update team perms for mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
params = kleister.ModTeamParams() # ModTeamParams | The mod team data to update

try:
    # Update team perms for mod
    api_response = api_instance.permit_mod_team(mod_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->permit_mod_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **params** | [**ModTeamParams**](ModTeamParams.md)| The mod team data to update | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_mod_user**
> GeneralError permit_mod_user(mod_id, params)

Update user perms for mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
params = kleister.ModUserParams() # ModUserParams | The mod user data to update

try:
    # Update user perms for mod
    api_response = api_instance.permit_mod_user(mod_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->permit_mod_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **params** | [**ModUserParams**](ModUserParams.md)| The mod user data to update | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_mod**
> Mod show_mod(mod_id)

Fetch a specific mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug

try:
    # Fetch a specific mod
    api_response = api_instance.show_mod(mod_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->show_mod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 

### Return type

[**Mod**](Mod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_version**
> Version show_version(mod_id, version_id)

Fetch a specific version for a mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
version_id = 'version_id_example' # str | A version UUID or slug

try:
    # Fetch a specific version for a mod
    api_response = api_instance.show_version(mod_id, version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->show_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **version_id** | **str**| A version UUID or slug | 

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mod**
> Mod update_mod(mod_id, params)

Update a specific mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
params = kleister.Mod() # Mod | The mod data to update

try:
    # Update a specific mod
    api_response = api_instance.update_mod(mod_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->update_mod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **params** | [**Mod**](Mod.md)| The mod data to update | 

### Return type

[**Mod**](Mod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version**
> Version update_version(mod_id, version_id, params)

Update a specific version for a mod

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.ModApi()
mod_id = 'mod_id_example' # str | A mod UUID or slug
version_id = 'version_id_example' # str | A version UUID or slug
params = kleister.Version() # Version | The version data to update

try:
    # Update a specific version for a mod
    api_response = api_instance.update_version(mod_id, version_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModApi->update_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mod_id** | **str**| A mod UUID or slug | 
 **version_id** | **str**| A version UUID or slug | 
 **params** | [**Version**](Version.md)| The version data to update | 

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

