# CreatePackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 

## Example

```python
from kleister.models.create_pack_request import CreatePackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePackRequest from a JSON string
create_pack_request_instance = CreatePackRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePackRequest.to_json())

# convert the object into a dict
create_pack_request_dict = create_pack_request_instance.to_dict()
# create an instance of CreatePackRequest from a dict
create_pack_request_from_dict = CreatePackRequest.from_dict(create_pack_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


