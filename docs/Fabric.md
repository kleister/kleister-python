# Fabric

Model to represent fabric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.fabric import Fabric

# TODO update the JSON string below
json = "{}"
# create an instance of Fabric from a JSON string
fabric_instance = Fabric.from_json(json)
# print the JSON string representation of the object
print(Fabric.to_json())

# convert the object into a dict
fabric_dict = fabric_instance.to_dict()
# create an instance of Fabric from a dict
fabric_from_dict = Fabric.from_dict(fabric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


