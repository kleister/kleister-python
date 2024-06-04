# MinecraftBuildParams

Model to represent params for minecraft builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | **str** |  | 
**build** | **str** |  | 

## Example

```python
from kleister.models.minecraft_build_params import MinecraftBuildParams

# TODO update the JSON string below
json = "{}"
# create an instance of MinecraftBuildParams from a JSON string
minecraft_build_params_instance = MinecraftBuildParams.from_json(json)
# print the JSON string representation of the object
print(MinecraftBuildParams.to_json())

# convert the object into a dict
minecraft_build_params_dict = minecraft_build_params_instance.to_dict()
# create an instance of MinecraftBuildParams from a dict
minecraft_build_params_from_dict = MinecraftBuildParams.from_dict(minecraft_build_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


