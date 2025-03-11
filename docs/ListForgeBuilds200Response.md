# ListForgeBuilds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**forge** | [**Forge**](Forge.md) |  | [optional] 
**builds** | [**List[Build]**](Build.md) |  | 

## Example

```python
from kleister.models.list_forge_builds200_response import ListForgeBuilds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListForgeBuilds200Response from a JSON string
list_forge_builds200_response_instance = ListForgeBuilds200Response.from_json(json)
# print the JSON string representation of the object
print(ListForgeBuilds200Response.to_json())

# convert the object into a dict
list_forge_builds200_response_dict = list_forge_builds200_response_instance.to_dict()
# create an instance of ListForgeBuilds200Response from a dict
list_forge_builds200_response_from_dict = ListForgeBuilds200Response.from_dict(list_forge_builds200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


