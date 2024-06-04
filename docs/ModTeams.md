# ModTeams

Model to represent mod teams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mod** | [**Mod**](Mod.md) |  | [optional] 
**total** | **int** |  | [optional] 
**teams** | [**List[TeamMod]**](TeamMod.md) |  | [optional] 

## Example

```python
from kleister.models.mod_teams import ModTeams

# TODO update the JSON string below
json = "{}"
# create an instance of ModTeams from a JSON string
mod_teams_instance = ModTeams.from_json(json)
# print the JSON string representation of the object
print(ModTeams.to_json())

# convert the object into a dict
mod_teams_dict = mod_teams_instance.to_dict()
# create an instance of ModTeams from a dict
mod_teams_from_dict = ModTeams.from_dict(mod_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


