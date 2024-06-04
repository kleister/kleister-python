# UserPack

Model to represent user pack

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**user** | [**User**](User.md) |  | [optional] 
**pack_id** | **str** |  | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**perm** | **str** |  | [optional] [default to 'user']
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.user_pack import UserPack

# TODO update the JSON string below
json = "{}"
# create an instance of UserPack from a JSON string
user_pack_instance = UserPack.from_json(json)
# print the JSON string representation of the object
print(UserPack.to_json())

# convert the object into a dict
user_pack_dict = user_pack_instance.to_dict()
# create an instance of UserPack from a dict
user_pack_from_dict = UserPack.from_dict(user_pack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


