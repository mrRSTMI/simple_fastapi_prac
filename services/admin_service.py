from models.admin_model_db import Admin
from datetime import datetime
from fastapi import HTTPException


def get_admin_service(db, skip, limit):
    all_admins = db.query(Admin).offset(skip).limit(limit).all()
    return all_admins


def create_admin_service(admin_new, db):
    admin_item = db.query(Admin).filter(Admin.user_name == admin_new.user_name).first()
    if admin_item:
        raise HTTPException(
            status_code=404, detail=f"* * * === your admin is exist === * * *"
        )
    new_admin = Admin(**admin_new.model_dump())
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin


# def update_admin_by_id(id: str, patch_admin: PatchAdmin):
#     data[id].update(patch_admin.model_dump(exclude_unset=True))
#     return data[id]


# def delete_admin_by_id(id:str):
#     data.pop(id)
#     return {"message": f"deleted admin by id: {id}"}
