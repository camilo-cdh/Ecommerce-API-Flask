from app.extensions import db
from flask import request


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
            "stock": self.stock
        }
        return product
    
    @classmethod
    def from_json(cls, data):

        # Recibe un JSON con los datos del producto a crear.
        # Retorna: Product, Modelo de producto para la base de datos.

        product = cls(
            sku = data.get("sku"),
            nombre = data.get("nombre"),
            marca = data.get("marca"),
            tipo = data.get("tipo"),
            precio = data.get("precio"),
            stock = data.get("stock",0)
        )

        return product
    

    def update_from_json(self, data):

        # Recibe un JSON con los datos para actualizar el Producto.
        # Retorna: None.

        ignore_fields = ["id", "sku"]
        attributes = [column.name for column in self.__table__.columns if column.name not in ignore_fields]
        for field, value in data.items():
            if field in attributes:
                setattr(self, field, value)

