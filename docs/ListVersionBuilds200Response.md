# ListVersionBuilds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**mod** | [**Mod**](Mod.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**builds** | [**List[BuildVersion]**](BuildVersion.md) |  | 

## Example

```python
from kleister.models.list_version_builds200_response import ListVersionBuilds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListVersionBuilds200Response from a JSON string
list_version_builds200_response_instance = ListVersionBuilds200Response.from_json(json)
# print the JSON string representation of the object
print(ListVersionBuilds200Response.to_json())

# convert the object into a dict
list_version_builds200_response_dict = list_version_builds200_response_instance.to_dict()
# create an instance of ListVersionBuilds200Response from a dict
list_version_builds200_response_from_dict = ListVersionBuilds200Response.from_dict(list_version_builds200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


