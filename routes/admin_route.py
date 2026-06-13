from fastapi import APIRouter, HTTPException, Depends
from schema.admin_schema import NewAdminModel, ResponseModel, PatchAdmin
from datetime import datetime

router = APIRouter(prefix="/api/admin", tags=["admin"])


data = {
    "1": {
        "user_name_admin": "ali1214",
        "password": "112345aliW",
        "created_at": "2026-06-13 10:26:21",
    }
}


@router.get("/", response_model=dict[str, ResponseModel])
def get_admin():
    return data


@router.post("/new_admin", response_model=ResponseModel)
def create_admin(admin_new: NewAdminModel):
    admin_new.created_at = datetime.now()
    new_id = str(len(data) + 1)
    data[new_id] = admin_new.model_dump(mode="json")
    return data[new_id]


@router.patch("/update-admin/{id:str}", response_model=ResponseModel)
def update_admin_by_id(id: str, patch_admin: PatchAdmin):
    data[id].update(patch_admin.model_dump(exclude_unset=True))

    return data[id]
