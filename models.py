from flask_sqlalchemy import SQLAlchemy
import bcrypt

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    aadhaar_encrypted = db.Column(db.LargeBinary, nullable=False)

    def set_password(self, pwd):
        self.password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

    def check_password(self, pwd):
        return bcrypt.checkpw(pwd.encode(), self.password.encode())
