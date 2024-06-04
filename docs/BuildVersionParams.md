# BuildVersionParams

Parameters to attach or unlink build version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mod** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from kleister.models.build_version_params import BuildVersionParams

# TODO update the JSON string below
json = "{}"
# create an instance of BuildVersionParams from a JSON string
build_version_params_instance = BuildVersionParams.from_json(json)
# print the JSON string representation of the object
print(BuildVersionParams.to_json())

# convert the object into a dict
build_version_params_dict = build_version_params_instance.to_dict()
# create an instance of BuildVersionParams from a dict
build_version_params_from_dict = BuildVersionParams.from_dict(build_version_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


