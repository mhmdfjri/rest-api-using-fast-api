from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(
    tags=["Cek Kelulusan"]
)

@router.get("/cek-kelulusan", response_model=list[schemas.Mahasiswa])
def cek_kelulusan(db: Session = Depends(database.get_db)):
    return crud.get_all_mahasiswa(db)
@router.get("/cek-kelulusan/search", response_model=list[schemas.Mahasiswa])
def cek_kelulusan(nama: str = Query(..., description="Nama Mahasiswa"), db: Session = Depends(database.get_db)):
    return crud.get_mahasiswa_by_nama(db, nama)