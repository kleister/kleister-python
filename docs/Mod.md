# Mod

Model to represent mod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**donate** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.mod import Mod

# TODO update the JSON string below
json = "{}"
# create an instance of Mod from a JSON string
mod_instance = Mod.from_json(json)
# print the JSON string representation of the object
print(Mod.to_json())

# convert the object into a dict
mod_dict = mod_instance.to_dict()
# create an instance of Mod from a dict
mod_from_dict = Mod.from_dict(mod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


