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
    user_name_admin: str
    created_at: datetime


class NewAdminModel(AdminBaseModel):
    user_name_admin: str = Field(
        alias="userNameAdmin",
        validation_alias=AliasChoices("userName", "adminName"),
        serialization_alias="userNameAdmin",
        default="admin",
    )
    password: str
    created_at: datetime | None = None

    @field_serializer("created_at")
    def get_datetime(self, value: datetime, info: FieldSerializationInfo):
        if info.mode == "json":
            return value.strftime("%Y-%m-%d %H:%M:%S")
        return value.isoformat()


class PatchAdmin(AdminBaseModel):
    user_name_admin: Optional[str] = None
    password: Optional[str] = None
    