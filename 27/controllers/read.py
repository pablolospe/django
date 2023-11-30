def read_user(dni:int, db_user:list = None)->None:
    if db_user is None:
        print("no pasaste una database")
        return None
    
    user_list:list = [
    print(user) or user  # Esta línea imprimirá cada 'user'
    for user in db_user
    if isinstance(user, dict) and user.get("dni") == dni
]
    print(len(user_list))

    if len(user_list)==0:
        return {}

    user:dict = user_list[0]
    print(
        f"""
        El usuario buscado es: 
            {user.get("nombre")} de {user.get("edad")} años.
        """
    )
    return user