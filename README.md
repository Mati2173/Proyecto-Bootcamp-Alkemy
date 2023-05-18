# Control De Stock (Proyecto Bootcamp Alkemy)
Este simple proyecto es una aplicación web desarrollada en Django como parte del bootcamp organizado por Alkemy y el gobierno de Salta. El objetivo del proyecto es crear un sistema de control de stock para gestionar productos y proveedores.

## Funcionalidades
El sistema cuenta con las siguietnes funcionalidades principales:
1. **Ingresar un proveedor:** Permite agregar un nuevo proveedor a la base de datos mediante un formulario. Se solicita el nombre, apellido y DNI del proveedor.
2. **Ingresar un producto:** Permite agregar un nuevo producto a la base de datos mediante un formulario. Se solicita el nombre del producto, precio, stock actual y proveedor asociado.
3. **Listar proveedores:** Muestra una tabla con todos los proveedores registrados en la base de datos. Se muestra el nombre, apellido y DNI del proveedor.
4. **Listar productos:** Muestra una tabla con todos los productos registrados en la base de datos. Se muestra el nombre del producto, precio, stock actual y proveedor asociado.

## Tecnologias utilizdas
El proyecto utiliza las siguientes herramientas y tecnologías:
- **Python:** Lenguaje de programación utilizado para implementar la lógica del sistema.
- **Django:** Framework de desarrollo web en Python utilizado para crear la aplicación.
- **Jinja2:** Motor de plantillas utilizado para generar las páginas HTML dinámicamente.
- **Bootstrap:** Framework de CSS utilizado para el diseño y la apariencia visual de la página.

## Requisitos de instalación
Para poder ejecutar el proyecto en tu entorno local, debes tener instalado [**Python**](https://www.python.org/downloads/). Luego, ejecuta el siguiente comando en la terminal para poder instalar los requerimientos del proyecto:
```
pip install -r requirements.txt
```

## Instrucciones de uso
1. Clona o descarga el respositorio en tu computadora.
2. Dentro del directorio del proyecto ejecuta el siguiente comando para inciar el servidor de desarrollo de Django:
```
python manage.py runserver
```
3. Abre tu navegador y ve a esta dirección: http://localhost:8000/
4. Ahora puedes utilizar las diferentes funcionalidades de la aplicación. Cada una está en las siguientes direcciones:
    - Listar productos: http://localhost:8000/products
    - Agregar producto: http://localhost:8000/products/create
    - Listar proveedores: http://localhost:8000/suppliers
    - Agregar proveedor: http://localhost:8000/suppliers/create
