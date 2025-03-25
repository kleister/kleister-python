# ListPackGroups200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**groups** | [**List[GroupPack]**](GroupPack.md) |  | 

## Example

```python
from kleister.models.list_pack_groups200_response import ListPackGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPackGroups200Response from a JSON string
list_pack_groups200_response_instance = ListPackGroups200Response.from_json(json)
# print the JSON string representation of the object
print(ListPackGroups200Response.to_json())

# convert the object into a dict
list_pack_groups200_response_dict = list_pack_groups200_response_instance.to_dict()
# create an instance of ListPackGroups200Response from a dict
list_pack_groups200_response_from_dict = ListPackGroups200Response.from_dict(list_pack_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


