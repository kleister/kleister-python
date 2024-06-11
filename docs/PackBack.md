# PackBack

Model to represent pack background

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
from kleister.models.pack_back import PackBack

# TODO update the JSON string below
json = "{}"
# create an instance of PackBack from a JSON string
pack_back_instance = PackBack.from_json(json)
# print the JSON string representation of the object
print(PackBack.to_json())

# convert the object into a dict
pack_back_dict = pack_back_instance.to_dict()
# create an instance of PackBack from a dict
pack_back_from_dict = PackBack.from_dict(pack_back_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


