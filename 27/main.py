from generador import generar_usuarios
from controllers.create import create_user
from controllers.read import read_user
from controllers.update import update_user
from controllers.delete import delete_user
## Funciones
def greeting(param)->None:
    print('hola ' + param)

greeting('pol')


usuarios_venta = generar_usuarios(12)
usuarios_dev = generar_usuarios()

print(usuarios_venta)
# for usuario in usuarios:
#     print(usuario)

#CRUD

"""
saber que quiere hacer el usuario 
get_orden_del_crud()
{
    create_user ?
    read_user ?
    update_user ?
    delete_user?
}
deseas_hacer_otra_operación?

"""
def main():
    opcion:str = input(f"""
        Bienvenido
        Que desea hacer
          - a => crear
          - b => leer
          - c => modificar
          - d => borrar
        """)
    if opcion == "a":
        nombre:str = input("ingrese nombre\n")
        dni = int(input("ingrese dni\n"))
        edad = int(input("ingrese edad\n"))
        create_user(nombre, dni, edad, usuarios_venta)
        print(usuarios_venta)
        return
    
    if opcion == "b":
        dni = int(input("ingrese dni\n"))
        read_user(dni, usuarios_venta)
        return
    
    if opcion == "c":
        dni = int(input("ingrese dni\n"))
        update_user(dni, usuarios_venta)
        
        return
    
    if opcion == "d":
        dni = int(input("ingrese dni\n"))
        delete_user(dni, usuarios_venta)
        print(usuarios_venta)
        return
        
main()