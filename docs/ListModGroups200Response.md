# ListModGroups200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**mod** | [**Mod**](Mod.md) |  | [optional] 
**groups** | [**List[GroupMod]**](GroupMod.md) |  | 

## Example

```python
from kleister.models.list_mod_groups200_response import ListModGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListModGroups200Response from a JSON string
list_mod_groups200_response_instance = ListModGroups200Response.from_json(json)
# print the JSON string representation of the object
print(ListModGroups200Response.to_json())

# convert the object into a dict
list_mod_groups200_response_dict = list_mod_groups200_response_instance.to_dict()
# create an instance of ListModGroups200Response from a dict
list_mod_groups200_response_from_dict = ListModGroups200Response.from_dict(list_mod_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


