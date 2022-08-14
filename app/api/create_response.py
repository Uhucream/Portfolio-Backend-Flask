from typing import Optional
from flask import current_app, Response

def create_response(content: str, status_code: int, mimetype: Optional[str] = None) -> Response:

    response = current_app.response_class(
        response='\n{}\n'.format(content),
        status=status_code,
        mimetype=mimetype or 'application/json;charset=UTF-8'
    )
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['X-Frame-Options'] = 'deny'

    return response
