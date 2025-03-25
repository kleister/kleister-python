# ListMods200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**mods** | [**List[Mod]**](Mod.md) |  | 

## Example

```python
from kleister.models.list_mods200_response import ListMods200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMods200Response from a JSON string
list_mods200_response_instance = ListMods200Response.from_json(json)
# print the JSON string representation of the object
print(ListMods200Response.to_json())

# convert the object into a dict
list_mods200_response_dict = list_mods200_response_instance.to_dict()
# create an instance of ListMods200Response from a dict
list_mods200_response_from_dict = ListMods200Response.from_dict(list_mods200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


