from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, crud, database

router = APIRouter(
    prefix="/dosen",
    tags=["Dosen"]
)

@router.get("/list", response_model=list[schemas.Mahasiswa])
def list_mahasiswa(db: Session = Depends(database.get_db)):
    return crud.get_all_mahasiswa(db)

@router.put("/update/{id}", response_model=schemas.Mahasiswa)
def update_status(id, status: schemas.StatusEnum, db: Session = Depends(database.get_db)):
    db_mahasiswa = crud.get_mahasiswa_by_id(db, id)
    if db_mahasiswa is None:
        raise HTTPException(status_code=404, detail="Mahasiswa tidak ditemukan")
    return crud.update_status(db, db_mahasiswa, status)
