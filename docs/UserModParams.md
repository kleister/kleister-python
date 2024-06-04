# UserModParams

Parameters to attach or unlink user mod

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mod** | **str** |  | 
**perm** | **str** |  | [optional] [default to 'user']

## Example

```python
from kleister.models.user_mod_params import UserModParams

# TODO update the JSON string below
json = "{}"
# create an instance of UserModParams from a JSON string
user_mod_params_instance = UserModParams.from_json(json)
# print the JSON string representation of the object
print(UserModParams.to_json())

# convert the object into a dict
user_mod_params_dict = user_mod_params_instance.to_dict()
# create an instance of UserModParams from a dict
user_mod_params_from_dict = UserModParams.from_dict(user_mod_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


