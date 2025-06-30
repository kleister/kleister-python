# InlineObject20


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**build** | [**Build**](Build.md) |  | [optional] 
**versions** | [**List[BuildVersion]**](BuildVersion.md) |  | 

## Example

```python
from kleister.models.inline_object20 import InlineObject20

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject20 from a JSON string
inline_object20_instance = InlineObject20.from_json(json)
# print the JSON string representation of the object
print(InlineObject20.to_json())

# convert the object into a dict
inline_object20_dict = inline_object20_instance.to_dict()
# create an instance of InlineObject20 from a dict
inline_object20_from_dict = InlineObject20.from_dict(inline_object20_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


