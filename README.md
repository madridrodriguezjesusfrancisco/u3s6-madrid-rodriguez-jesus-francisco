# U3S6 — Autenticación, sesiones y seguridad

Aplicación web desarrollada con Django para administrar servicios con cuentas de usuario. Cada persona puede consultar y modificar únicamente los servicios que le pertenecen.

## Demo

[Ver aplicación en Render](https://u3s6-madrid-rodriguez-jesus-francisco.onrender.com)

## Funcionalidades

- Registro de usuarios.
- Inicio y cierre de sesión.
- Creación, consulta, edición y eliminación de servicios.
- Aislamiento de registros por propietario.
- Protección de vistas para usuarios autenticados.
- Validación de contraseñas y gestión de sesiones mediante Django.

## Tecnologías

- Python
- Django
- MySQL en Aiven
- Tailwind CSS
- Gunicorn y WhiteNoise

## Ejecutar en local

1. Clona el repositorio y entra en la carpeta:

   ```powershell
   git clone https://github.com/madridrodriguezjesusfrancisco/u3s6-madrid-rodriguez-jesus-francisco.git
   cd u3s6-madrid-rodriguez-jesus-francisco
