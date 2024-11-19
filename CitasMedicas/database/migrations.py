from database.conexion import conectado

def migraciones():
    conexion = conectado()
    my = conexion.cursor()

    my.execute("SHOW TABLES LIKE 'datos_usuarios'")
    if not my.fetchone():
        my.execute("""CREATE TABLE datos_usuarios(
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   nombre VARCHAR(255) NOT NULL,
                   apellidos VARCHAR(255) NOT NULL,
                   dni VARCHAR(255) NOT NULL,
                   fechaNacimiento DATE NOT NULL
                   )""")
        print("Se ha creado la tabla datos_usuarios")
    else:
        print("Ya existe la tabla datos de usuarios")

    my.execute("SHOW TABLES LIKE 'usuarios'")
    if not my.fetchone():
        my.execute("""CREATE TABLE usuarios (
        id INT PRIMARY KEY,
        usuario VARCHAR(255) NOT NULL,
        contrasenia VARCHAR(255) NOT NULL,
        FOREIGN KEY (id) REFERENCES datos_usuarios(id)
    )
""")

        print("Se ha creado correctamente la tabla usuarios")
    else:
        print("Ya existe la tabla usuarios")

