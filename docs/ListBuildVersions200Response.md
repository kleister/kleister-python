# ListBuildVersions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**build** | [**Build**](Build.md) |  | [optional] 
**versions** | [**List[BuildVersion]**](BuildVersion.md) |  | 

## Example

```python
from kleister.models.list_build_versions200_response import ListBuildVersions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListBuildVersions200Response from a JSON string
list_build_versions200_response_instance = ListBuildVersions200Response.from_json(json)
# print the JSON string representation of the object
print(ListBuildVersions200Response.to_json())

# convert the object into a dict
list_build_versions200_response_dict = list_build_versions200_response_instance.to_dict()
# create an instance of ListBuildVersions200Response from a dict
list_build_versions200_response_from_dict = ListBuildVersions200Response.from_dict(list_build_versions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


