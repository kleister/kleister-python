# Mods

Model to represent list of mods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**mods** | [**List[Mod]**](Mod.md) |  | [optional] 

## Example

```python
from kleister.models.mods import Mods

# TODO update the JSON string below
json = "{}"
# create an instance of Mods from a JSON string
mods_instance = Mods.from_json(json)
# print the JSON string representation of the object
print(Mods.to_json())

# convert the object into a dict
mods_dict = mods_instance.to_dict()
# create an instance of Mods from a dict
mods_from_dict = Mods.from_dict(mods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


