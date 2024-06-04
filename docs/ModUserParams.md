# ModUserParams

Parameters to attach or unlink mod user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**perm** | **str** |  | [optional] [default to 'user']

## Example

```python
from kleister.models.mod_user_params import ModUserParams

# TODO update the JSON string below
json = "{}"
# create an instance of ModUserParams from a JSON string
mod_user_params_instance = ModUserParams.from_json(json)
# print the JSON string representation of the object
print(ModUserParams.to_json())

# convert the object into a dict
mod_user_params_dict = mod_user_params_instance.to_dict()
# create an instance of ModUserParams from a dict
mod_user_params_from_dict = ModUserParams.from_dict(mod_user_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


