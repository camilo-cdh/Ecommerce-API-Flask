from app.extensions import db


class Product(db.Model):

    # Modelo de producto para la base de datos.

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(30), unique=True, nullable=False)  # Código SKU único
    nombre = db.Column(db.String(100), nullable=False)  # Nombre del producto
    marca = db.Column(db.String(30), nullable=False)  # Marca a la que pertenece
    tipo = db.Column(db.String(30), nullable=False)  # Tipo o categoría
    precio = db.Column(db.Integer, nullable=False)  # Precio en la moneda local
    stock = db.Column(db.Integer, default=0)  # Cantidad en inventario, por defecto 0

    def to_json(self):

        # Convierte el objeto Product en un diccionario JSON listo para la API.
        # Retorna: dict, representación del producto.

        product = {
            "id": self.id,
            "sku": self.sku,
            "nombre": self.nombre,
            "marca": self.marca,
            "tipo": self.tipo,
            "precio": self.precio,
            "stock": self.stock,
        }
        return product
