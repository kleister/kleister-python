# Quilts

Model to represent list of quilts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**versions** | [**List[Quilt]**](Quilt.md) |  | [optional] 

## Example

```python
from kleister.models.quilts import Quilts

# TODO update the JSON string below
json = "{}"
# create an instance of Quilts from a JSON string
quilts_instance = Quilts.from_json(json)
# print the JSON string representation of the object
print(Quilts.to_json())

# convert the object into a dict
quilts_dict = quilts_instance.to_dict()
# create an instance of Quilts from a dict
quilts_from_dict = Quilts.from_dict(quilts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


