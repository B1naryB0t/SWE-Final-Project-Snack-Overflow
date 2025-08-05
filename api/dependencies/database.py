from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import DATABASE_URL  

if DATABASE_URL.startswith("mysql"):
    import re
    match = re.match(r"mysql\+pymysql://([^:]+):([^@]+)@([^:/]+):?(\d+)?/([^?]+)", DATABASE_URL)
    if match:
        user, password, host, port, db_name = match.groups()
        port = port or "3306"
        root_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/"
        engine_tmp = create_engine(root_url)
        with engine_tmp.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))  # <-- wrap with text()
        engine_tmp.dispose()
        
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()