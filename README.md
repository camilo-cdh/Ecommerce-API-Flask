<a id="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/camilo-cdh/Ecommerce-API-Flask">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Ecommerce API</h3>

  <p align="center">
    API de ecommerce desarrollada con Flask y SQLAlchemy
    <br />
    <a href="https://github.com/camilo-cdh/Ecommerce-API-Flask"><strong>Explora el repositorio »</strong></a>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li><a href="#sobre-el-proyecto">Sobre el proyecto</a></li>
    <li><a href="#construido-con">Construido con</a></li>
    <li><a href="#instalación">Instalación</a></li> 
    <li><a href="#uso">Uso</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#autor">Autor</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## Sobre el proyecto

API desarrollada con **Flask** y **SQLAlchemy** para manejar información de productos.  
Incluye:
- Listado de productos con paginación.
- Filtros por marca, tipo y rango de precios.
- Endpoint para obtener producto por SKU.
- Estructura modular y escalable.
- Manejadores de errores personalizados.

Por defecto, la API está configurada en modo **Development**, lista para ejecutarse con **SQLite** sin necesidad de configuración extra. Además, carga inicialmente la tabla producto con una base de ejemplo de 75 productos.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


## Construido con

* [![Python][Python]][Python-url]
* [![Flask][Flask]][Flask-url]
* [![SQLAlchemy][SQLAlchemy]][SQLAlchemy-url]
* [![MySQL][MySQL]][MySQL-url]
* [![SQLite][SQLite]][SQLite-url]

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- Installation -->
## Instalación

1. Clonar el repositorio
   ```sh
    git clone https://github.com/camilo-cdh/Ecommerce-API-Flask.git
   ```
2. Crear y activar entorno virtual
   ```sh
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En Linux/Mac
    source venv/bin/activate
    ```

3. Instalar dependencias
   ```sh
    pip install -r requirements.txt
    ```

4. Configurar variables de entorno
    ```sh

    Crear un archivo .env en la raíz con el siguiente contenido:

    # Variables para SQLite (por defecto)
    DATABASE_PATH=./
    DATABASE_NAME=ecommerce.db
    
    # Variables para MySQL (para producción)
    DB_USER=usuario
    DB_PASSWORD=contraseña
    DB_HOST=localhost
    DB_NAME=ecommerce
    ```

5. Ejecutar la aplicación
    ```sh
    python run.py
    ```

La API se ejecutará por defecto en:
👉 http://127.0.0.1:5000/products

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- USAGE EXAMPLES -->
## Uso

### Ejemplos de endpoints

* Listar productos (con filtros y paginación)
    ```sh
    GET /products/?marca=samsung&precio_min=100&page=1&per_page=5
    ```

* Obtener producto por SKU
    ```sh
    GET /products/<sku>
    ```

### La API responde con un JSON que incluye:

* Estado (status)

* Resultados (data)

* Metadatos (metadata)

* Paginación (pagination)

* Enlaces de navegación (links)

### Ejemplo de JSON
```sh
{
"data": [
    {
    "id": 13,
    "marca": "Samsung",
    "nombre": "Samsung Galaxy A52S 5G 128 Gb Negro",
    "precio": 314,
    "sku": "EQ7642325013",
    "stock": 8,
    "tipo": "Equipos"
    }
],
"links": {
    "next": "http://127.0.0.1:5000/products/?marca=samsung&per_page=1&precio_min=100&precio_max=1000&page=3",
    "prev": "http://127.0.0.1:5000/products/?marca=samsung&per_page=1&precio_min=100&precio_max=1000&page=1",
    "self": "http://127.0.0.1:5000/products/?marca=samsung&per_page=1&precio_min=100&precio_max=1000&page=2"
},
"metadata": {
    "api_version": "1.0",
    "endpoint": "/products/",
    "filters": {
    "marca": "samsung",
    "precio_max": 1000,
    "precio_min": 100,
    "tipo": null
    },
    "query_params": {
    "marca": "samsung",
    "page": "2",
    "per_page": "1",
    "precio_max": "1000",
    "precio_min": "100"
    },
    "timestamp": "2025-10-04T06:07:40.966Z"
},
"pagination": {
    "has_next": true,
    "has_prev": true,
    "page": 2,
    "per_page": 1,
    "total": 6,
    "total_pages": 6
},
"results": 1,
"status": {
    "code": 200,
    "message": "success"
}
}
```

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Estructura base Flask con Blueprints
- [x] Modelos y seeding automático con CSV
- [x] Filtros y paginación en endpoints
- [x] Manejadores de errores personalizados
- [ ] Agregar tablas: Users, Purchases
- [ ] Agregar Logins
- [ ] Hash seguro de contraseñas
- [ ] Autenticación con JWT
- [ ] Validaciones con Marshmallow
- [ ] Testing con Pytest
- [ ] Migraciones con Flask-Migrate / Alembic

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<!-- AUTHORS -->
## Autor

* **Camilo Diaz** - *Backend Developer* - [Camilo-cdh](https://github.com/camilo-cdh/)

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<!-- CONTACT -->
## Contacto

[![LinkedIn][linkedin-shield]][linkedin-url]
[![Gmail][gmail-shield]][gmail-url]
[![GitHub][github-shield]][github-url]

🔗 Proyecto: [https://github.com/camilo-cdh/Ecommerce-API-Flask](https://github.com/camilo-cdh/Ecommerce-API-Flask)

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->

[Python]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/stable/
[MySQL]: https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white
[MySQL-url]: https://www.mysql.com/
[SQLite]: https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://sqlite.org/
[SQLAlchemy]: https://img.shields.io/badge/sqlalchemy-778877?style=for-the-badge&logo=sqlalchemy&logoColor=white
[SQLAlchemy-url]: https://www.sqlalchemy.org/
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/camilo-diaz-huenchuman/
[gmail-shield]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[gmail-url]: mailto:camilo.cdh.dev@gmail.com
[github-shield]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/camilo-cdh



