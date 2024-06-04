# Fabrics

Model to represent list of fabrics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**versions** | [**List[Fabric]**](Fabric.md) |  | [optional] 

## Example

```python
from kleister.models.fabrics import Fabrics

# TODO update the JSON string below
json = "{}"
# create an instance of Fabrics from a JSON string
fabrics_instance = Fabrics.from_json(json)
# print the JSON string representation of the object
print(Fabrics.to_json())

# convert the object into a dict
fabrics_dict = fabrics_instance.to_dict()
# create an instance of Fabrics from a dict
fabrics_from_dict = Fabrics.from_dict(fabrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


