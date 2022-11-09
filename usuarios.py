class Usuarios:
    def __init__(self,id_usuario, username, nombre, apellido,contrasenia, email, rol ):
        self._username= username
        self._nombre= nombre
        self._apellido= apellido
        self._contrasenia= contrasenia
        self._email= email
        self._rol= rol
        self._id_usuario= id_usuario
        
    def __str__(self):
        return f'''
            Id Usuario: {self.id_usuario}, Username: {self._username}, Nombre: {self.nombre},
            Apellido: {self.apellido}, Email: {self.email}
        '''
        
    @property
    def username (self):
        return self._username
    
    @username.setter
    def username (self, username):
        self._username= username
    
    @property
    def nombre (self):
        return self._nombre
    
    @nombre.setter
    def nombre (self, nombre):
        self._nombre= nombre
        
    @property
    def apellido (self):
        return self._apellido
    
    @apellido.setter
    def apellido (self, apellido):
        self._apellido= apellido    
        
    @property
    def email (self):
        return self._email
    
    @email.setter
    def email (self, email):
        self._email = email
        
    @property
    def rol (self):
        return self._rol
    
    @rol.setter
    def rol (self, rol):
        self._rol= rol
        
    @property
    def contrasenia (self):
        return self._contrasenia
    
    @contrasenia.setter
    def conrasenia (self, contrasenia):
        self._conrasenia = contrasenia
        
    @property 
    def id_usuario (self):
        return self._id_usuario
    
    @id_usuario.setter
    def iduser (self, iduser):
        self._id_usuario= iduser