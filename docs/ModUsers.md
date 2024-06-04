# ModUsers

Model to represent mod users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mod** | [**Mod**](Mod.md) |  | [optional] 
**total** | **int** |  | [optional] 
**users** | [**List[UserMod]**](UserMod.md) |  | [optional] 

## Example

```python
from kleister.models.mod_users import ModUsers

# TODO update the JSON string below
json = "{}"
# create an instance of ModUsers from a JSON string
mod_users_instance = ModUsers.from_json(json)
# print the JSON string representation of the object
print(ModUsers.to_json())

# convert the object into a dict
mod_users_dict = mod_users_instance.to_dict()
# create an instance of ModUsers from a dict
mod_users_from_dict = ModUsers.from_dict(mod_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


