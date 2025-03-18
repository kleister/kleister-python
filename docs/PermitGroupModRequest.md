# PermitGroupModRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mod** | **str** |  | 
**perm** | **str** |  | 

## Example

```python
from kleister.models.permit_group_mod_request import PermitGroupModRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermitGroupModRequest from a JSON string
permit_group_mod_request_instance = PermitGroupModRequest.from_json(json)
# print the JSON string representation of the object
print(PermitGroupModRequest.to_json())

# convert the object into a dict
permit_group_mod_request_dict = permit_group_mod_request_instance.to_dict()
# create an instance of PermitGroupModRequest from a dict
permit_group_mod_request_from_dict = PermitGroupModRequest.from_dict(permit_group_mod_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


