from .read import read_user

def delete_user(dni:int, db_user:list=None):
    if db_user is None:
        print("no pasaste una database")
        return None
    
    user:dict = read_user(dni, db_user)

    if len(user) == 0:
        print("user no encontrado")
        return
    
    for index, u in enumerate(db_user):
        if u["dni"] == user["dni"]:
            db_user.pop(index)
            break  # Añadido para prevenir errores si hay más de un usuario con el mismo dni

    return