# Builds

Model to represent list of builds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**pack** | [**Pack**](Pack.md) |  | [optional] 
**builds** | [**List[Build]**](Build.md) |  | [optional] 

## Example

```python
from kleister.models.builds import Builds

# TODO update the JSON string below
json = "{}"
# create an instance of Builds from a JSON string
builds_instance = Builds.from_json(json)
# print the JSON string representation of the object
print(Builds.to_json())

# convert the object into a dict
builds_dict = builds_instance.to_dict()
# create an instance of Builds from a dict
builds_from_dict = Builds.from_dict(builds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


