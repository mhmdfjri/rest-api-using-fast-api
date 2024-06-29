from app.routers import mahasiswa, dosen, cek_kelulusan
from fastapi import FastAPI
from app.database import engine
import app.models as models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(mahasiswa.router)
app.include_router(dosen.router)
app.include_router(cek_kelulusan.router)
