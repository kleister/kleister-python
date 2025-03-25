# GroupMod

Model to represent group mod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 
**group** | [**Group**](Group.md) |  | [optional] 
**mod_id** | **str** |  | 
**mod** | [**Mod**](Mod.md) |  | [optional] 
**perm** | **str** |  | [optional] [default to 'user']
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.group_mod import GroupMod

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMod from a JSON string
group_mod_instance = GroupMod.from_json(json)
# print the JSON string representation of the object
print(GroupMod.to_json())

# convert the object into a dict
group_mod_dict = group_mod_instance.to_dict()
# create an instance of GroupMod from a dict
group_mod_from_dict = GroupMod.from_dict(group_mod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


