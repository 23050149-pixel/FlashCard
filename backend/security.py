import hashlib
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def _normalize_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def hash_mat_khau(mat_khau: str) -> str:
    return pwd_context.hash(_normalize_password(mat_khau))

def verify_mat_khau(mat_khau: str, mat_khau_hash: str) -> bool:
    return pwd_context.verify(
        _normalize_password(mat_khau),
        mat_khau_hash
    )
