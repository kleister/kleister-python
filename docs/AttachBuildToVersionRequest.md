# AttachBuildToVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mod** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from kleister.models.attach_build_to_version_request import AttachBuildToVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachBuildToVersionRequest from a JSON string
attach_build_to_version_request_instance = AttachBuildToVersionRequest.from_json(json)
# print the JSON string representation of the object
print(AttachBuildToVersionRequest.to_json())

# convert the object into a dict
attach_build_to_version_request_dict = attach_build_to_version_request_instance.to_dict()
# create an instance of AttachBuildToVersionRequest from a dict
attach_build_to_version_request_from_dict = AttachBuildToVersionRequest.from_dict(attach_build_to_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


