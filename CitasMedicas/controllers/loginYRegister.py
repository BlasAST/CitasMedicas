from database import conectado
class LoginYRegistro():
    def __init__(self):
        pass

    def login(self,usuario,contrasenia): 
        my = conectado().cursor()
        my.execute("SELECT * from usuarios where nombre = %s and contrasenia = %s",(usuario,contrasenia))
        if my.fetchone():
            return {'resultado':True}
        else:
            return {'resultado':False}
        
    def register(self,nombre,apellidos,dni,fechaNacimiento,usuario,contrasenia,contrasenia2):
        pass

    def recuperar(self,a):
        pass