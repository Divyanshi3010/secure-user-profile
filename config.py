import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root1234@localhost/secure_profile"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "super-secret-jwt-key"
    AES_SECRET_KEY = b'0123456789abcdef0123456789abcdef'  # 32 bytes