from pydantic import (
    BaseModel,
    ValidationError,
    Field,
    AliasChoices,
    field_serializer,
    FieldSerializationInfo,
    ConfigDict,
)
from pydantic.alias_generators import to_camel
from datetime import datetime
from typing import Optional


class AdminBaseModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel,
        validate_assignment=True,
        validate_default=True,
        extra="forbid",
    )


class ResponseModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    id: int
    name_admin : str = Field(
        alias="nameAdmin",
        serialization_alias="nameAdmin",
    )
    email : str
    user_name: str = Field(
        alias="userNameAdmin",
        serialization_alias="userNameAdmin",
    )
    # password: str = Field(min_length=8, max_length=18)
    is_root_admin: bool = Field(
        alias="isRootAdmin",
        serialization_alias="isRootAdmin",
    )
    changer_access : bool = Field(
        alias="changerAccess",
        validation_alias=AliasChoices("ChangerAccess"),
        serialization_alias="changerAccess",
    )


class NewAdminModel(AdminBaseModel):
   
    name_admin : str = Field(
        alias="nameAdmin",
        validation_alias=AliasChoices("NameAdmin", "nAdmin"),
        serialization_alias="nameAdmin",
    )
    email : str
    user_name: str = Field(
        alias="userNameAdmin",
        validation_alias=AliasChoices("UserNameAdmin", "unAdmin"),
        serialization_alias="userNameAdmin",
    )
    password: str = Field(min_length=8, max_length=18)
    is_root_admin: bool = Field(
        alias="isRootAdmin",
        validation_alias=AliasChoices("IsRootAdmin"),
        serialization_alias="isRootAdmin",
    )
    changer_access : bool = Field(
        alias="changerAccess",
        validation_alias=AliasChoices("ChangerAccess"),
        serialization_alias="changerAccess",
    )

class PatchAdmin(AdminBaseModel):
    user_name_admin: Optional[str] = None
    password: Optional[str] = None
