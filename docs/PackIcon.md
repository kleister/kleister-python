# PackIcon

Model to represent pack icon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**pack_id** | **str** |  | [optional] 
**pack** | [**Pack**](Pack.md) |  | [optional] 
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
from kleister.models.pack_icon import PackIcon

# TODO update the JSON string below
json = "{}"
# create an instance of PackIcon from a JSON string
pack_icon_instance = PackIcon.from_json(json)
# print the JSON string representation of the object
print(PackIcon.to_json())

# convert the object into a dict
pack_icon_dict = pack_icon_instance.to_dict()
# create an instance of PackIcon from a dict
pack_icon_from_dict = PackIcon.from_dict(pack_icon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


