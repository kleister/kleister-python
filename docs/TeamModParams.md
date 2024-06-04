# TeamModParams

Parameters to attach or unlink team mod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mod** | **str** |  | 
**perm** | **str** |  | [optional] [default to 'team']

## Example

```python
from kleister.models.team_mod_params import TeamModParams

# TODO update the JSON string below
json = "{}"
# create an instance of TeamModParams from a JSON string
team_mod_params_instance = TeamModParams.from_json(json)
# print the JSON string representation of the object
print(TeamModParams.to_json())

# convert the object into a dict
team_mod_params_dict = team_mod_params_instance.to_dict()
# create an instance of TeamModParams from a dict
team_mod_params_from_dict = TeamModParams.from_dict(team_mod_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


