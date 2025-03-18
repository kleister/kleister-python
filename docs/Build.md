# Build

Model to represent build

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**minecraft_id** | **str** |  | [optional] 
**minecraft** | [**Minecraft**](Minecraft.md) |  | [optional] 
**forge_id** | **str** |  | [optional] 
**forge** | [**Forge**](Forge.md) |  | [optional] 
**neoforge_id** | **str** |  | [optional] 
**neoforge** | [**Neoforge**](Neoforge.md) |  | [optional] 
**quilt_id** | **str** |  | [optional] 
**quilt** | [**Quilt**](Quilt.md) |  | [optional] 
**fabric_id** | **str** |  | [optional] 
**fabric** | [**Fabric**](Fabric.md) |  | [optional] 
**name** | **str** |  | [optional] 
**java** | **str** |  | [optional] 
**memory** | **str** |  | [optional] 
**latest** | **bool** |  | [optional] 
**recommended** | **bool** |  | [optional] 
**public** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.build import Build

# TODO update the JSON string below
json = "{}"
# create an instance of Build from a JSON string
build_instance = Build.from_json(json)
# print the JSON string representation of the object
print(Build.to_json())

# convert the object into a dict
build_dict = build_instance.to_dict()
# create an instance of Build from a dict
build_from_dict = Build.from_dict(build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


