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
from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from kleister.models.mod import Mod
from kleister.models.team import Team
from typing import Optional, Set
from typing_extensions import Self

class TeamMod(BaseModel):
    """
    Model to represent team mod
    """ # noqa: E501
    team_id: StrictStr
    team: Optional[Team] = None
    mod_id: StrictStr
    mod: Optional[Mod] = None
    perm: Optional[StrictStr] = 'team'
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["team_id", "team", "mod_id", "mod", "perm", "created_at", "updated_at"]

    @field_validator('perm')
    def perm_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['user', 'admin', 'owner']):
            raise ValueError("must be one of enum values ('user', 'admin', 'owner')")
        return value

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
        """Create an instance of TeamMod from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of team
        if self.team:
            _dict['team'] = self.team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mod
        if self.mod:
            _dict['mod'] = self.mod.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TeamMod from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "team_id": obj.get("team_id"),
            "team": Team.from_dict(obj["team"]) if obj.get("team") is not None else None,
            "mod_id": obj.get("mod_id"),
            "mod": Mod.from_dict(obj["mod"]) if obj.get("mod") is not None else None,
            "perm": obj.get("perm") if obj.get("perm") is not None else 'team',
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


