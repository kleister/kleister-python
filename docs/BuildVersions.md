# BuildVersions

Model to represent build versions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | [**Pack**](Pack.md) |  | [optional] 
**build** | [**Build**](Build.md) |  | [optional] 
**total** | **int** |  | [optional] 
**versions** | [**List[BuildVersion]**](BuildVersion.md) |  | [optional] 

## Example

```python
from kleister.models.build_versions import BuildVersions

# TODO update the JSON string below
json = "{}"
# create an instance of BuildVersions from a JSON string
build_versions_instance = BuildVersions.from_json(json)
# print the JSON string representation of the object
print(BuildVersions.to_json())

# convert the object into a dict
build_versions_dict = build_versions_instance.to_dict()
# create an instance of BuildVersions from a dict
build_versions_from_dict = BuildVersions.from_dict(build_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


