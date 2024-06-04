# VersionBuilds

Model to represent version builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mod** | [**Mod**](Mod.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**total** | **int** |  | [optional] 
**builds** | [**List[BuildVersion]**](BuildVersion.md) |  | [optional] 

## Example

```python
from kleister.models.version_builds import VersionBuilds

# TODO update the JSON string below
json = "{}"
# create an instance of VersionBuilds from a JSON string
version_builds_instance = VersionBuilds.from_json(json)
# print the JSON string representation of the object
print(VersionBuilds.to_json())

# convert the object into a dict
version_builds_dict = version_builds_instance.to_dict()
# create an instance of VersionBuilds from a dict
version_builds_from_dict = VersionBuilds.from_dict(version_builds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


