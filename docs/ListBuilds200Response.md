# ListBuilds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**builds** | [**List[Build]**](Build.md) |  | 

## Example

```python
from kleister.models.list_builds200_response import ListBuilds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListBuilds200Response from a JSON string
list_builds200_response_instance = ListBuilds200Response.from_json(json)
# print the JSON string representation of the object
print(ListBuilds200Response.to_json())

# convert the object into a dict
list_builds200_response_dict = list_builds200_response_instance.to_dict()
# create an instance of ListBuilds200Response from a dict
list_builds200_response_from_dict = ListBuilds200Response.from_dict(list_builds200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


