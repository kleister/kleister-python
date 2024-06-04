# FabricBuilds

Model to represent fabric builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fabric** | [**Fabric**](Fabric.md) |  | [optional] 
**total** | **int** |  | [optional] 
**builds** | [**List[Build]**](Build.md) |  | [optional] 

## Example

```python
from kleister.models.fabric_builds import FabricBuilds

# TODO update the JSON string below
json = "{}"
# create an instance of FabricBuilds from a JSON string
fabric_builds_instance = FabricBuilds.from_json(json)
# print the JSON string representation of the object
print(FabricBuilds.to_json())

# convert the object into a dict
fabric_builds_dict = fabric_builds_instance.to_dict()
# create an instance of FabricBuilds from a dict
fabric_builds_from_dict = FabricBuilds.from_dict(fabric_builds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


