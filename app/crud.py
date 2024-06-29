from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

def get_mahasiswa_by_id(db: Session, id):
    return db.query(models.Mahasiswa).filter(models.Mahasiswa.id == id).first()

def get_mahasiswa_by_nama_slug(db: Session, nama_slug: str):
    return db.query(models.Mahasiswa).filter(models.Mahasiswa.nama.ilike(nama_slug.replace("-", " "))).first()

def get_mahasiswa_by_nama(db: Session, nama: str):
    return db.query(models.Mahasiswa).filter(func.lower(models.Mahasiswa.nama).like(func.lower(f"%{nama}%"))).all()

def get_all_mahasiswa(db: Session):
    return db.query(models.Mahasiswa).all()

def create_mahasiswa(db: Session, mahasiswa: schemas.ResponseMessage):
    db_mahasiswa = models.Mahasiswa(**mahasiswa.dict())
    db.add(db_mahasiswa)
    db.commit()
    db.refresh(db_mahasiswa)
    return {"message": "Pendaftaran telah berhasil"}

def update_mahasiswa(db: Session, db_mahasiswa: models.Mahasiswa, mahasiswa_update: schemas.ResponseMessage):
    for key, value in mahasiswa_update.dict().items():
        setattr(db_mahasiswa, key, value)
    db.commit()
    db.refresh(db_mahasiswa)
    return {"message": "Data berhasil diubah"}

def delete_mahasiswa(db: Session, db_mahasiswa: models.Mahasiswa):
    db.delete(db_mahasiswa)
    db.commit()
    return {"message": "Data berhasil dihapus"}

def update_status(db: Session, db_mahasiswa: models.Mahasiswa, status: schemas.StatusEnum):
    db_mahasiswa.status = status
    db.commit()
    db.refresh(db_mahasiswa)
    return db_mahasiswa
