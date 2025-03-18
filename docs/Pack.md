# Pack

Model to represent pack

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**avatar** | [**PackAvatar**](PackAvatar.md) |  | [optional] 
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from kleister.models.pack import Pack

# TODO update the JSON string below
json = "{}"
# create an instance of Pack from a JSON string
pack_instance = Pack.from_json(json)
# print the JSON string representation of the object
print(Pack.to_json())

# convert the object into a dict
pack_dict = pack_instance.to_dict()
# create an instance of Pack from a dict
pack_from_dict = Pack.from_dict(pack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


