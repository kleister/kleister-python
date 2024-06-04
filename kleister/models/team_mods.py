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
from kleister.models.team import Team
from kleister.models.team_mod import TeamMod
from typing import Optional, Set
from typing_extensions import Self

class TeamMods(BaseModel):
    """
    Model to represent team mods
    """ # noqa: E501
    team: Optional[Team] = None
    total: Optional[StrictInt] = None
    mods: Optional[List[TeamMod]] = None
    __properties: ClassVar[List[str]] = ["team", "total", "mods"]

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
        """Create an instance of TeamMods from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of team
        if self.team:
            _dict['team'] = self.team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in mods (list)
        _items = []
        if self.mods:
            for _item in self.mods:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mods'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TeamMods from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "team": Team.from_dict(obj["team"]) if obj.get("team") is not None else None,
            "total": obj.get("total"),
            "mods": [TeamMod.from_dict(_item) for _item in obj["mods"]] if obj.get("mods") is not None else None
        })
        return _obj


