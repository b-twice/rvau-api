import jwt
import base64
from flask import request
from flask_restful import wraps, abort
from app import CLIENT_ID, CLIENT_SECRET

def authenticate(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization', None)
        if not auth:
            abort(401, errors={'code': 'authorization_header_missing', 'description': 'Authorization header is expected'})
        parts = auth.split()

        if parts[0].lower() != 'bearer':
          abort(401, errors={'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'})
        elif len(parts) == 1:
          abort(401, errors={'code': 'invalid_header', 'description': 'Token not found'})
        elif len(parts) > 2:
          abort(401, errors={'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'})

        token = parts[1]
        try:
            payload = jwt.decode(
                token,
                base64.b64decode(CLIENT_SECRET.replace("_","/").replace("-","+")),
                audience=CLIENT_ID
            )
        except jwt.ExpiredSignature:
            abort(401, errors={'code': 'token_expired', 'description': 'token is expired'})
        except jwt.InvalidAudienceError:
            abort(401, errors={'code': 'invalid_audience', 'description': 'incorrect audience, expected: TPZrTRxzqYySVXNwNsokXsFL25cTD1ML'})
        except jwt.DecodeError:
            abort(401, errors={'code': 'token_invalid_signature', 'description': 'token signature is invalid'})

        return func(*args, **kwargs)
        # _request_ctx_stack.top.current_user = user = payload
        # return f(*args, **kwargs)

    return decorated