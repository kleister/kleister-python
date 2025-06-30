# InlineObject6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**neoforge** | [**Neoforge**](Neoforge.md) |  | [optional] 
**builds** | [**List[Build]**](Build.md) |  | 

## Example

```python
from kleister.models.inline_object6 import InlineObject6

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject6 from a JSON string
inline_object6_instance = InlineObject6.from_json(json)
# print the JSON string representation of the object
print(InlineObject6.to_json())

# convert the object into a dict
inline_object6_dict = inline_object6_instance.to_dict()
# create an instance of InlineObject6 from a dict
inline_object6_from_dict = InlineObject6.from_dict(inline_object6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


