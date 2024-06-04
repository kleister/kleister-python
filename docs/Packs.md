# Packs

Model to represent list of packs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**packs** | [**List[Pack]**](Pack.md) |  | [optional] 

## Example

```python
from kleister.models.packs import Packs

# TODO update the JSON string below
json = "{}"
# create an instance of Packs from a JSON string
packs_instance = Packs.from_json(json)
# print the JSON string representation of the object
print(Packs.to_json())

# convert the object into a dict
packs_dict = packs_instance.to_dict()
# create an instance of Packs from a dict
packs_from_dict = Packs.from_dict(packs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


