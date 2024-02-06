"""REST API models for Zones management package"""

from marshmallow import Schema
from marshmallow.fields import Str


class ZonesSchema(Schema):
    """REST ressource for Zone schema"""
    
    zones = Str(required=True, allow_none=False, many=True)
    

