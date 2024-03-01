"""REST API models for Clients management package"""
from marshmallow import Schema
from marshmallow.fields import Str


class AdminSchema(Schema):
    """REST ressource for Clients schema"""
    
    email = Str(required=True, allow_none=False)
    password = Str(required=True, allow_none=False)


class LoginResponseSchema(Schema):
    """REST ressource for Login response schema"""
    
    email = Str(required=True, allow_none=False)
    password = Str(required=True, allow_none=False)
    token = Str(required=True, allow_none=False)
    

