from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# =====================
# DATABASE CONFIG
# =====================
DATABASE_URL = "postgresql://flashcard_ar5k_user:hfaIOOniDoWPXHoq4bxVoK5OB6fI0mlA@dpg-d4vcpapr0fns739irq2g-a.virginia-postgres.render.com/flashcard_ar5k"

# =====================
# ENGINE
# =====================
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # tự động reconnect nếu mất kết nối
)

# =====================
# SESSION
# =====================
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# =====================
# BASE MODEL
# =====================
Base = declarative_base()
