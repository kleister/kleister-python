# Neoforges

Model to represent list of neoforges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**versions** | [**List[Neoforge]**](Neoforge.md) |  | [optional] 

## Example

```python
from kleister.models.neoforges import Neoforges

# TODO update the JSON string below
json = "{}"
# create an instance of Neoforges from a JSON string
neoforges_instance = Neoforges.from_json(json)
# print the JSON string representation of the object
print(Neoforges.to_json())

# convert the object into a dict
neoforges_dict = neoforges_instance.to_dict()
# create an instance of Neoforges from a dict
neoforges_from_dict = Neoforges.from_dict(neoforges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


