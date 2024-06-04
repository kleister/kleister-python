# QuiltBuilds

Model to represent quilt builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quilt** | [**Quilt**](Quilt.md) |  | [optional] 
**total** | **int** |  | [optional] 
**builds** | [**List[Build]**](Build.md) |  | [optional] 

## Example

```python
from kleister.models.quilt_builds import QuiltBuilds

# TODO update the JSON string below
json = "{}"
# create an instance of QuiltBuilds from a JSON string
quilt_builds_instance = QuiltBuilds.from_json(json)
# print the JSON string representation of the object
print(QuiltBuilds.to_json())

# convert the object into a dict
quilt_builds_dict = quilt_builds_instance.to_dict()
# create an instance of QuiltBuilds from a dict
quilt_builds_from_dict = QuiltBuilds.from_dict(quilt_builds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


