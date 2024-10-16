# Ecommerce 

## Descripción del Proyecto

Este es un proyecto de aplicación web Fullstack de Ecommerce, construido utilizando **Django** para el backend y **Bootstrap** para el frontend. La aplicación permite a los usuarios navegar por productos, agregar artículos al carrito, realizar pedidos y gestionar el inventario. Además, incluye un sistema de autenticación de usuarios, filtros por categorías, y el panel de administraciónpor defecto para la gestión de categorías, productos y pedidos.

## Tablas y relaciones necesarias

Consultar documento [Diseño Base de Datos](https://github.com/Jhonatanls/Stone-Marketplace/blob/main/Dise%C3%B1o%20de%20la%20Base%20de%20Datos.pdf)

## Características Principales

- **Autenticación de usuarios**: Registro, inicio de sesión y cierre de sesión.
- **Control de inventario**: Gestión de productos (crear, editar, eliminar) y control de stock.
- **Carrito de compras**: Los usuarios pueden agregar, actualizar y eliminar productos del carrito.
- **Órdenes de compra**: Los usuarios pueden realizar órdenes de compra, pagar con la Api Sandbox de Paypal para simular pagos.
- **Filtros por categorías**: Los productos se pueden filtrar por categorías específicas.
- **Interfaz responsiva**: Interfaz de usuario diseñada con Bootstrap para ser compatible con dispositivos móviles y de escritorio.

## Tecnologías Utilizadas

- **Backend**:
  - Django 5.1.2
  - SQLite (base de datos por defecto)
  
- **Frontend**:
  - Bootstrap 5.x
  - HTML5, CSS3
  - JavaScript

## Instalación y Configuración

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/Jhonatanls/Stone-Marketplace.git
   cd Stone-Marketplace
   python3 -m venv env
   env/bin/activate
   pip install -r requirements.txt
   python manage.py runserver

2. **Ejecución de imágen Docker**
   ```bash
   docker pull jhonatan25ls/stone-marketplace:latest 
   docker run -p 8000:8000 jhonatan25ls/stone-marketplace:latest
   Se deberá abrir localhost:8000 y la aplicación correrá

## Uso de la Aplicación
### Navegación General
- Los usuarios pueden navegar por las diferentes categorías de productos.
- Los productos se pueden agregar al carrito, y desde allí pueden proceder a realizar una compra.
- Se puede filtrar productos por diferentes categorías usando el menú de navegación.

### Carrito de Compras
- Una vez que el usuario confirma una compra, se genera una orden que queda registrada en su historial.
- Los administradores pueden gestionar las órdenes de compra desde el panel de administración de Django.

## Panel de Administración
- El administrador puede gestionar los productos, categorías, y controlar el inventario.
- Se pueden crear, editar o eliminar productos.
- Se puede controlar el stock y las órdenes de compra desde la interfaz de administración.

## Próximas Mejoras
- Funcionalidad de reseñas de productos.
- Migrar la base de datos a una más potente como PostgreSQL o MySQL.
- Implementación de procedimientos almacenados, indices y restricciones mencionados en el documento del [diseño de la base de datos.](https://github.com/Jhonatanls/Stone-Marketplace/blob/main/Dise%C3%B1o%20de%20la%20Base%20de%20Datos.pdf)
- Logging y test unitarios y de integración
- Despliegue de la aplicación y/o Dockerización
