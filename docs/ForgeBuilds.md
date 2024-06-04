# ForgeBuilds

Model to represent forge builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forge** | [**Forge**](Forge.md) |  | [optional] 
**total** | **int** |  | [optional] 
**builds** | [**List[Build]**](Build.md) |  | [optional] 

## Example

```python
from kleister.models.forge_builds import ForgeBuilds

# TODO update the JSON string below
json = "{}"
# create an instance of ForgeBuilds from a JSON string
forge_builds_instance = ForgeBuilds.from_json(json)
# print the JSON string representation of the object
print(ForgeBuilds.to_json())

# convert the object into a dict
forge_builds_dict = forge_builds_instance.to_dict()
# create an instance of ForgeBuilds from a dict
forge_builds_from_dict = ForgeBuilds.from_dict(forge_builds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


