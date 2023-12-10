# Proyecto Django: CRYPTOPLUS
  
  ![Imagen_home](./django_uno/static/images/1-home-b.png)

## Descripción

El proyecto CRYPTOPLUS es una aplicación web completa desarrollada en Django, que interactúa con la API de Binance para proporcionar información valiosa sobre las criptomonedas. Aparte de consumir y procesar datos criptográficos, también se gestiona un frontend propio y proporciona funcionalidades de administración y gestión de usuarios a través de Django.

Las principales funcionalidades de CryptoPlus incluyen:

- **Criptomonedas**: Visualización de las diferentes criptomonedas y su precio actual.
- **Histórico**: Funcionalidad para visualizar el gráfico de crecimiento de las criptomonedas.
- **Calculadora de Rendimiento**: Esta funcionalidad permite calcular el rendimiento de las inversiones en criptomonedas.
- **Contacto**: Sección que incluye un formulario de contacto para recibir mensajes.
- **Gestión de Usuarios**: A través del panel de Django admin, los usuarios pueden ser añadidos, editados y eliminados.


## Endpoints

Las siguientes son las rutas principales proporcionadas por la API. Cada endpoint está destinado a proporcionar las funcionalidades mencionadas.

```plaintext
https://ligarcia7.pythonanywhere.com/user/api-user/                 [GET, POST]
https://ligarcia7.pythonanywhere.com/user/api-user/{id}             [GET, PUT, DELETE]

/user/api-user/                 [GET, POST]
/user/api-user/{id}             [GET, PUT, DELETE]
```

## Desarrollo Local

1. Clonar el repositorio:

```bash
git clone <url_de_tu_repositorio>
```

2. Navegar al directorio del proyecto:

```bash
cd django_uno
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Crear y activar un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

5. Realizar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Ejecutar el servidor localmente:

```bash
python manage.py runserver
```

## Pruebas

Para ejecutar las pruebas, usa el siguiente comando:

```bash
python manage.py test
```

## Estructura de los archivos
```
django
├── README.md
├── .vscode
|   └── settings.json
└── django_uno
    ├── users
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── templates
    │   │   ├── vino_create.html
    │   │   ├── vino_delete.html
    │   │   ├── vino_detail.html
    │   │   └── vinos.html
    │   ├── urls.py
    │   └── views.py
    ├── manage.py
    ├── static
    │   ├── css
    │   │   └── main.css
    │   ├── imgs
    │   │   ├── fire.webp
    │   │   ├── landing.webp
    │   │   └── linux.png
    │   └── js
    │       ├── main.js
    │       └── vueScript.js
    ├── templates
    │   ├── base_vinoteca.html
    │   └── index.html
    └── vinoteca
        ├── asgi.py
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── views.py
        └── wsgi.py
```
## Horas extras

Si tienes alguna mejora o característica adicional que quisieras ver implementada, no dudes en contribuir al proyecto o ponte en contacto con nosotros a través de la página de contacto.


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Frontend

## Características

### 1. Criptomonedas

En la solapa "Criptomonedas", los usuarios pueden explorar una lista de criptomonedas populares junto con su precio actual en tiempo real. Esta función permite a los inversores y entusiastas de las criptomonedas estar al tanto de las últimas tasas de cambio. Clickeando los íconos, animados a traves de la función hover, somos redireccionados a la página de cada criptomoneda.

### 2. Histórico

La solapa "Histórico" ofrece un análisis gráfico del crecimiento de las criptomonedas a lo largo del tiempo. Los usuarios pueden visualizar gráficos interactivos que muestran la evolución de los precios, lo que les permite tomar decisiones más informadas sobre sus inversiones.

### 3. Calculadora de Rendimiento

La "Calculadora de Rendimiento" es una herramienta poderosa que permite a los usuarios estimar el rendimiento de sus inversiones en criptomonedas. Puedes ingresar tus datos y obtener una proyección de tus potenciales ganancias o pérdidas.

### 4. Contacto

La solapa "Contacto" proporciona un formulario de contacto que permite a los usuarios ponerse en contacto con nosotros para hacer preguntas, dar retroalimentación o solicitar asistencia.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz Fork del repositorio
2. Clona tu repositorio fork
3. Crea una rama para tu contribución (`git checkout -b feature/nueva-caracteristica`)
4. Realiza tus cambios y commitea (`git commit -m 'Añadida nueva característica'`)
5. Haz push a tu rama (`git push origin feature/nueva-caracteristica`)
6. Crea un pull request


Este proyecto es una valiosa herramienta para cualquiera interesado en el mercado de criptomonedas, ya sea un inversor experimentado o alguien que está comenzando. ¡Explora las características, realiza un seguimiento de tus inversiones y mantente en contacto con nosotros!

¡Gracias por usar nuestro servicio de criptomonedas!

# Django

## Despliegue en PythonAnywhere

Este proyecto ya ha sido desplegado en PythonAnywhere, que es una plataforma de alojamiento en la nube popular para aplicaciones web Python.

Puedes acceder a la aplicación en funcionamiento en [http://ligarcia7.pythonanywhere.com](http://ligarcia7.pythonanywhere.com). Aquí puedes interactuar con todas las funcionalidades en un entorno de producción. Además nos brinda los endpoints de la API.

```plaintext
https://ligarcia7.pythonanywhere.com/user/api-user/                 [GET, POST]
https://ligarcia7.pythonanywhere.com/user/api-user/{id}             [GET, PUT, DELETE]
```

El despliegue en PythonAnywhere asegura que la aplicación esté disponible 24/7, con un rendimiento fiable y rápido.

Fue usado "Manual Configuration" (Configuración manual) en PythonAnywhere para asegurar un control total sobre cómo se ejecuta la aplicación, y se realizó una serie de ajustes importantes para adaptar la configuración a un entorno de producción. Esto incluye la configuración de archivos estáticos para permitir a la aplicación servir sus propios archivos estáticos.

Para cualquier problemática relacionada con el despliegue en PythonAnywhere, no dudes en abrir un issue en este repositorio o contactarme directamente.

## Views

![Imagen_home](./django_uno/static/images/2-Historico.png)
![Imagen_home](./django_uno/static/images/3-Yield.png)
![Imagen_home](./django_uno/static/images/4-form.png)
![Imagen_home](./django_uno/static/images/5-UsuariosGET.png)
![Imagen_home](./django_uno/static/images/6-UsuariosCREATE.png)
![Imagen_home](./django_uno/static/images/7-UsuariosUpdate.png)
![Imagen_home](./django_uno/static/images/8-UsuariosDelete.png)
