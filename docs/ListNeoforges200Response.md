# ListNeoforges200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**versions** | [**List[Neoforge]**](Neoforge.md) |  | 

## Example

```python
from kleister.models.list_neoforges200_response import ListNeoforges200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListNeoforges200Response from a JSON string
list_neoforges200_response_instance = ListNeoforges200Response.from_json(json)
# print the JSON string representation of the object
print(ListNeoforges200Response.to_json())

# convert the object into a dict
list_neoforges200_response_dict = list_neoforges200_response_instance.to_dict()
# create an instance of ListNeoforges200Response from a dict
list_neoforges200_response_from_dict = ListNeoforges200Response.from_dict(list_neoforges200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


