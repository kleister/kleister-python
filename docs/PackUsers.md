# PackUsers

Model to represent pack users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pack** | [**Pack**](Pack.md) |  | [optional] 
**total** | **int** |  | [optional] 
**users** | [**List[UserPack]**](UserPack.md) |  | [optional] 

## Example

```python
from kleister.models.pack_users import PackUsers

# TODO update the JSON string below
json = "{}"
# create an instance of PackUsers from a JSON string
pack_users_instance = PackUsers.from_json(json)
# print the JSON string representation of the object
print(PackUsers.to_json())

# convert the object into a dict
pack_users_dict = pack_users_instance.to_dict()
# create an instance of PackUsers from a dict
pack_users_from_dict = PackUsers.from_dict(pack_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


