# ListGroupMods200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**group** | [**Group**](Group.md) |  | [optional] 
**mods** | [**List[GroupMod]**](GroupMod.md) |  | 

## Example

```python
from kleister.models.list_group_mods200_response import ListGroupMods200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListGroupMods200Response from a JSON string
list_group_mods200_response_instance = ListGroupMods200Response.from_json(json)
# print the JSON string representation of the object
print(ListGroupMods200Response.to_json())

# convert the object into a dict
list_group_mods200_response_dict = list_group_mods200_response_instance.to_dict()
# create an instance of ListGroupMods200Response from a dict
list_group_mods200_response_from_dict = ListGroupMods200Response.from_dict(list_group_mods200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


