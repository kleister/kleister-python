# TeamPackParams

Parameters to attach or unlink team pack

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | **str** |  | 
**perm** | **str** |  | [optional] [default to 'team']

## Example

```python
from kleister.models.team_pack_params import TeamPackParams

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPackParams from a JSON string
team_pack_params_instance = TeamPackParams.from_json(json)
# print the JSON string representation of the object
print(TeamPackParams.to_json())

# convert the object into a dict
team_pack_params_dict = team_pack_params_instance.to_dict()
# create an instance of TeamPackParams from a dict
team_pack_params_from_dict = TeamPackParams.from_dict(team_pack_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


