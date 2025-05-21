from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./pos.db"  # ./ assure que le chemin est relatif au fichier python

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # Obligatoire pour SQLite avec SQLAlchemy
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
