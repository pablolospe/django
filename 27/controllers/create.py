from .read import read_user

def create_user(nombre:str, dni:int, edad:int, db_user:list=None):
    """ 
    Crea nuevo usuario
    nombre:str, dni:int, edad:int, db_user:list=None
    """
    user:dict = {
        "nombre": nombre,
        "dni": dni,
        "edad": edad,
    }
    if db_user is None:
        print("ojo, no hay database")
    
    db_user.append(user)
    print(user)
    read_user(dni, db_user)

    return