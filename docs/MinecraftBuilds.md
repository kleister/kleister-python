# MinecraftBuilds

Model to represent minecraft builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minecraft** | [**Minecraft**](Minecraft.md) |  | [optional] 
**total** | **int** |  | [optional] 
**builds** | [**List[Build]**](Build.md) |  | [optional] 

## Example

```python
from kleister.models.minecraft_builds import MinecraftBuilds

# TODO update the JSON string below
json = "{}"
# create an instance of MinecraftBuilds from a JSON string
minecraft_builds_instance = MinecraftBuilds.from_json(json)
# print the JSON string representation of the object
print(MinecraftBuilds.to_json())

# convert the object into a dict
minecraft_builds_dict = minecraft_builds_instance.to_dict()
# create an instance of MinecraftBuilds from a dict
minecraft_builds_from_dict = MinecraftBuilds.from_dict(minecraft_builds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


