# TeamPacks

Model to represent team packs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | [**Team**](Team.md) |  | [optional] 
**total** | **int** |  | [optional] 
**packs** | [**List[TeamPack]**](TeamPack.md) |  | [optional] 

## Example

```python
from kleister.models.team_packs import TeamPacks

# TODO update the JSON string below
json = "{}"
# create an instance of TeamPacks from a JSON string
team_packs_instance = TeamPacks.from_json(json)
# print the JSON string representation of the object
print(TeamPacks.to_json())

# convert the object into a dict
team_packs_dict = team_packs_instance.to_dict()
# create an instance of TeamPacks from a dict
team_packs_from_dict = TeamPacks.from_dict(team_packs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


