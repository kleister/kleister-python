# ListMinecrafts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**versions** | [**List[Minecraft]**](Minecraft.md) |  | 

## Example

```python
from kleister.models.list_minecrafts200_response import ListMinecrafts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMinecrafts200Response from a JSON string
list_minecrafts200_response_instance = ListMinecrafts200Response.from_json(json)
# print the JSON string representation of the object
print(ListMinecrafts200Response.to_json())

# convert the object into a dict
list_minecrafts200_response_dict = list_minecrafts200_response_instance.to_dict()
# create an instance of ListMinecrafts200Response from a dict
list_minecrafts200_response_from_dict = ListMinecrafts200Response.from_dict(list_minecrafts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


