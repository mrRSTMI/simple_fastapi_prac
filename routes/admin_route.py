from fastapi import APIRouter, HTTPException, Depends
from schema.admin_schema import NewAdminModel, ResponseModel, PatchAdmin
from datetime import datetime
from models.admin_model_db import Admin
from core.database import get_db
from sqlalchemy.orm import Session
from services.admin_service import get_admin_service,create_admin_service
router = APIRouter(prefix="/api/admin", tags=["admin"])


data = {
    "1": {
        "user_name_admin": "ali1214",
        "password": "112345aliW",
        "created_at": "2026-06-13 10:26:21",
    }
}
# , response_model=dict[str, ResponseModel]

@router.get("/", response_model=list[ResponseModel])
def get_admin(skip:int= 0, limit: int = 100 ,db: Session = Depends(get_db)):
    return get_admin_service(skip=skip, limit=limit,db=db)


@router.post("/new_admin",response_model=ResponseModel)
def create_admin(admin_new: NewAdminModel, db: Session = Depends(get_db)):
    return create_admin_service(admin_new=admin_new,db=db)


@router.patch("/update-admin/{id:str}", response_model=ResponseModel)
def update_admin_by_id(id: str, patch_admin: PatchAdmin):
    data[id].update(patch_admin.model_dump(exclude_unset=True))
    return data[id]


@router.delete("/delete-admin/{id:str}")
def delete_admin_by_id(id:str):
    data.pop(id)
    return {"message": f"deleted admin by id: {id}"}