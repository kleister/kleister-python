# InlineObject18


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**groups** | [**List[GroupPack]**](GroupPack.md) |  | 

## Example

```python
from kleister.models.inline_object18 import InlineObject18

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject18 from a JSON string
inline_object18_instance = InlineObject18.from_json(json)
# print the JSON string representation of the object
print(InlineObject18.to_json())

# convert the object into a dict
inline_object18_dict = inline_object18_instance.to_dict()
# create an instance of InlineObject18 from a dict
inline_object18_from_dict = InlineObject18.from_dict(inline_object18_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


