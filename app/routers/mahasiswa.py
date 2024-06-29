from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, crud, database

router = APIRouter(
    prefix="/mahasiswa",
    tags=["Mahasiswa"]
)

# @router.post("/register", response_model=schemas.ResponseMessage)
# def daftar_sidang(mahasiswa: schemas.MahasiswaCreate, db: Session = Depends(database.get_db)):
#     if crud.get_mahasiswa_by_npm(db, mahasiswa.npm) or crud.get_mahasiswa_by_no_telp(db, mahasiswa.no_telp) or crud.get_mahasiswa_by_email(db, mahasiswa.email):
#         raise HTTPException(status_code=400, detail="NPM, No Telp atau Email sudah terdaftar")
#     return crud.create_mahasiswa(db, mahasiswa)

@router.post("/register", response_model=schemas.ResponseMessage)
def daftar_sidang(mahasiswa: schemas.MahasiswaCreate, db: Session = Depends(database.get_db)):
    existing_npm = db.query(models.Mahasiswa.npm).all()
    if any(npm[0] == mahasiswa.npm for npm in existing_npm):
        raise HTTPException(status_code=400, detail="NPM sudah terdaftar")
    return crud.create_mahasiswa(db, mahasiswa)

@router.put("/update/{id}", response_model=schemas.ResponseMessage)
def update_sidang(id, mahasiswa: schemas.MahasiswaUpdate, db: Session = Depends(database.get_db)):
    db_mahasiswa = crud.get_mahasiswa_by_id(db, id)
    if db_mahasiswa is None:
        raise HTTPException(status_code=404, detail="Mahasiswa tidak ditemukan")
    return crud.update_mahasiswa(db, db_mahasiswa, mahasiswa)

@router.get("/{nama_slug}", response_model=schemas.MahasiswaCreate)
def get_sidang(nama_slug: str, db: Session = Depends(database.get_db)):
    db_mahasiswa = crud.get_mahasiswa_by_nama_slug(db, nama_slug)
    if db_mahasiswa is None:
        raise HTTPException(status_code=404, detail="Mahasiswa tidak ditemukan")
    return db_mahasiswa

@router.delete("/delete/{id}", response_model=schemas.ResponseMessage)
def delete_sidang(id, db: Session = Depends(database.get_db)):
    db_mahasiswa = crud.get_mahasiswa_by_id(db, id)
    if db_mahasiswa is None:
        raise HTTPException(status_code=404, detail="Mahasiswa tidak ditemukan")
    return crud.delete_mahasiswa(db, db_mahasiswa)
