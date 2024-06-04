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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kleister.models.fabric import Fabric
from kleister.models.forge import Forge
from kleister.models.minecraft import Minecraft
from kleister.models.neoforge import Neoforge
from kleister.models.quilt import Quilt
from typing import Optional, Set
from typing_extensions import Self

class Build(BaseModel):
    """
    Model to represent build
    """ # noqa: E501
    id: Optional[StrictStr] = None
    pack_id: Optional[StrictStr] = None
    pack: Optional[Pack] = None
    minecraft_id: Optional[StrictStr] = None
    minecraft: Optional[Minecraft] = None
    forge_id: Optional[StrictStr] = None
    forge: Optional[Forge] = None
    neoforge_id: Optional[StrictStr] = None
    neoforge: Optional[Neoforge] = None
    quilt_id: Optional[StrictStr] = None
    quilt: Optional[Quilt] = None
    fabric_id: Optional[StrictStr] = None
    fabric: Optional[Fabric] = None
    slug: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    java: Optional[StrictStr] = None
    memory: Optional[StrictStr] = None
    public: Optional[StrictBool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    versions: Optional[List[BuildVersion]] = None
    __properties: ClassVar[List[str]] = ["id", "pack_id", "pack", "minecraft_id", "minecraft", "forge_id", "forge", "neoforge_id", "neoforge", "quilt_id", "quilt", "fabric_id", "fabric", "slug", "name", "java", "memory", "public", "created_at", "updated_at", "versions"]

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
        """Create an instance of Build from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "created_at",
            "updated_at",
            "versions",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of pack
        if self.pack:
            _dict['pack'] = self.pack.to_dict()
        # override the default output from pydantic by calling `to_dict()` of minecraft
        if self.minecraft:
            _dict['minecraft'] = self.minecraft.to_dict()
        # override the default output from pydantic by calling `to_dict()` of forge
        if self.forge:
            _dict['forge'] = self.forge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of neoforge
        if self.neoforge:
            _dict['neoforge'] = self.neoforge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quilt
        if self.quilt:
            _dict['quilt'] = self.quilt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fabric
        if self.fabric:
            _dict['fabric'] = self.fabric.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in versions (list)
        _items = []
        if self.versions:
            for _item in self.versions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['versions'] = _items
        # set to None if minecraft_id (nullable) is None
        # and model_fields_set contains the field
        if self.minecraft_id is None and "minecraft_id" in self.model_fields_set:
            _dict['minecraft_id'] = None

        # set to None if forge_id (nullable) is None
        # and model_fields_set contains the field
        if self.forge_id is None and "forge_id" in self.model_fields_set:
            _dict['forge_id'] = None

        # set to None if neoforge_id (nullable) is None
        # and model_fields_set contains the field
        if self.neoforge_id is None and "neoforge_id" in self.model_fields_set:
            _dict['neoforge_id'] = None

        # set to None if quilt_id (nullable) is None
        # and model_fields_set contains the field
        if self.quilt_id is None and "quilt_id" in self.model_fields_set:
            _dict['quilt_id'] = None

        # set to None if fabric_id (nullable) is None
        # and model_fields_set contains the field
        if self.fabric_id is None and "fabric_id" in self.model_fields_set:
            _dict['fabric_id'] = None

        # set to None if slug (nullable) is None
        # and model_fields_set contains the field
        if self.slug is None and "slug" in self.model_fields_set:
            _dict['slug'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if java (nullable) is None
        # and model_fields_set contains the field
        if self.java is None and "java" in self.model_fields_set:
            _dict['java'] = None

        # set to None if memory (nullable) is None
        # and model_fields_set contains the field
        if self.memory is None and "memory" in self.model_fields_set:
            _dict['memory'] = None

        # set to None if public (nullable) is None
        # and model_fields_set contains the field
        if self.public is None and "public" in self.model_fields_set:
            _dict['public'] = None

        # set to None if versions (nullable) is None
        # and model_fields_set contains the field
        if self.versions is None and "versions" in self.model_fields_set:
            _dict['versions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Build from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "pack_id": obj.get("pack_id"),
            "pack": Pack.from_dict(obj["pack"]) if obj.get("pack") is not None else None,
            "minecraft_id": obj.get("minecraft_id"),
            "minecraft": Minecraft.from_dict(obj["minecraft"]) if obj.get("minecraft") is not None else None,
            "forge_id": obj.get("forge_id"),
            "forge": Forge.from_dict(obj["forge"]) if obj.get("forge") is not None else None,
            "neoforge_id": obj.get("neoforge_id"),
            "neoforge": Neoforge.from_dict(obj["neoforge"]) if obj.get("neoforge") is not None else None,
            "quilt_id": obj.get("quilt_id"),
            "quilt": Quilt.from_dict(obj["quilt"]) if obj.get("quilt") is not None else None,
            "fabric_id": obj.get("fabric_id"),
            "fabric": Fabric.from_dict(obj["fabric"]) if obj.get("fabric") is not None else None,
            "slug": obj.get("slug"),
            "name": obj.get("name"),
            "java": obj.get("java"),
            "memory": obj.get("memory"),
            "public": obj.get("public"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "versions": [BuildVersion.from_dict(_item) for _item in obj["versions"]] if obj.get("versions") is not None else None
        })
        return _obj

from kleister.models.build_version import BuildVersion
from kleister.models.pack import Pack
# TODO: Rewrite to not use raise_errors
Build.model_rebuild(raise_errors=False)

