# kleister.TeamApi

All URIs are relative to *http://try.kleister.tech/api/v1*

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
> GeneralError append_team_to_mod(team_id, team_mod)

Assign a mod to team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_mod_params import TeamModParams
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug
    team_mod = TeamModParams(
        mod="mod_example",
        perm="user",
    ) # TeamModParams | The team mod data to assign

    # example passing only required values which don't have defaults set
    try:
        # Assign a mod to team
        api_response = api_instance.append_team_to_mod(team_id, team_mod)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->append_team_to_mod: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |
 **team_mod** | [**TeamModParams**](TeamModParams.md)| The team mod data to assign |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Mod is already assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_team_to_pack**
> GeneralError append_team_to_pack(team_id, team_pack)

Assign a pack to team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_pack_params import TeamPackParams
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug
    team_pack = TeamPackParams(
        pack="pack_example",
        perm="user",
    ) # TeamPackParams | The team pack data to assign

    # example passing only required values which don't have defaults set
    try:
        # Assign a pack to team
        api_response = api_instance.append_team_to_pack(team_id, team_pack)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->append_team_to_pack: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |
 **team_pack** | [**TeamPackParams**](TeamPackParams.md)| The team pack data to assign |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Pack is already assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **append_team_to_user**
> GeneralError append_team_to_user(team_id, team_user)

Assign a user to team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_user_params import TeamUserParams
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug
    team_user = TeamUserParams(
        user="user_example",
        perm="user",
    ) # TeamUserParams | The team user data to assign

    # example passing only required values which don't have defaults set
    try:
        # Assign a user to team
        api_response = api_instance.append_team_to_user(team_id, team_user)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->append_team_to_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |
 **team_user** | [**TeamUserParams**](TeamUserParams.md)| The team user data to assign |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | User is already assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_team**
> Team create_team(team)

