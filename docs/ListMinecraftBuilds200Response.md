# ListMinecraftBuilds200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**minecraft** | [**Minecraft**](Minecraft.md) |  | [optional] 
**builds** | [**List[Build]**](Build.md) |  | 

## Example

```python
from kleister.models.list_minecraft_builds200_response import ListMinecraftBuilds200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMinecraftBuilds200Response from a JSON string
list_minecraft_builds200_response_instance = ListMinecraftBuilds200Response.from_json(json)
# print the JSON string representation of the object
print(ListMinecraftBuilds200Response.to_json())

# convert the object into a dict
list_minecraft_builds200_response_dict = list_minecraft_builds200_response_instance.to_dict()
# create an instance of ListMinecraftBuilds200Response from a dict
list_minecraft_builds200_response_from_dict = ListMinecraftBuilds200Response.from_dict(list_minecraft_builds200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


