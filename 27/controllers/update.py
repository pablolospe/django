from .read import read_user
from .create import create_user

def update_user(dni:int, db_user:list):
    user = read_user(dni, db_user)

    if user == None:
        return
    
    if len(user) == 0:
        print("el user no existe, a crearlo!")
        nombre:str = input("ingresa el nombre\n")
        edad: int = input("ingrese la edad\n")
        create_user(dni, nombre, edad, db_user)
        return
    
    key = input("que valor querés modificar?\n Nombre o edad?\n")
    value = input("ingresa el nuevo valor\n")

    user[key] = value

    for index, user in enumerate(db_user):
        if user["dni"] == dni:
            db_user[index] = user
            print(user)
            
    print("gracias por modificar el user")