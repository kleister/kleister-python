# ForgeBuildParams

Model to represent params for forge builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | **str** |  | 
**build** | **str** |  | 

## Example

```python
from kleister.models.forge_build_params import ForgeBuildParams

# TODO update the JSON string below
json = "{}"
# create an instance of ForgeBuildParams from a JSON string
forge_build_params_instance = ForgeBuildParams.from_json(json)
# print the JSON string representation of the object
print(ForgeBuildParams.to_json())

# convert the object into a dict
forge_build_params_dict = forge_build_params_instance.to_dict()
# create an instance of ForgeBuildParams from a dict
forge_build_params_from_dict = ForgeBuildParams.from_dict(forge_build_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


