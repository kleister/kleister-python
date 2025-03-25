# AttachMinecraftToBuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | **str** |  | 
**build** | **str** |  | 

## Example

```python
from kleister.models.attach_minecraft_to_build_request import AttachMinecraftToBuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachMinecraftToBuildRequest from a JSON string
attach_minecraft_to_build_request_instance = AttachMinecraftToBuildRequest.from_json(json)
# print the JSON string representation of the object
print(AttachMinecraftToBuildRequest.to_json())

# convert the object into a dict
attach_minecraft_to_build_request_dict = attach_minecraft_to_build_request_instance.to_dict()
# create an instance of AttachMinecraftToBuildRequest from a dict
attach_minecraft_to_build_request_from_dict = AttachMinecraftToBuildRequest.from_dict(attach_minecraft_to_build_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


