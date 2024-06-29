from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional
from .models import StatusEnum

class MahasiswaBase(BaseModel):
    nama: str
    npm: str
    judul: str
    dosen_pembimbing: str
    tanggal_sidang: date
    no_telp: str
    email: EmailStr

class MahasiswaCreate(MahasiswaBase):
    pass

class MahasiswaUpdate(MahasiswaBase):
    pass

class Mahasiswa(MahasiswaBase):
    id: int
    status: StatusEnum

    class Config:
        from_attributes = True

class ResponseMessage(BaseModel):
    message: str