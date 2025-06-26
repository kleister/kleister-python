# InlineObject9


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**versions** | [**List[Fabric]**](Fabric.md) |  | 

## Example

```python
from kleister.models.inline_object9 import InlineObject9

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject9 from a JSON string
inline_object9_instance = InlineObject9.from_json(json)
# print the JSON string representation of the object
print(InlineObject9.to_json())

# convert the object into a dict
inline_object9_dict = inline_object9_instance.to_dict()
# create an instance of InlineObject9 from a dict
inline_object9_from_dict = InlineObject9.from_dict(inline_object9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


