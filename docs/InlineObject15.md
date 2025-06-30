# InlineObject15


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**mod** | [**Mod**](Mod.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**builds** | [**List[BuildVersion]**](BuildVersion.md) |  | 

## Example

```python
from kleister.models.inline_object15 import InlineObject15

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject15 from a JSON string
inline_object15_instance = InlineObject15.from_json(json)
# print the JSON string representation of the object
print(InlineObject15.to_json())

# convert the object into a dict
inline_object15_dict = inline_object15_instance.to_dict()
# create an instance of InlineObject15 from a dict
inline_object15_from_dict = InlineObject15.from_dict(inline_object15_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


