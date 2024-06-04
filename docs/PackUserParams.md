# PackUserParams

Parameters to attach or unlink pack user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**perm** | **str** |  | [optional] [default to 'user']

## Example

```python
from kleister.models.pack_user_params import PackUserParams

# TODO update the JSON string below
json = "{}"
# create an instance of PackUserParams from a JSON string
pack_user_params_instance = PackUserParams.from_json(json)
# print the JSON string representation of the object
print(PackUserParams.to_json())

# convert the object into a dict
pack_user_params_dict = pack_user_params_instance.to_dict()
# create an instance of PackUserParams from a dict
pack_user_params_from_dict = PackUserParams.from_dict(pack_user_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


