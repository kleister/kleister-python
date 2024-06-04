# TeamMods

Model to represent team mods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | [**Team**](Team.md) |  | [optional] 
**total** | **int** |  | [optional] 
**mods** | [**List[TeamMod]**](TeamMod.md) |  | [optional] 

## Example

```python
from kleister.models.team_mods import TeamMods

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMods from a JSON string
team_mods_instance = TeamMods.from_json(json)
# print the JSON string representation of the object
print(TeamMods.to_json())

# convert the object into a dict
team_mods_dict = team_mods_instance.to_dict()
# create an instance of TeamMods from a dict
team_mods_from_dict = TeamMods.from_dict(team_mods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


