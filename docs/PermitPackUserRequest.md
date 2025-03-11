# PermitPackUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**perm** | **str** |  | 

## Example

```python
from kleister.models.permit_pack_user_request import PermitPackUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PermitPackUserRequest from a JSON string
permit_pack_user_request_instance = PermitPackUserRequest.from_json(json)
# print the JSON string representation of the object
print(PermitPackUserRequest.to_json())

# convert the object into a dict
permit_pack_user_request_dict = permit_pack_user_request_instance.to_dict()
# create an instance of PermitPackUserRequest from a dict
permit_pack_user_request_from_dict = PermitPackUserRequest.from_dict(permit_pack_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


