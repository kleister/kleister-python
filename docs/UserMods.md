# UserMods

Model to represent user mods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) |  | [optional] 
**total** | **int** |  | [optional] 
**mods** | [**List[UserMod]**](UserMod.md) |  | [optional] 

## Example

```python
from kleister.models.user_mods import UserMods

# TODO update the JSON string below
json = "{}"
# create an instance of UserMods from a JSON string
user_mods_instance = UserMods.from_json(json)
# print the JSON string representation of the object
print(UserMods.to_json())

# convert the object into a dict
user_mods_dict = user_mods_instance.to_dict()
# create an instance of UserMods from a dict
user_mods_from_dict = UserMods.from_dict(user_mods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


