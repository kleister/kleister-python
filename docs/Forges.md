# Forges

Model to represent list of forges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**versions** | [**List[Forge]**](Forge.md) |  | [optional] 

## Example

```python
from kleister.models.forges import Forges

# TODO update the JSON string below
json = "{}"
# create an instance of Forges from a JSON string
forges_instance = Forges.from_json(json)
# print the JSON string representation of the object
print(Forges.to_json())

# convert the object into a dict
forges_dict = forges_instance.to_dict()
# create an instance of Forges from a dict
forges_from_dict = Forges.from_dict(forges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


