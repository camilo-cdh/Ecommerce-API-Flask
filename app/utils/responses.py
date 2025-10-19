from flask import request, jsonify
from datetime import datetime, timezone


def response(
    data=None,
    status_code=200,
    message="success",
    pagination=None,
    filters=None,
    api_version="1.0",
    link_self = None
    ):

    """
    Construye un JSON estándar para las respuestas de la API, incluyendo 
    información de estado, datos, metadatos, paginación y links.

    Args:
        data (list/dict, optional): datos a retornar en la respuesta.
        status_code (int, optional): código HTTP de la respuesta (por defecto 200).
        message (str, optional): mensaje de estado (por defecto "success").
        pagination (dict, optional): diccionario con info de paginación (page, has_next, has_prev, etc.).
        filters (dict, optional): filtros aplicados en la consulta.
        api_version (str, optional): versión de la API (por defecto "1.0").
        link_self (str, optional): Link personalizado.

    Returns:
        Response: objeto jsonify listo para enviar como respuesta HTTP.
    """
    
    # Construimos la sección de estado
    status = {
        "code": status_code,
        "message": message
        }

    # Metadata: info de la API, endpoint, filtros, query params y timestamp UTC
    metadata ={
    "api_version": api_version,
    "endpoint": request.path,
    "method": request.method,
    "timestamp":datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    }

    if filters:
        metadata["filters"] = filters
    if request.args:
        metadata["query_params"] = request.args.to_dict()

    # Links de navegación (self, next, prev)
    links = {
        "self":link_self or request.url,
        "next":None,
        "prev":None
        }
    
    # Si se recibe paginación, calculamos next y prev
    if pagination:
        page = pagination.get("page",1)
        next_page = page + 1 if pagination.get("has_next") else None
        prev_page = page - 1 if pagination.get("has_prev") else None

        if next_page:
            args = request.args.to_dict()
            args["page"] = next_page
            links["next"] = f"{request.base_url}?{'&'.join(f'{k}={v}' for k,v in args.items())}"
        if prev_page:
            args = request.args.to_dict()
            args["page"] = prev_page
            links["prev"] = f"{request.base_url}?{'&'.join(f'{k}={v}' for k,v in args.items())}"

    # Construimos el JSON final de la respuesta
    response_json = {
        "status":status,
        "results":len(data) if data else 0,
        "data":data,
        "metadata":metadata,
        }
    
    if pagination:
        response_json["pagination"] = pagination

    if request.method != "DELETE":
        response_json["links"] = links
 
    return jsonify(response_json)


