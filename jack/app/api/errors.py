from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException
from app.api import bp

def error_resposne(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    return payload, status_code

def bad_request(message):
    return error_resposne(400, message)

@bp.errorhandler(HTTPException)
def handle_exception(e):
    return error_resposne(e.code)