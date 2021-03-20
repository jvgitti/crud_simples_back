from sqlalchemy import Column, String, BigInteger
from server import db
from server import ma

class Usuario(db.Model):
    __tablename__ = "tb_usuario"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nm_usuario = Column(String)
    email_usuario = Column(String)

class UsuarioSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "id",
            "nm_usuario",
            "email_usuario"
        )