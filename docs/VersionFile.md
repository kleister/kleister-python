# VersionFile

Model to represent version file

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
from kleister.models.version_file import VersionFile

# TODO update the JSON string below
json = "{}"
# create an instance of VersionFile from a JSON string
version_file_instance = VersionFile.from_json(json)
# print the JSON string representation of the object
print(VersionFile.to_json())

# convert the object into a dict
version_file_dict = version_file_instance.to_dict()
# create an instance of VersionFile from a dict
version_file_from_dict = VersionFile.from_dict(version_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


