from conexion import Conexion
from usuarios import Usuarios
from logger_base import log
from cursor_pool import CursorDelPool



class UsuarioDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuarios(username, nombre, apellido, contrasenia, email, rol) VALUES(%s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE usuarios SET username= %s, nombre=%s, apellido=%s, contrasenia= %s , email=%s, rol=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario=%s'
    
    
    @classmethod
    def seleccionar(cls):
            with Conexion.obtenerConexion():
                with CursorDelPool() as cursor:
                    cursor.execute(cls._SELECCIONAR)
                    registro= cursor.fetchall()
                    lista_usuarios=[]
                    """for dato in registro:
                        lista_usuario= Usuarios (dato[0], dato[1], dato[2], dato[3],
                                            dato[4], dato[5], dato[6])"""
                    lista_usuarios.append(registro)
                    return lista_usuarios
                    
            
        
    @classmethod
    def insertar(cls, usuario):
        with Conexion.obtenerConexion():
            with CursorDelPool() as cursor:
                valores = (usuario.username, usuario.nombre, usuario.apellido, usuario.contrasenia, usuario.email, usuario.rol)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Usuario insertado: {usuario}')
                return cursor.rowcount
            
    @classmethod
    def actualizar(cls, usuario):
        with Conexion.obtenerConexion():
           with CursorDelPool() as cursor: 
                valores = ( usuario.username, usuario.nombre, usuario.apellido,
                           usuario.contrasenia, usuario.email, usuario.rol, usuario.id_usuario)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Usuario modificado con éxito: {usuario}')
                return cursor.rowcount
    
    @classmethod
    def eliminar(cls, usuario):
        with Conexion.obtenerConexion():
            with CursorDelPool() as cursor:
                valores = (usuario.id_usuario)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Usuario eliminado')
                return cursor.rowcount

if __name__ == '__main__':
    # Insertar un i
    #user1 = Usuarios (id_usuario= "2", username= 'loki', nombre='Pedro', 
    #                 apellido='Najera',contrasenia= 'lola123', email='pnajera@mail.com', rol='usuario',)
    #usuarios_insertados = UsuarioDAO.insertar(user1)
    #log.debug(f'Usuarios insertados: {usuarios_insertados}')

    # Seleccionar objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuarios)