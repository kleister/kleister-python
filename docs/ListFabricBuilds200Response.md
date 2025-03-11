# ListFabricBuilds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**fabric** | [**Fabric**](Fabric.md) |  | [optional] 
**builds** | [**List[Build]**](Build.md) |  | 

## Example

```python
from kleister.models.list_fabric_builds200_response import ListFabricBuilds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListFabricBuilds200Response from a JSON string
list_fabric_builds200_response_instance = ListFabricBuilds200Response.from_json(json)
# print the JSON string representation of the object
print(ListFabricBuilds200Response.to_json())

# convert the object into a dict
list_fabric_builds200_response_dict = list_fabric_builds200_response_instance.to_dict()
# create an instance of ListFabricBuilds200Response from a dict
list_fabric_builds200_response_from_dict = ListFabricBuilds200Response.from_dict(list_fabric_builds200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


