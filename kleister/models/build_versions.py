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
from kleister.models.build_version import BuildVersion
from kleister.models.pack import Pack
from typing import Optional, Set
from typing_extensions import Self

class BuildVersions(BaseModel):
    """
    Model to represent build versions
    """ # noqa: E501
    pack: Optional[Pack] = None
    build: Optional[Build] = None
    total: Optional[StrictInt] = None
    versions: Optional[List[BuildVersion]] = None
    __properties: ClassVar[List[str]] = ["pack", "build", "total", "versions"]

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
        """Create an instance of BuildVersions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pack
        if self.pack:
            _dict['pack'] = self.pack.to_dict()
        # override the default output from pydantic by calling `to_dict()` of build
        if self.build:
            _dict['build'] = self.build.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in versions (list)
        _items = []
        if self.versions:
            for _item in self.versions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['versions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BuildVersions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pack": Pack.from_dict(obj["pack"]) if obj.get("pack") is not None else None,
            "build": Build.from_dict(obj["build"]) if obj.get("build") is not None else None,
            "total": obj.get("total"),
            "versions": [BuildVersion.from_dict(_item) for _item in obj["versions"]] if obj.get("versions") is not None else None
        })
        return _obj

