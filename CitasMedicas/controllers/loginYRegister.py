from database import conectado
conexion = conectado()
my = conexion.cursor()
class LoginYRegistro():
    def __init__(self):
        pass
        # Consulta a la base de datos de si encuentra el usuario y devuelve confirmación si si
    def login(self,usuario,contrasenia): 
        my.reset()
        my.execute("SELECT id from usuarios where usuario = %s and contrasenia = %s",(usuario,contrasenia))
        resultado=my.fetchall()
        if resultado:
            return {'id':resultado[0][0]}
        else:
            return {'id':False}
        # Insertar nuevos datos de un usuario en la base de datos y asi poder pasar el login
    def register(self,nombre,apellidos,dni,fechaNacimiento,usuario,contrasenia):
        
        my.execute("SELECT id from usuarios WHERE usuario = %s or (usuario= %s and contrasenia=%s)",(usuario,usuario,contrasenia))
        if not my.fetchall():
            my.execute("""INSERT INTO datos_usuarios(nombre,apellidos,dni,fechaNacimiento)
                       VALUES (%s,%s,%s,%s)""",(nombre,apellidos,dni,fechaNacimiento))
            id = my.lastrowid
            my.execute("""INSERT INTO usuarios(id,usuario,contrasenia)
                       VALUES (%s,%s,%s)""",(id,usuario,contrasenia))
            conexion.commit()
            return {"estado":True}
        else:
            return{"estado" : False}
    def recuperar(self,a):
        pass