# NeoforgeBuilds

Model to represent neoforge builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neoforge** | [**Neoforge**](Neoforge.md) |  | [optional] 
**total** | **int** |  | [optional] 
**builds** | [**List[Build]**](Build.md) |  | [optional] 

## Example

```python
from kleister.models.neoforge_builds import NeoforgeBuilds

# TODO update the JSON string below
json = "{}"
# create an instance of NeoforgeBuilds from a JSON string
neoforge_builds_instance = NeoforgeBuilds.from_json(json)
# print the JSON string representation of the object
print(NeoforgeBuilds.to_json())

# convert the object into a dict
neoforge_builds_dict = neoforge_builds_instance.to_dict()
# create an instance of NeoforgeBuilds from a dict
neoforge_builds_from_dict = NeoforgeBuilds.from_dict(neoforge_builds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