Create a new team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.validation_error import ValidationError
from kleister.model.team import Team
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team = Team(
        id="id_example",
        slug="slug_example",
        name="name_example",
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Team | The team data to create

    # example passing only required values which don't have defaults set
    try:
        # Create a new team
        api_response = api_instance.create_team(team)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->create_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | [**Team**](Team.md)| The team data to create |

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The created team data |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team**
> GeneralError delete_team(team_id)

Delete a specific team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Delete a specific team
        api_response = api_instance.delete_team(team_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->delete_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |

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
**400** | Failed to delete the team |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_from_mod**
> GeneralError delete_team_from_mod(team_id, team_mod)

Remove a mod from team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_mod_params import TeamModParams
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug
    team_mod = TeamModParams(
        mod="mod_example",
        perm="user",
    ) # TeamModParams | The team mod data to delete

    # example passing only required values which don't have defaults set
    try:
        # Remove a mod from team
        api_response = api_instance.delete_team_from_mod(team_id, team_mod)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->delete_team_from_mod: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |
 **team_mod** | [**TeamModParams**](TeamModParams.md)| The team mod data to delete |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Mod is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_from_pack**
> GeneralError delete_team_from_pack(team_id, team_pack)

Remove a pack from team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_pack_params import TeamPackParams
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug
    team_pack = TeamPackParams(
        pack="pack_example",
        perm="user",
    ) # TeamPackParams | The team pack data to delete

    # example passing only required values which don't have defaults set
    try:
        # Remove a pack from team
        api_response = api_instance.delete_team_from_pack(team_id, team_pack)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->delete_team_from_pack: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |
 **team_pack** | [**TeamPackParams**](TeamPackParams.md)| The team pack data to delete |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Pack is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_team_from_user**
> GeneralError delete_team_from_user(team_id, team_user)

Remove a user from team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_user_params import TeamUserParams
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug
    team_user = TeamUserParams(
        user="user_example",
        perm="user",
    ) # TeamUserParams | The team user data to delete

    # example passing only required values which don't have defaults set
    try:
        # Remove a user from team
        api_response = api_instance.delete_team_from_user(team_id, team_user)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->delete_team_from_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |
 **team_user** | [**TeamUserParams**](TeamUserParams.md)| The team user data to delete |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | User is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_mods**
> [TeamMod] list_team_mods(team_id)

Fetch all mods assigned to team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_mod import TeamMod
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all mods assigned to team
        api_response = api_instance.list_team_mods(team_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->list_team_mods: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |

### Return type

[**[TeamMod]**](TeamMod.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of team mods |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_packs**
> [TeamPack] list_team_packs(team_id)

Fetch all packs assigned to team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_pack import TeamPack
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all packs assigned to team
        api_response = api_instance.list_team_packs(team_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->list_team_packs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |

### Return type

[**[TeamPack]**](TeamPack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of team packs |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_team_users**
> [TeamUser] list_team_users(team_id)

Fetch all users assigned to team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_user import TeamUser
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch all users assigned to team
        api_response = api_instance.list_team_users(team_id)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->list_team_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |

### Return type

[**[TeamUser]**](TeamUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of team users |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_teams**
> [Team] list_teams()

Fetch all available teams

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team import Team
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch all available teams
        api_response = api_instance.list_teams()
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->list_teams: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of teams |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_team_mod**
> GeneralError permit_team_mod(team_id, team_mod)

Update mod perms for team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_mod_params import TeamModParams
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug
    team_mod = TeamModParams(
        mod="mod_example",
        perm="user",
    ) # TeamModParams | The team mod data to update

    # example passing only required values which don't have defaults set
    try:
        # Update mod perms for team
        api_response = api_instance.permit_team_mod(team_id, team_mod)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->permit_team_mod: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |
 **team_mod** | [**TeamModParams**](TeamModParams.md)| The team mod data to update |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Mod is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_team_pack**
> GeneralError permit_team_pack(team_id, team_pack)

Update pack perms for team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_pack_params import TeamPackParams
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug
    team_pack = TeamPackParams(
        pack="pack_example",
        perm="user",
    ) # TeamPackParams | The team pack data to update

    # example passing only required values which don't have defaults set
    try:
        # Update pack perms for team
        api_response = api_instance.permit_team_pack(team_id, team_pack)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->permit_team_pack: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |
 **team_pack** | [**TeamPackParams**](TeamPackParams.md)| The team pack data to update |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Pack is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permit_team_user**
> GeneralError permit_team_user(team_id, team_user)

Update user perms for team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team_user_params import TeamUserParams
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug
    team_user = TeamUserParams(
        user="user_example",
        perm="user",
    ) # TeamUserParams | The team user data to update

    # example passing only required values which don't have defaults set
    try:
        # Update user perms for team
        api_response = api_instance.permit_team_user(team_id, team_user)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->permit_team_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |
 **team_user** | [**TeamUserParams**](TeamUserParams.md)| The team user data to update |

### Return type

[**GeneralError**](GeneralError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plain success message |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | User is not assigned |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_team**
> Team show_team(team_id)

Fetch a specific team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.team import Team
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug

    # example passing only required values which don't have defaults set
    try:
        # Fetch a specific team
        api_response = api_instance.show_team(team_id)
        pprint(api_response)
    except kleister.ApiException as e:
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetched team details |  -  |
**403** | User is not authorized |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> Team update_team(team_id, team)

Update a specific team

### Example

```python
import time
import kleister
from kleister.api import team_api
from kleister.model.general_error import GeneralError
from kleister.model.validation_error import ValidationError
from kleister.model.team import Team
from pprint import pprint

configuration = kleister.Configuration(
    host = "http://try.kleister.tech/api/v1"
)


# Enter a context with an instance of the API client
with kleister.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = team_api.TeamApi(api_client)
    team_id = "team_id_example" # str | A team UUID or slug
    team = Team(
        id="id_example",
        slug="slug_example",
        name="name_example",
        created_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
        updated_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # Team | The team data to update

    # example passing only required values which don't have defaults set
    try:
        # Update a specific team
        api_response = api_instance.update_team(team_id, team)
        pprint(api_response)
    except kleister.ApiException as e:
        print("Exception when calling TeamApi->update_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| A team UUID or slug |
 **team** | [**Team**](Team.md)| The team data to update |

### Return type

[**Team**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated team details |  -  |
**403** | User is not authorized |  -  |
**412** | Failed to parse request body |  -  |
**422** | Failed to validate request |  -  |
**0** | Some error unrelated to the handler |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

