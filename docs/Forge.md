# Forge

Model to represent forge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**minecraft** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.forge import Forge

# TODO update the JSON string below
json = "{}"
# create an instance of Forge from a JSON string
forge_instance = Forge.from_json(json)
# print the JSON string representation of the object
print(Forge.to_json())

# convert the object into a dict
forge_dict = forge_instance.to_dict()
# create an instance of Forge from a dict
forge_from_dict = Forge.from_dict(forge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


