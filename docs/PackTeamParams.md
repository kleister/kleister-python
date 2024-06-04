# PackTeamParams

Parameters to attach or unlink pack team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **str** |  | 
**perm** | **str** |  | [optional] [default to 'team']

## Example

```python
from kleister.models.pack_team_params import PackTeamParams

# TODO update the JSON string below
json = "{}"
# create an instance of PackTeamParams from a JSON string
pack_team_params_instance = PackTeamParams.from_json(json)
# print the JSON string representation of the object
print(PackTeamParams.to_json())

# convert the object into a dict
pack_team_params_dict = pack_team_params_instance.to_dict()
# create an instance of PackTeamParams from a dict
pack_team_params_from_dict = PackTeamParams.from_dict(pack_team_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


