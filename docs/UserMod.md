# UserMod

Model to represent user mod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**user** | [**User**](User.md) |  | [optional] 
**mod_id** | **str** |  | 
**mod** | [**Mod**](Mod.md) |  | [optional] 
**perm** | **str** |  | [optional] [default to 'user']
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.user_mod import UserMod

# TODO update the JSON string below
json = "{}"
# create an instance of UserMod from a JSON string
user_mod_instance = UserMod.from_json(json)
# print the JSON string representation of the object
print(UserMod.to_json())

# convert the object into a dict
user_mod_dict = user_mod_instance.to_dict()
# create an instance of UserMod from a dict
user_mod_from_dict = UserMod.from_dict(user_mod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


