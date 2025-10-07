from app.models import Product
from flask import request
from datetime import datetime

def paginate(query):

    """
    Aplica paginación a una consulta SQLAlchemy basada en query params.

    Query params opcionales:
        - page (int): número de página, por defecto 1
        - per_page (int): cantidad de elementos por página, por defecto 10 (máximo 15)

    Args:
        query (SQLAlchemy Query): Consulta de la que se desea obtener resultados paginados.

    Returns:
        items (list): lista de objetos correspondientes a la página solicitada.
        pagination_json (dict): diccionario con información de paginación:
            - page: página actual
            - per_page: elementos por página
            - total: total de elementos en la consulta
            - total_pages: total de páginas disponibles
            - has_next: indica si hay página siguiente
            - has_prev: indica si hay página anterior
    """

    # Obtenemos parámetros de la URL con valores por defecto
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)

    # Validación de los parámetros para evitar valores fuera de rango
    page = max(1, page)
    per_page = min(max(1, per_page), 15)

    # Aplicamos la paginación con SQLAlchemy
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    # Construimos un diccionario con la información de paginación
    pagination_json = {
                "page": pagination.page,
                "per_page": pagination.per_page,
                "total": pagination.total,
                "total_pages": pagination.pages,
                "has_next": pagination.has_next,
                "has_prev": pagination.has_prev
            }
    

    return pagination.items, pagination_json

