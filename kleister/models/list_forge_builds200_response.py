# coding: utf-8

"""
    Kleister OpenAPI

    API definition for Kleister, manage mod packs for Minecraft

    The version of the OpenAPI document: 1.0.0-alpha1
    Contact: kleister@webhippie.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from kleister.models.build import Build
from kleister.models.forge import Forge
from typing import Optional, Set
from typing_extensions import Self

class ListForgeBuilds200Response(BaseModel):
    """
    ListForgeBuilds200Response
    """ # noqa: E501
    total: StrictInt
    limit: StrictInt
    offset: StrictInt
    forge: Optional[Forge] = None
    builds: List[Build]
    __properties: ClassVar[List[str]] = ["total", "limit", "offset", "forge", "builds"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ListForgeBuilds200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of forge
        if self.forge:
            _dict['forge'] = self.forge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in builds (list)
        _items = []
        if self.builds:
            for _item in self.builds:
                if _item:
                    _items.append(_item.to_dict())
            _dict['builds'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListForgeBuilds200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total": obj.get("total"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "forge": Forge.from_dict(obj["forge"]) if obj.get("forge") is not None else None,
            "builds": [Build.from_dict(_item) for _item in obj["builds"]] if obj.get("builds") is not None else None
        })
        return _obj


