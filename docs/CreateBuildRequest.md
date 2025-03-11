# CreateBuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minecraft_id** | **str** |  | [optional] 
**forge_id** | **str** |  | [optional] 
**neoforge_id** | **str** |  | [optional] 
**quilt_id** | **str** |  | [optional] 
**fabric_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**java** | **str** |  | [optional] 
**memory** | **str** |  | [optional] 
**latest** | **bool** |  | [optional] 
**recommended** | **bool** |  | [optional] 
**public** | **bool** |  | [optional] 

## Example

```python
from kleister.models.create_build_request import CreateBuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBuildRequest from a JSON string
create_build_request_instance = CreateBuildRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBuildRequest.to_json())

# convert the object into a dict
create_build_request_dict = create_build_request_instance.to_dict()
# create an instance of CreateBuildRequest from a dict
create_build_request_from_dict = CreateBuildRequest.from_dict(create_build_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


