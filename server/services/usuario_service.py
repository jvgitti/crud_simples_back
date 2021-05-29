from server.models.usuario import UsuarioSchema
from server.models.usuario import Usuario
from server import db

def adiciona_usuario(body):
    usuario = Usuario()
    usuario.nm_usuario = body['nm_usuario']
    usuario.senha_usuario = body['senha_usuario']
    try:
        db.session.add(usuario)
        db.session.commit()
    except:
        db.session.rollback()
    rett = UsuarioSchema(many=False).jsonify(usuario)
    return rett


def retorna_usuarios():
    usuario = Usuario()
    usuario = usuario.query.all()
    rett = UsuarioSchema(many=True).jsonify(usuario)
    return rett

def deleta_usuario(id):
    usuario = Usuario()
    usuario = usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return "Ok"
