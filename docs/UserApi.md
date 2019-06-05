# kleister.UserApi

All URIs are relative to *http://try.kleister.tech/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_user_to_mod**](UserApi.md#append_user_to_mod) | **POST** /users/{user_id}/mods | Assign a mod to user
[**append_user_to_pack**](UserApi.md#append_user_to_pack) | **POST** /users/{user_id}/packs | Assign a pack to user
[**append_user_to_team**](UserApi.md#append_user_to_team) | **POST** /users/{user_id}/teams | Assign a team to user
[**create_user**](UserApi.md#create_user) | **POST** /users | Create a new user
[**delete_user**](UserApi.md#delete_user) | **DELETE** /users/{user_id} | Delete a specific user
[**delete_user_from_mod**](UserApi.md#delete_user_from_mod) | **DELETE** /users/{user_id}/mods | Remove a mod from user
[**delete_user_from_pack**](UserApi.md#delete_user_from_pack) | **DELETE** /users/{user_id}/packs | Remove a pack from user
[**delete_user_from_team**](UserApi.md#delete_user_from_team) | **DELETE** /users/{user_id}/teams | Remove a team from user
[**list_user_mods**](UserApi.md#list_user_mods) | **GET** /users/{user_id}/mods | Fetch all mods assigned to user
[**list_user_packs**](UserApi.md#list_user_packs) | **GET** /users/{user_id}/packs | Fetch all packs assigned to user
[**list_user_teams**](UserApi.md#list_user_teams) | **GET** /users/{user_id}/teams | Fetch all teams assigned to user
[**list_users**](UserApi.md#list_users) | **GET** /users | Fetch all available users
[**permit_user_mod**](UserApi.md#permit_user_mod) | **PUT** /users/{user_id}/mods | Update mod perms for user
[**permit_user_pack**](UserApi.md#permit_user_pack) | **PUT** /users/{user_id}/packs | Update pack perms for user
[**permit_user_team**](UserApi.md#permit_user_team) | **PUT** /users/{user_id}/teams | Update team perms for user
[**show_user**](UserApi.md#show_user) | **GET** /users/{user_id} | Fetch a specific user
[**update_user**](UserApi.md#update_user) | **PUT** /users/{user_id} | Update a specific user


# **append_user_to_mod**
> GeneralError append_user_to_mod(user_id, params)

Assign a mod to user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
params = kleister.UserModParams() # UserModParams | The user mod data to assign

try:
    # Assign a mod to user
    api_response = api_instance.append_user_to_mod(user_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->append_user_to_mod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 
 **params** | [**UserModParams**](UserModParams.md)| The user mod data to assign | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_user_to_pack**
> GeneralError append_user_to_pack(user_id, params)

Assign a pack to user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
params = kleister.UserPackParams() # UserPackParams | The user pack data to assign

try:
    # Assign a pack to user
    api_response = api_instance.append_user_to_pack(user_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->append_user_to_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 
 **params** | [**UserPackParams**](UserPackParams.md)| The user pack data to assign | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_user_to_team**
> GeneralError append_user_to_team(user_id, params)

Assign a team to user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
params = kleister.UserTeamParams() # UserTeamParams | The user team data to assign

try:
    # Assign a team to user
    api_response = api_instance.append_user_to_team(user_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->append_user_to_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 
 **params** | [**UserTeamParams**](UserTeamParams.md)| The user team data to assign | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(params)

Create a new user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
params = kleister.User() # User | The user data to create

try:
    # Create a new user
    api_response = api_instance.create_user(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**User**](User.md)| The user data to create | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> GeneralError delete_user(user_id)

Delete a specific user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug

try:
    # Delete a specific user
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_mod**
> GeneralError delete_user_from_mod(user_id, params)

Remove a mod from user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
params = kleister.UserModParams() # UserModParams | The user mod data to delete

try:
    # Remove a mod from user
    api_response = api_instance.delete_user_from_mod(user_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_from_mod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 
 **params** | [**UserModParams**](UserModParams.md)| The user mod data to delete | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_pack**
> GeneralError delete_user_from_pack(user_id, params)

Remove a pack from user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
params = kleister.UserPackParams() # UserPackParams | The user pack data to delete

try:
    # Remove a pack from user
    api_response = api_instance.delete_user_from_pack(user_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_from_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 
 **params** | [**UserPackParams**](UserPackParams.md)| The user pack data to delete | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_from_team**
> GeneralError delete_user_from_team(user_id, params)

Remove a team from user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
params = kleister.UserTeamParams() # UserTeamParams | The user team data to delete

try:
    # Remove a team from user
    api_response = api_instance.delete_user_from_team(user_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->delete_user_from_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 
 **params** | [**UserTeamParams**](UserTeamParams.md)| The user team data to delete | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_mods**
> list[UserMod] list_user_mods(user_id)

Fetch all mods assigned to user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug

try:
    # Fetch all mods assigned to user
    api_response = api_instance.list_user_mods(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_mods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 

### Return type

[**list[UserMod]**](UserMod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_packs**
> list[UserPack] list_user_packs(user_id)

Fetch all packs assigned to user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug

try:
    # Fetch all packs assigned to user
    api_response = api_instance.list_user_packs(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_packs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 

### Return type

[**list[UserPack]**](UserPack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_teams**
> list[TeamUser] list_user_teams(user_id)

Fetch all teams assigned to user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug

try:
    # Fetch all teams assigned to user
    api_response = api_instance.list_user_teams(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_user_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 

### Return type

[**list[TeamUser]**](TeamUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> list[User] list_users()

Fetch all available users

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()

try:
    # Fetch all available users
    api_response = api_instance.list_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_user_mod**
> GeneralError permit_user_mod(user_id, params)

Update mod perms for user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
params = kleister.UserModParams() # UserModParams | The user mod data to update

try:
    # Update mod perms for user
    api_response = api_instance.permit_user_mod(user_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->permit_user_mod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 
 **params** | [**UserModParams**](UserModParams.md)| The user mod data to update | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_user_pack**
> GeneralError permit_user_pack(user_id, params)

Update pack perms for user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
params = kleister.UserPackParams() # UserPackParams | The user pack data to update

try:
    # Update pack perms for user
    api_response = api_instance.permit_user_pack(user_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->permit_user_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 
 **params** | [**UserPackParams**](UserPackParams.md)| The user pack data to update | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_user_team**
> GeneralError permit_user_team(user_id, params)

Update team perms for user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
params = kleister.UserTeamParams() # UserTeamParams | The user team data to update

try:
    # Update team perms for user
    api_response = api_instance.permit_user_team(user_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->permit_user_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 
 **params** | [**UserTeamParams**](UserTeamParams.md)| The user team data to update | 

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_user**
> User show_user(user_id)

Fetch a specific user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug

try:
    # Fetch a specific user
    api_response = api_instance.show_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->show_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, params)

Update a specific user

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.UserApi()
user_id = 'user_id_example' # str | A user UUID or slug
params = kleister.User() # User | The user data to update

try:
    # Update a specific user
    api_response = api_instance.update_user(user_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| A user UUID or slug | 
 **params** | [**User**](User.md)| The user data to update | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

