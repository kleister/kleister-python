# Versions

Model to represent list of versions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**mod** | [**Mod**](Mod.md) |  | [optional] 
**versions** | [**List[Version]**](Version.md) |  | [optional] 

## Example

```python
from kleister.models.versions import Versions

# TODO update the JSON string below
json = "{}"
# create an instance of Versions from a JSON string
versions_instance = Versions.from_json(json)
# print the JSON string representation of the object
print(Versions.to_json())

# convert the object into a dict
versions_dict = versions_instance.to_dict()
# create an instance of Versions from a dict
versions_from_dict = Versions.from_dict(versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


