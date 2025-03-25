# PermitPackGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | 
**perm** | **str** |  | 

## Example

```python
from kleister.models.permit_pack_group_request import PermitPackGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermitPackGroupRequest from a JSON string
permit_pack_group_request_instance = PermitPackGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PermitPackGroupRequest.to_json())

# convert the object into a dict
permit_pack_group_request_dict = permit_pack_group_request_instance.to_dict()
# create an instance of PermitPackGroupRequest from a dict
permit_pack_group_request_from_dict = PermitPackGroupRequest.from_dict(permit_pack_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


