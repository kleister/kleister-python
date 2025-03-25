# ModAvatar

Model to represent mod avatar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.mod_avatar import ModAvatar

# TODO update the JSON string below
json = "{}"
# create an instance of ModAvatar from a JSON string
mod_avatar_instance = ModAvatar.from_json(json)
# print the JSON string representation of the object
print(ModAvatar.to_json())

# convert the object into a dict
mod_avatar_dict = mod_avatar_instance.to_dict()
# create an instance of ModAvatar from a dict
mod_avatar_from_dict = ModAvatar.from_dict(mod_avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


