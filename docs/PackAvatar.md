# PackAvatar

Model to represent pack avatar

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.pack_avatar import PackAvatar

# TODO update the JSON string below
json = "{}"
# create an instance of PackAvatar from a JSON string
pack_avatar_instance = PackAvatar.from_json(json)
# print the JSON string representation of the object
print(PackAvatar.to_json())

# convert the object into a dict
pack_avatar_dict = pack_avatar_instance.to_dict()
# create an instance of PackAvatar from a dict
pack_avatar_from_dict = PackAvatar.from_dict(pack_avatar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


