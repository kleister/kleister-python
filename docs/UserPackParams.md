# UserPackParams

Parameters to attach or unlink user pack

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | **str** |  | 
**perm** | **str** |  | [optional] [default to 'user']

## Example

```python
from kleister.models.user_pack_params import UserPackParams

# TODO update the JSON string below
json = "{}"
# create an instance of UserPackParams from a JSON string
user_pack_params_instance = UserPackParams.from_json(json)
# print the JSON string representation of the object
print(UserPackParams.to_json())

# convert the object into a dict
user_pack_params_dict = user_pack_params_instance.to_dict()
# create an instance of UserPackParams from a dict
user_pack_params_from_dict = UserPackParams.from_dict(user_pack_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


