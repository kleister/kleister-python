# InlineObject11


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**mods** | [**List[Mod]**](Mod.md) |  | 

## Example

```python
from kleister.models.inline_object11 import InlineObject11

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject11 from a JSON string
inline_object11_instance = InlineObject11.from_json(json)
# print the JSON string representation of the object
print(InlineObject11.to_json())

# convert the object into a dict
inline_object11_dict = inline_object11_instance.to_dict()
# create an instance of InlineObject11 from a dict
inline_object11_from_dict = InlineObject11.from_dict(inline_object11_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


