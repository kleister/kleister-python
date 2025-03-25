# ListModUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**mod** | [**Mod**](Mod.md) |  | [optional] 
**users** | [**List[UserMod]**](UserMod.md) |  | 

## Example

```python
from kleister.models.list_mod_users200_response import ListModUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListModUsers200Response from a JSON string
list_mod_users200_response_instance = ListModUsers200Response.from_json(json)
# print the JSON string representation of the object
print(ListModUsers200Response.to_json())

# convert the object into a dict
list_mod_users200_response_dict = list_mod_users200_response_instance.to_dict()
# create an instance of ListModUsers200Response from a dict
list_mod_users200_response_from_dict = ListModUsers200Response.from_dict(list_mod_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


