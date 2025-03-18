# PermitGroupPackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | **str** |  | 
**perm** | **str** |  | 

## Example

```python
from kleister.models.permit_group_pack_request import PermitGroupPackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermitGroupPackRequest from a JSON string
permit_group_pack_request_instance = PermitGroupPackRequest.from_json(json)
# print the JSON string representation of the object
print(PermitGroupPackRequest.to_json())

# convert the object into a dict
permit_group_pack_request_dict = permit_group_pack_request_instance.to_dict()
# create an instance of PermitGroupPackRequest from a dict
permit_group_pack_request_from_dict = PermitGroupPackRequest.from_dict(permit_group_pack_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


