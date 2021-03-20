from server.services.usuario_service import adiciona_usuario, retorna_usuarios, deleta_usuario


def post_usuario(body):
    return adiciona_usuario(body)

def get_usuarios():
    return retorna_usuarios()

def delete_usuario(id):
    return deleta_usuario(id)