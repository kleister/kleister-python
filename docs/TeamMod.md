# TeamMod

Model to represent team mod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **str** |  | 
**team** | [**Team**](Team.md) |  | [optional] 
**mod_id** | **str** |  | 
**mod** | [**Mod**](Mod.md) |  | [optional] 
**perm** | **str** |  | [optional] [default to 'team']
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.team_mod import TeamMod

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMod from a JSON string
team_mod_instance = TeamMod.from_json(json)
# print the JSON string representation of the object
print(TeamMod.to_json())

# convert the object into a dict
team_mod_dict = team_mod_instance.to_dict()
# create an instance of TeamMod from a dict
team_mod_from_dict = TeamMod.from_dict(team_mod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


