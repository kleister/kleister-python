# PackLogo

Model to represent pack logo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**slug** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**md5** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**upload** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.pack_logo import PackLogo

# TODO update the JSON string below
json = "{}"
# create an instance of PackLogo from a JSON string
pack_logo_instance = PackLogo.from_json(json)
# print the JSON string representation of the object
print(PackLogo.to_json())

# convert the object into a dict
pack_logo_dict = pack_logo_instance.to_dict()
# create an instance of PackLogo from a dict
pack_logo_from_dict = PackLogo.from_dict(pack_logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


