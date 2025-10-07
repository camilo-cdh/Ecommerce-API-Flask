from app.extensions import db
from app.models.product import Product


def seed_products():
    """
    Inserta productos desde un CSV en la base de datos si no existen.

    CSV esperado en 'app/seeds/products.csv' con columnas:
        sku, marca, tipo, nombre, precio, stock

    Cada fila del CSV se convierte en un objeto Product y se inserta
    usando bulk_save_objects para eficiencia.
    """

    # Verificamos si ya hay productos en la tabla
    if Product.query.count() == 0:
        products = []

        # Abrimos el CSV
        with open("app/seeds/products.csv", "r") as productos:
            # Saltamos la primera línea si es encabezado
            primera_linea = productos.readline()

            # Leemos las demás líneas
            lineas = productos.readlines()

            # Procesamos cada línea y creamos objetos Product
            for l in lineas:
                linea = [x.strip() for x in l.split(",")]  # Elimina espacios y saltos de línea
                products.append(
                    Product(
                        sku=linea[0],
                        marca=linea[1],
                        tipo=linea[2],
                        nombre=linea[3],
                        precio=int(linea[4]),
                        stock=int(linea[5][:-1]),
                    )
                )
        # Insertamos todos los productos en la base de datos
        db.session.bulk_save_objects(products)
        db.session.commit()
