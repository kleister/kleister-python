# InlineObject22


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**group** | [**Group**](Group.md) |  | [optional] 
**users** | [**List[UserGroup]**](UserGroup.md) |  | 

## Example

```python
from kleister.models.inline_object22 import InlineObject22

# TODO update the JSON string below
json = "{}"
# create an instance of InlineObject22 from a JSON string
inline_object22_instance = InlineObject22.from_json(json)
# print the JSON string representation of the object
print(InlineObject22.to_json())

# convert the object into a dict
inline_object22_dict = inline_object22_instance.to_dict()
# create an instance of InlineObject22 from a dict
inline_object22_from_dict = InlineObject22.from_dict(inline_object22_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


