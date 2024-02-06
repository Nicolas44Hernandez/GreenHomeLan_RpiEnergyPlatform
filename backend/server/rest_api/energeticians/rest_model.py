"""REST API models for Zones management package"""

from marshmallow import Schema
from marshmallow.fields import Str


class EnergeticiansSchema(Schema):
    """REST ressource for Energeticians schema"""
    
    energeticians = Str(required=True, allow_none=False, many=True)
    

