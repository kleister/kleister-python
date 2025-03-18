# ListUserMods200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**user** | [**User**](User.md) |  | [optional] 
**mods** | [**List[UserMod]**](UserMod.md) |  | 

## Example

```python
from kleister.models.list_user_mods200_response import ListUserMods200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserMods200Response from a JSON string
list_user_mods200_response_instance = ListUserMods200Response.from_json(json)
# print the JSON string representation of the object
print(ListUserMods200Response.to_json())

# convert the object into a dict
list_user_mods200_response_dict = list_user_mods200_response_instance.to_dict()
# create an instance of ListUserMods200Response from a dict
list_user_mods200_response_from_dict = ListUserMods200Response.from_dict(list_user_mods200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


