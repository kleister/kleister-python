# ListForges200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**versions** | [**List[Forge]**](Forge.md) |  | 

## Example

```python
from kleister.models.list_forges200_response import ListForges200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListForges200Response from a JSON string
list_forges200_response_instance = ListForges200Response.from_json(json)
# print the JSON string representation of the object
print(ListForges200Response.to_json())

# convert the object into a dict
list_forges200_response_dict = list_forges200_response_instance.to_dict()
# create an instance of ListForges200Response from a dict
list_forges200_response_from_dict = ListForges200Response.from_dict(list_forges200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


