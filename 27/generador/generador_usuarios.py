import random

def generar_usuarios(num_usuarios=20):
    nombres = ['Carlos', 'Sofia', 'Juan', 'Maria', 'Luis', 'Ana', 'David', 'Laura', 'Daniel', 'Lucia', 'Miguel', 'Carmen']
    apellidos = ['Garcia', 'Rodriguez', 'Gonzalez', 'Fernandez', 'Lopez', 'Martinez', 'Sanchez', 'Perez', 'Gomez', 'Ruiz', 'Diaz', 'Hernandez']
    dnis = [random.randint(10000000,99999999) for _ in range(num_usuarios)] # Creamos DNIs aleatorios para los usuarios
    # dnis = [123,1234,12345]
    edades = [random.randint(18,60) for _ in range(num_usuarios)] # Creamos edades aleatorias para los usuarios

    usuarios = []

    for i in range(num_usuarios):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        # dni = random.choice(dnis)
        dnis = random.randint(10000000,99999999)  # Creamos DNIs aleatorios para los usuarios
        usuario = {
            "nombre": f'{nombre} {apellido}',
            "dni": dnis,
            "edad": edades[i]
        }
        usuarios.append(usuario)

    return usuarios

usuarios = generar_usuarios()

for usuario in usuarios:
    print(usuario)