# Minecrafts

Model to represent list of minecrafts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**versions** | [**List[Minecraft]**](Minecraft.md) |  | [optional] 

## Example

```python
from kleister.models.minecrafts import Minecrafts

# TODO update the JSON string below
json = "{}"
# create an instance of Minecrafts from a JSON string
minecrafts_instance = Minecrafts.from_json(json)
# print the JSON string representation of the object
print(Minecrafts.to_json())

# convert the object into a dict
minecrafts_dict = minecrafts_instance.to_dict()
# create an instance of Minecrafts from a dict
minecrafts_from_dict = Minecrafts.from_dict(minecrafts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


