# PackTeams

Model to represent pack teams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | [**Pack**](Pack.md) |  | [optional] 
**total** | **int** |  | [optional] 
**teams** | [**List[TeamPack]**](TeamPack.md) |  | [optional] 

## Example

```python
from kleister.models.pack_teams import PackTeams

# TODO update the JSON string below
json = "{}"
# create an instance of PackTeams from a JSON string
pack_teams_instance = PackTeams.from_json(json)
# print the JSON string representation of the object
print(PackTeams.to_json())

# convert the object into a dict
pack_teams_dict = pack_teams_instance.to_dict()
# create an instance of PackTeams from a dict
pack_teams_from_dict = PackTeams.from_dict(pack_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


