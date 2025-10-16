from flask import Blueprint, abort
from app.models import Product
from app.utils import paginate, products_filters, response

# Blueprint para agrupar las rutas de productos
bp = Blueprint("products", __name__, url_prefix="/products")


@bp.route("/", methods=["GET"])
def list_products():
    """
    Endpoint para listar productos con filtros y paginación.

    Query Params opcionales:
        - marca: filtra por marca del producto
        - tipo: filtra por tipo de producto
        - precio_min: filtra por precio mínimo
        - precio_max: filtra por precio máximo
        - page: número de página (para paginación)
        - per_page: cantidad de productos por página

    Retorna:
        JSON con la lista de productos, metadatos y paginación.
    """

    # Query de todos los productos (sin ejecutar aún)
    products = Product.query
    
    # Si la tabla está vacía, devolvemos 404
    if not products.first():
        abort(404, description="No se encontraron productos")

    # Aplicamos filtros opcionales y obtenemos un diccionario con los filtros usados
    products, filters = products_filters(products)

    # Aplicamos paginación
    pagination, pagination_json = paginate(products)

    # Convertimos los productos de la página actual a JSON
    data = [p.to_json() for p in pagination]

    # Construimos el JSON de respuesta con data, metadatos y paginación
    response_json = response(data=data, pagination=pagination_json, filters=filters)

    return response_json, 200


@bp.route("/<string:sku>", methods=["GET"])
def get_product_sku(sku):
    """
    Endpoint para obtener un producto por su SKU.

    Parámetros de URL:
        sku (str): código único del producto

    Retorna:
        JSON con los detalles del producto si se encuentra, o 404 si no existe.
    """

    # Buscamos el producto por SKU
    product = Product.query.filter_by(sku=sku).first()

    # Si no existe, devolvemos 404
    if not product:
        abort(404, description="No se encontro el producto")

    # Convertimos el producto a JSON
    data = {"product": product.to_json()}

    # Construimos el JSON de respuesta
    response_json = response(data=data)

    return response_json, 200
