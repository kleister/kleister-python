# Minecraft

Model to represent minecraft

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.minecraft import Minecraft

# TODO update the JSON string below
json = "{}"
# create an instance of Minecraft from a JSON string
minecraft_instance = Minecraft.from_json(json)
# print the JSON string representation of the object
print(Minecraft.to_json())

# convert the object into a dict
minecraft_dict = minecraft_instance.to_dict()
# create an instance of Minecraft from a dict
minecraft_from_dict = Minecraft.from_dict(minecraft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


