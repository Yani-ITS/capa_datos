from usuarios_dao import UsuarioDAO
from usuarios import Usuarios
from logger_base import log



def mostrar_menu(): #muestra un menu de opciones que permite acceder a las distintas funciones

    while True:
        print("""
                1.Listar Usuarios
                2.Agregar Usuario
                3.Actualizar Usuario
                4.Eliminar Usuario
                5.Salir
                """)
        
        respuesta= int(input("Elija una opción: "))
        
        if respuesta == 1:
            usuarios_lista= UsuarioDAO.seleccionar()
            print(usuarios_lista)
            mostrar_menu()
        
        elif respuesta == 2:
            idUser= int(input("Ingrese Id Usuario: "))
            userName= input(" Ingrese Nombre de Usuario: ")
            name= input("Ingrese Nombre: ")
            surname= input("Ingrese Apellido: ")
            contrasenia= input("Ingrese Contraseña: ")
            correo= input("Ingrese Email: ")
            rouli= input("Ingrese Rol: ")
            user= Usuarios(id_usuario=idUser ,username= userName, nombre=name, apellido= surname, contrasenia= contrasenia, 
                           email=correo, rol=rouli)
            usuarios_insertados = UsuarioDAO.insertar(user)
            log.debug(f'Usuarios insertados: {usuarios_insertados}')
            
            mostrar_menu()
            
        elif respuesta == 3:
            idUser= int(input("Ingrese Id Usuario: "))
            userName= input(" Ingrese Nombre de Usuario: ")
            name= input("Ingrese Nombre: ")
            surname= input("Ingrese Apellido: ")
            contrasenia= input("Ingrese Contraseña: ")
            correo= input("Ingrese Email: ")
            rouli= input("Ingrese Rol: ")
            user= Usuarios(id_usuario=idUser, username= userName, nombre=name, apellido= surname, contrasenia= contrasenia, 
                           email=correo, rol=rouli)
            usuario_actualizado = UsuarioDAO.actualizar(user)
            log.debug(f'Usuario actualizado con éxito: {usuario_actualizado}')
            
            mostrar_menu()
            
        elif respuesta== 4:
            idUser= int(input("Ingrese Id Usuario: "))
            user= Usuarios(id_usuario= idUser)
            usuario_eliminado= UsuarioDAO.eliminar(user)
            log.debug(f'Usuario actualizado con éxito: {usuario_eliminado}')
            
            mostrar_menu()
        elif respuesta<1 or respuesta>6:
            print("Respuesta incorrecta, elija una opción válida")   
            mostrar_menu()
             
        elif respuesta==5:
            print("Muchas Gracias. Hasta Pronto.")
            break
        
        
                    
                    
mostrar_menu()