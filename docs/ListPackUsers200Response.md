# ListPackUsers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**users** | [**List[UserPack]**](UserPack.md) |  | 

## Example

```python
from kleister.models.list_pack_users200_response import ListPackUsers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPackUsers200Response from a JSON string
list_pack_users200_response_instance = ListPackUsers200Response.from_json(json)
# print the JSON string representation of the object
print(ListPackUsers200Response.to_json())

# convert the object into a dict
list_pack_users200_response_dict = list_pack_users200_response_instance.to_dict()
# create an instance of ListPackUsers200Response from a dict
list_pack_users200_response_from_dict = ListPackUsers200Response.from_dict(list_pack_users200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


