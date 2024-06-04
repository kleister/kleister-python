# Quilt

Model to represent quilt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.quilt import Quilt

# TODO update the JSON string below
json = "{}"
# create an instance of Quilt from a JSON string
quilt_instance = Quilt.from_json(json)
# print the JSON string representation of the object
print(Quilt.to_json())

# convert the object into a dict
quilt_dict = quilt_instance.to_dict()
# create an instance of Quilt from a dict
quilt_from_dict = Quilt.from_dict(quilt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


