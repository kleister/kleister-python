# kleister.TeamApi

All URIs are relative to *http://http:/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_team_to_mod**](TeamApi.md#append_team_to_mod) | **POST** /teams/{team_id}/mods | Assign a mod to team
[**append_team_to_pack**](TeamApi.md#append_team_to_pack) | **POST** /teams/{team_id}/packs | Assign a pack to team
[**append_team_to_user**](TeamApi.md#append_team_to_user) | **POST** /teams/{team_id}/users | Assign a user to team
[**create_team**](TeamApi.md#create_team) | **POST** /teams | Create a new team
[**delete_team**](TeamApi.md#delete_team) | **DELETE** /teams/{team_id} | Delete a specific team
[**delete_team_from_mod**](TeamApi.md#delete_team_from_mod) | **DELETE** /teams/{team_id}/mods | Remove a mod from team
[**delete_team_from_pack**](TeamApi.md#delete_team_from_pack) | **DELETE** /teams/{team_id}/packs | Remove a pack from team
[**delete_team_from_user**](TeamApi.md#delete_team_from_user) | **DELETE** /teams/{team_id}/users | Remove a user from team
[**list_team_mods**](TeamApi.md#list_team_mods) | **GET** /teams/{team_id}/mods | Fetch all mods assigned to team
[**list_team_packs**](TeamApi.md#list_team_packs) | **GET** /teams/{team_id}/packs | Fetch all packs assigned to team
[**list_team_users**](TeamApi.md#list_team_users) | **GET** /teams/{team_id}/users | Fetch all users assigned to team
[**list_teams**](TeamApi.md#list_teams) | **GET** /teams | Fetch all available teams
[**permit_team_mod**](TeamApi.md#permit_team_mod) | **PUT** /teams/{team_id}/mods | Update mod perms for team
[**permit_team_pack**](TeamApi.md#permit_team_pack) | **PUT** /teams/{team_id}/packs | Update pack perms for team
[**permit_team_user**](TeamApi.md#permit_team_user) | **PUT** /teams/{team_id}/users | Update user perms for team
[**show_team**](TeamApi.md#show_team) | **GET** /teams/{team_id} | Fetch a specific team
[**update_team**](TeamApi.md#update_team) | **PUT** /teams/{team_id} | Update a specific team


# **append_team_to_mod**
> object append_team_to_mod(team_id, params)

Assign a mod to team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
params = kleister.TeamModParams() # TeamModParams | The team mod data to assign

try:
    # Assign a mod to team
    api_response = api_instance.append_team_to_mod(team_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->append_team_to_mod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **params** | [**TeamModParams**](TeamModParams.md)| The team mod data to assign | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_team_to_pack**
> object append_team_to_pack(team_id, params)

Assign a pack to team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
params = kleister.TeamPackParams() # TeamPackParams | The team pack data to assign

try:
    # Assign a pack to team
    api_response = api_instance.append_team_to_pack(team_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->append_team_to_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **params** | [**TeamPackParams**](TeamPackParams.md)| The team pack data to assign | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_team_to_user**
> object append_team_to_user(team_id, params)

Assign a user to team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
params = kleister.TeamUserParams() # TeamUserParams | The team user data to assign

try:
    # Assign a user to team
    api_response = api_instance.append_team_to_user(team_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->append_team_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **params** | [**TeamUserParams**](TeamUserParams.md)| The team user data to assign | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team**
> Team create_team(params)

Create a new team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
params = kleister.Team() # Team | The team data to create

try:
    # Create a new team
    api_response = api_instance.create_team(params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **params** | [**Team**](Team.md)| The team data to create | 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> object delete_team(team_id)

Delete a specific team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug

try:
    # Delete a specific team
    api_response = api_instance.delete_team(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_from_mod**
> object delete_team_from_mod(team_id, params)

Remove a mod from team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
params = kleister.TeamModParams() # TeamModParams | The team mod data to delete

try:
    # Remove a mod from team
    api_response = api_instance.delete_team_from_mod(team_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->delete_team_from_mod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **params** | [**TeamModParams**](TeamModParams.md)| The team mod data to delete | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_from_pack**
> object delete_team_from_pack(team_id, params)

Remove a pack from team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
params = kleister.TeamPackParams() # TeamPackParams | The team pack data to delete

try:
    # Remove a pack from team
    api_response = api_instance.delete_team_from_pack(team_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->delete_team_from_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **params** | [**TeamPackParams**](TeamPackParams.md)| The team pack data to delete | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_from_user**
> object delete_team_from_user(team_id, params)

Remove a user from team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
params = kleister.TeamUserParams() # TeamUserParams | The team user data to delete

try:
    # Remove a user from team
    api_response = api_instance.delete_team_from_user(team_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->delete_team_from_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **params** | [**TeamUserParams**](TeamUserParams.md)| The team user data to delete | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_mods**
> list[TeamMod] list_team_mods(team_id)

Fetch all mods assigned to team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug

try:
    # Fetch all mods assigned to team
    api_response = api_instance.list_team_mods(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->list_team_mods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 

### Return type

[**list[TeamMod]**](TeamMod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_packs**
> list[TeamPack] list_team_packs(team_id)

Fetch all packs assigned to team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug

try:
    # Fetch all packs assigned to team
    api_response = api_instance.list_team_packs(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->list_team_packs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 

### Return type

[**list[TeamPack]**](TeamPack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_users**
> list[TeamUser] list_team_users(team_id)

Fetch all users assigned to team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug

try:
    # Fetch all users assigned to team
    api_response = api_instance.list_team_users(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->list_team_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 

### Return type

[**list[TeamUser]**](TeamUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_teams**
> list[Team] list_teams()

Fetch all available teams

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()

try:
    # Fetch all available teams
    api_response = api_instance.list_teams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->list_teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_team_mod**
> object permit_team_mod(team_id, params)

Update mod perms for team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
params = kleister.TeamModParams() # TeamModParams | The team mod data to update

try:
    # Update mod perms for team
    api_response = api_instance.permit_team_mod(team_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->permit_team_mod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **params** | [**TeamModParams**](TeamModParams.md)| The team mod data to update | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_team_pack**
> object permit_team_pack(team_id, params)

Update pack perms for team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
params = kleister.TeamPackParams() # TeamPackParams | The team pack data to update

try:
    # Update pack perms for team
    api_response = api_instance.permit_team_pack(team_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->permit_team_pack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **params** | [**TeamPackParams**](TeamPackParams.md)| The team pack data to update | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_team_user**
> object permit_team_user(team_id, params)

Update user perms for team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
params = kleister.TeamUserParams() # TeamUserParams | The team user data to update

try:
    # Update user perms for team
    api_response = api_instance.permit_team_user(team_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->permit_team_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **params** | [**TeamUserParams**](TeamUserParams.md)| The team user data to update | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_team**
> Team show_team(team_id)

Fetch a specific team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug

try:
    # Fetch a specific team
    api_response = api_instance.show_team(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->show_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> Team update_team(team_id, params)

Update a specific team

### Example

```python
from __future__ import print_function
import time
import kleister
from kleister.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kleister.TeamApi()
team_id = 'team_id_example' # str | A team UUID or slug
params = kleister.Team() # Team | The team data to update

try:
    # Update a specific team
    api_response = api_instance.update_team(team_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug | 
 **params** | [**Team**](Team.md)| The team data to update | 

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

