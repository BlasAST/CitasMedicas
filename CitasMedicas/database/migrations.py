from database.conexion import conectado

def migraciones():
    my = conectado().cursor()

            
    my.execute("SHOW TABLES LIKE 'datos_usuarios")
    if not my.fetchone():
        my.execute("""CREATE TABLE datos_usuarios(
                   id = INT AUTO_INCREMENT PRIMARY KEY
                   )""")

    my.execute("SHOW TABLES LIKE 'usuarios")
    if not my.fetchone():
        my.execute("""CREATE TABLE usuarios(
                   id INT PRIMARY KEY,
                   usuario VARCHAR(255) NOT NULL,
                   contrasenia VARCHAR(255) NOT NULL,
                   FOREING KEY (id) REFERENCES datos_usuarios(id)
                   )""")
    else:
        print("Ya existe la tabla usuarios")

