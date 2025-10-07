from flask import Blueprint, jsonify

# Blueprint para manejar errores de la API
errors = Blueprint('errors',__name__)

# Handler para errores 404 (Not Found).
@errors.app_errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Recurso no encontrado"
    }), 404

# Handler para errores 400 (Bad Request).
@errors.app_errorhandler(400)
def bad_request(error):
     return jsonify({
        "status": "error",
        "message": "Solicitud incorrecta"
    }), 400

# Handler para errores 500 (Internal Server Error).
@errors.app_errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "message": "Error interno del servidor"
    }), 500

# Handler genérico para cualquier excepción no controlada.
@errors.app_errorhandler(Exception)
def handle_exception(error):
    return jsonify({
        "status": "error",
        "message": "Ocurrió un error inesperado"
    }), 500

