"""REST API models for Clients management package"""

from marshmallow import Schema
from marshmallow.fields import Str


class ClientSchema(Schema):
    """REST ressource for Clients schema"""
    
    client_id = Str(required=True, allow_none=False)
    zone = Str(required=True, allow_none=False)
    energetician = Str(required=True, allow_none=False)
    id_energetician = Str(required=True, allow_none=False)
    contract_class = Str(required=True, allow_none=False)
    fai = Str(required=True, allow_none=False)
    id_client_fai = Str(required=True, allow_none=False)
    name_client_fai = Str(required=True, allow_none=False)
    ip = Str(required=True, allow_none=False)
    port = Str(required=True, allow_none=False)
    

