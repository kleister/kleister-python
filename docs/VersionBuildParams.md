# VersionBuildParams

Parameters to attach or unlink version build

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | **str** |  | 
**build** | **str** |  | 

## Example

```python
from kleister.models.version_build_params import VersionBuildParams

# TODO update the JSON string below
json = "{}"
# create an instance of VersionBuildParams from a JSON string
version_build_params_instance = VersionBuildParams.from_json(json)
# print the JSON string representation of the object
print(VersionBuildParams.to_json())

# convert the object into a dict
version_build_params_dict = version_build_params_instance.to_dict()
# create an instance of VersionBuildParams from a dict
version_build_params_from_dict = VersionBuildParams.from_dict(version_build_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


