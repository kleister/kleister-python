# ListPacks200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**packs** | [**List[Pack]**](Pack.md) |  | 

## Example

```python
from kleister.models.list_packs200_response import ListPacks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPacks200Response from a JSON string
list_packs200_response_instance = ListPacks200Response.from_json(json)
# print the JSON string representation of the object
print(ListPacks200Response.to_json())

# convert the object into a dict
list_packs200_response_dict = list_packs200_response_instance.to_dict()
# create an instance of ListPacks200Response from a dict
list_packs200_response_from_dict = ListPacks200Response.from_dict(list_packs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


