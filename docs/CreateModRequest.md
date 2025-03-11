# CreateModRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**side** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**donate** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 

## Example

```python
from kleister.models.create_mod_request import CreateModRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateModRequest from a JSON string
create_mod_request_instance = CreateModRequest.from_json(json)
# print the JSON string representation of the object
print(CreateModRequest.to_json())

# convert the object into a dict
create_mod_request_dict = create_mod_request_instance.to_dict()
# create an instance of CreateModRequest from a dict
create_mod_request_from_dict = CreateModRequest.from_dict(create_mod_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


