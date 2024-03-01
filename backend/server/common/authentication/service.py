"""Authentication management package"""
import jwt
import logging
from functools import wraps
from flask import  request, jsonify
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

logger = logging.getLogger(__name__)


class AdminAuth():
    email: str
    password: str
    secret_key: str

    @classmethod
    def create_admin(cls, email:str, password: str, secret_key: str):
        cls.email = email
        cls.secret_key = secret_key
        cls.password = generate_password_hash(password, method='sha256')
        logger.info("Admin created")


    @classmethod
    def authenticate(cls, **kwargs):
        user_email = kwargs.get('email')
        user_password = kwargs.get('password')

        if not user_email or not user_password:
            logger.error("A field is missing")
            return None
        
        if user_email != cls.email:
            logger.error("Invalid email")
            return None
        
        # Validate hashed password
        if not check_password_hash(cls.password, user_password):
            logger.error("Invalid password")
            return None

        logger.info(f"user authenticated: {user_email}")
        token = jwt.encode({
            'sub': user_email,
            'iat':datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(seconds=10)},
            AdminAuth.secret_key,
            algorithm="HS256",
        )
        return token
        

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }

        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(jwt=token, key=AdminAuth.secret_key, algorithms="HS256")
            user_email = data['sub']
            if user_email !=  AdminAuth.email:
                raise RuntimeError('Wrong user')
            return f(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify
