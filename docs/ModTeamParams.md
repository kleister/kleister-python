# ModTeamParams

Parameters to attach or unlink mod team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**perm** | **str** |  | [optional] [default to 'user']

## Example

```python
from kleister.models.mod_team_params import ModTeamParams

# TODO update the JSON string below
json = "{}"
# create an instance of ModTeamParams from a JSON string
mod_team_params_instance = ModTeamParams.from_json(json)
# print the JSON string representation of the object
print(ModTeamParams.to_json())

# convert the object into a dict
mod_team_params_dict = mod_team_params_instance.to_dict()
# create an instance of ModTeamParams from a dict
mod_team_params_from_dict = ModTeamParams.from_dict(mod_team_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


