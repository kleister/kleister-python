# BuildVersion

Model to represent build version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_id** | **str** |  | 
**build** | [**Build**](Build.md) |  | [optional] 
**version_id** | **str** |  | 
**version** | [**Version**](Version.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.build_version import BuildVersion

# TODO update the JSON string below
json = "{}"
# create an instance of BuildVersion from a JSON string
build_version_instance = BuildVersion.from_json(json)
# print the JSON string representation of the object
print(BuildVersion.to_json())

# convert the object into a dict
build_version_dict = build_version_instance.to_dict()
# create an instance of BuildVersion from a dict
build_version_from_dict = BuildVersion.from_dict(build_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


