# QuiltBuildParams

Model to represent params for quilt builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | **str** |  | 
**build** | **str** |  | 

## Example

```python
from kleister.models.quilt_build_params import QuiltBuildParams

# TODO update the JSON string below
json = "{}"
# create an instance of QuiltBuildParams from a JSON string
quilt_build_params_instance = QuiltBuildParams.from_json(json)
# print the JSON string representation of the object
print(QuiltBuildParams.to_json())

# convert the object into a dict
quilt_build_params_dict = quilt_build_params_instance.to_dict()
# create an instance of QuiltBuildParams from a dict
quilt_build_params_from_dict = QuiltBuildParams.from_dict(quilt_build_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


