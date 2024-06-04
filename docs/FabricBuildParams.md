# FabricBuildParams

Model to represent params for fabric builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | **str** |  | 
**build** | **str** |  | 

## Example

```python
from kleister.models.fabric_build_params import FabricBuildParams

# TODO update the JSON string below
json = "{}"
# create an instance of FabricBuildParams from a JSON string
fabric_build_params_instance = FabricBuildParams.from_json(json)
# print the JSON string representation of the object
print(FabricBuildParams.to_json())

# convert the object into a dict
fabric_build_params_dict = fabric_build_params_instance.to_dict()
# create an instance of FabricBuildParams from a dict
fabric_build_params_from_dict = FabricBuildParams.from_dict(fabric_build_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


