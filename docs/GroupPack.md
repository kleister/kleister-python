# GroupPack

Model to represent group pack

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 
**group** | [**Group**](Group.md) |  | [optional] 
**pack_id** | **str** |  | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**perm** | **str** |  | [optional] [default to 'user']
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.group_pack import GroupPack

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPack from a JSON string
group_pack_instance = GroupPack.from_json(json)
# print the JSON string representation of the object
print(GroupPack.to_json())

# convert the object into a dict
group_pack_dict = group_pack_instance.to_dict()
# create an instance of GroupPack from a dict
group_pack_from_dict = GroupPack.from_dict(group_pack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


