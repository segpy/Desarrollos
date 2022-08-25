from getpass import getpass
import mysql.connector

def main():
    user = input('Usuario: ')
    passw = getpass('Password: ')
    if verificarUsuario(user, passw):
        print('Bienvenido')
    else:
        print('Usuario o contraseña incorrectos')
    """ usercrear = input('Usuario a crear: ')
    passwcrear = getpass('Password a crear: ')
    crearUsuario(usercrear, passwcrear) """
    usuarios = leerUsuarios()
    for usuario in usuarios:
        print(usuario)
    usuarioeliminar = input('Usuario a eliminar: ')

def verificarUsuario(usuario, password):
    # Conexión a la base de datos
    conexion = mysql.connector.connect(user='root', password='123456789', host='localhost', database='miconexion')
    cursor = conexion.cursor()

    # Consulta a la base de datos
    consulta = 'SELECT * FROM users WHERE usuario = %s AND clave = %s'
    cursor.execute(consulta, (usuario, password))
    resultado = cursor.fetchone()
    conexion.close()
    if resultado:
        return True
    else:
        return False

def crearUsuario(usuario, password):
    # Conexión a la base de datos
    conexion = mysql.connector.connect(user='root', password='123456789', host='localhost', database='miconexion')
    cursor = conexion.cursor()

    # Consulta a la base de datos
    consulta = 'INSERT INTO users (usuario, clave) VALUES (%s, %s)'
    cursor.execute(consulta, (usuario, password))
    conexion.commit()
    conexion.close()
    print('Usuario creado')

def eliminarUsuario(usuario):
    # Conexión a la base de datos
    conexion = mysql.connector.connect(user='root', password='123456789', host='localhost', database='miconexion')
    cursor = conexion.cursor()

    # Consulta a la base de datos
    consulta = 'DELETE FROM users WHERE usuario = %s'
    cursor.execute(consulta, (usuario))
    conexion.commit()
    conexion.close()
    print('Usuario eliminado')

def actualizarUsuario(usuario, password):
    # Conexión a la base de datos
    conexion = mysql.connector.connect(user='root', password='123456789', host='localhost', database='miconexion')
    cursor = conexion.cursor()

    # Consulta a la base de datos
    consulta = 'UPDATE users SET clave = %s WHERE usuario = %s'
    cursor.execute(consulta, (password, usuario))
    conexion.commit()
    conexion.close()
    print('Usuario actualizado')

def leerUsuarios():
    # Conexión a la base de datos
    conexion = mysql.connector.connect(
    user='root', password='123456789', host='localhost', database='miconexion')
    cursor = conexion.cursor()

    # Consulta a la base de datos
    consulta = 'SELECT * FROM users'
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    conexion.close()
    return resultado

if __name__ == '__main__':
    main()