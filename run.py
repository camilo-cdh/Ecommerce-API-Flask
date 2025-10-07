"""
Archivo principal para ejecutar la aplicación Flask.
Inicializa la app llamando a create_app() y la ejecuta.
"""

from app import create_app

# Crear la instancia de la aplicación
app = create_app()

# Ejecutar la app solo si este archivo se ejecuta directamente
if __name__ == "__main__":
    app.run()
