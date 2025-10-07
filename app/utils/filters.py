from app.models import Product
from flask import request
from datetime import datetime

def products_filters(query):

    """
    Aplica filtros a una consulta de productos basada en los query params de la request.

    Query params opcionales:
        - marca (str): filtra productos por marca (insensible a mayúsculas/minúsculas)
        - tipo (str): filtra productos por tipo/categoría
        - precio_min (int): filtra productos con precio >= precio_min
        - precio_max (int): filtra productos con precio <= precio_max

    Args:
        query (SQLAlchemy Query): Consulta inicial de Product.

    Returns:
        query (SQLAlchemy Query): Consulta filtrada según los parámetros.
        filters (dict): Diccionario con los filtros aplicados (útil para metadata en la API).
    """

    # Obtenemos los parámetros de la URL
    marca = request.args.get("marca")
    tipo = request.args.get("tipo")
    precio_min = request.args.get("precio_min", type=int)
    precio_max = request.args.get("precio_max", type=int)

    # Aplicamos filtros solo si se proporcionan
    if marca:
        query = query.filter(Product.marca.ilike(marca))
    if tipo:
        query = query.filter(Product.tipo.ilike(tipo))
    if precio_min is not None:
        query = query.filter(Product.precio >= precio_min)
    if precio_max is not None:
        query = query.filter(Product.precio <= precio_max)

    # Diccionario con los filtros aplicados
    filters = {
            "marca": marca,
            "tipo":tipo,
            "precio_min": precio_min,
            "precio_max": precio_max
        }

    return  query, filters