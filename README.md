# Proyecto Django: CRYPTOPLUS
  

## Descripción

El proyecto es una API desarrollada en Django que utiliza la API de Binance para proporcionar información valiosa sobre las criptomonedas.

El API CRIPTO-BINANCE ofrece las siguientes características principales:

- **Criptomonedas**: Visualización de las diferentes criptomonedas y su precio actual.
- **Histórico**: Funcionalidad para visualizar el gráfico de crecimiento de las criptomonedas.
- **Calculadora de Rendimiento**: Esta funcionalidad permite calcular el rendimiento de las inversiones en criptomonedas.
- **Contacto**: Sección que incluye un formulario de contacto para recibir mensajes.
- **Usuarios**: Esta sección muestra un CRUD para la gestión de los usuarios de la aplicación.


## Endpoints

Las siguientes son las rutas principales proporcionadas por la API. Cada endpoint está destinado a proporcionar las funcionalidades mencionadas.

```plaintext
/users                  [GET, POST]
/users/{id}             [GET, PUT, DELETE]
```

## Desarrollo Local

1. Clonar el repositorio:

```bash
git clone https://github.com/pablolospe/django.git
```

2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

3. Crear y activar un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

4. Realizar las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Ejecutar el servidor localmente:

```bash
python manage.py runserver
```

## Pruebas

Para ejecutar las pruebas, usa el siguiente comando:

```bash
python manage.py test
```

## Despliegue

Las instrucciones para desplegar la API dependerán de tu proveedor de hosting. Por ejemplo, si estás utilizando Heroku, sería necesario tener instalado el CLI de Heroku y seguir los pasos para desplegar una aplicación Django.


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# CryptoPlus

## Descripción

Este proyecto es una API conectada a la plataforma de Binance (api.binance.com) que proporciona información valiosa sobre criptomonedas. Ofrece una experiencia completa en el mundo de las criptomonedas con cuatro solapas principales:

- **Criptomonedas**: Se visualizan las criptomonedas y su precio actual.
- **Histórico**: Muestra el gráfico de crecimiento de las criptomonedas.
- **Calculadora de Rendimiento**: Permite calcular el rendimiento de tus inversiones en criptomonedas.
- **Contacto**: Incluye un formulario de contacto.
- **Usuarios**: Muestra un CRUD de los usuarios de la app.

## Características

### 1. Criptomonedas

En la solapa "Criptomonedas", los usuarios pueden explorar una lista de criptomonedas populares junto con su precio actual en tiempo real. Esta función permite a los inversores y entusiastas de las criptomonedas estar al tanto de las últimas tasas de cambio.

### 2. Histórico

La solapa "Histórico" ofrece un análisis gráfico del crecimiento de las criptomonedas a lo largo del tiempo. Los usuarios pueden visualizar gráficos interactivos que muestran la evolución de los precios, lo que les permite tomar decisiones más informadas sobre sus inversiones.

### 3. Calculadora de Rendimiento

La "Calculadora de Rendimiento" es una herramienta poderosa que permite a los usuarios estimar el rendimiento de sus inversiones en criptomonedas. Puedes ingresar tus datos y obtener una proyección de tus potenciales ganancias o pérdidas.

### 4. Contacto

La solapa "Contacto" proporciona un formulario de contacto que permite a los usuarios ponerse en contacto con nosotros para hacer preguntas, dar retroalimentación o solicitar asistencia.

## Uso

Indica cómo los usuarios pueden utilizar tu API y acceder a estas características. Proporciona ejemplos de código si es necesario.

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
