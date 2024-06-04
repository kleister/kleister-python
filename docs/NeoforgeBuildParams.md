# NeoforgeBuildParams

Model to represent params for neoforge builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | **str** |  | 
**build** | **str** |  | 

## Example

```python
from kleister.models.neoforge_build_params import NeoforgeBuildParams

# TODO update the JSON string below
json = "{}"
# create an instance of NeoforgeBuildParams from a JSON string
neoforge_build_params_instance = NeoforgeBuildParams.from_json(json)
# print the JSON string representation of the object
print(NeoforgeBuildParams.to_json())

# convert the object into a dict
neoforge_build_params_dict = neoforge_build_params_instance.to_dict()
# create an instance of NeoforgeBuildParams from a dict
neoforge_build_params_from_dict = NeoforgeBuildParams.from_dict(neoforge_build_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


