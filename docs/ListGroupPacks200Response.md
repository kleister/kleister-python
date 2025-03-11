# ListGroupPacks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**group** | [**Group**](Group.md) |  | [optional] 
**packs** | [**List[GroupPack]**](GroupPack.md) |  | 

## Example

```python
from kleister.models.list_group_packs200_response import ListGroupPacks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListGroupPacks200Response from a JSON string
list_group_packs200_response_instance = ListGroupPacks200Response.from_json(json)
# print the JSON string representation of the object
print(ListGroupPacks200Response.to_json())

# convert the object into a dict
list_group_packs200_response_dict = list_group_packs200_response_instance.to_dict()
# create an instance of ListGroupPacks200Response from a dict
list_group_packs200_response_from_dict = ListGroupPacks200Response.from_dict(list_group_packs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


