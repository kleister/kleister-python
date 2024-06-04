# TeamPack

Model to represent team pack

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | 
**team** | [**Team**](Team.md) |  | [optional] 
**pack_id** | **str** |  | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**perm** | **str** |  | [optional] [default to 'team']
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.team_pack import TeamPack

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPack from a JSON string
team_pack_instance = TeamPack.from_json(json)
# print the JSON string representation of the object
print(TeamPack.to_json())

# convert the object into a dict
team_pack_dict = team_pack_instance.to_dict()
# create an instance of TeamPack from a dict
team_pack_from_dict = TeamPack.from_dict(team_pack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


