# UserPacks

Model to represent user packs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) |  | [optional] 
**total** | **int** |  | [optional] 
**packs** | [**List[UserPack]**](UserPack.md) |  | [optional] 

## Example

```python
from kleister.models.user_packs import UserPacks

# TODO update the JSON string below
json = "{}"
# create an instance of UserPacks from a JSON string
user_packs_instance = UserPacks.from_json(json)
# print the JSON string representation of the object
print(UserPacks.to_json())

# convert the object into a dict
user_packs_dict = user_packs_instance.to_dict()
# create an instance of UserPacks from a dict
user_packs_from_dict = UserPacks.from_dict(user_packs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


