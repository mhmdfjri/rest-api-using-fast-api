from sqlalchemy import Column, Integer, String, Date, Enum
from .database import Base
import enum

class StatusEnum(enum.Enum):
    sudah_daftar = "Sudah Daftar"
    lulus = "Lulus"
    tidak_lulus = "Tidak Lulus"

class Mahasiswa(Base):
    __tablename__ = "mahasiswa"

    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    npm = Column(String, unique=True, index=True)
    dosen_pembimbing = Column(String, index=True)
    judul = Column(String, index=True)
    tanggal_sidang = Column(Date)
    no_telp = Column(String, index=True)
    email = Column(String, index=True)
    status = Column(Enum(StatusEnum), default=StatusEnum.sudah_daftar)
