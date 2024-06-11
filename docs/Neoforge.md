# Neoforge

Model to represent neoforge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.neoforge import Neoforge

# TODO update the JSON string below
json = "{}"
# create an instance of Neoforge from a JSON string
neoforge_instance = Neoforge.from_json(json)
# print the JSON string representation of the object
print(Neoforge.to_json())

# convert the object into a dict
neoforge_dict = neoforge_instance.to_dict()
# create an instance of Neoforge from a dict
neoforge_from_dict = Neoforge.from_dict(neoforge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


