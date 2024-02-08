""" REST controller for zones ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.managers.clients_manager import clients_manager_service
from .rest_model import ZonesSchema


logger = logging.getLogger(__name__)

bp = Blueprint("zones", __name__, url_prefix="/api/zones")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class ZonesApi(MethodView):
    """API to retrieve zones list"""

    @bp.doc(responses={400: "BAD_REQUEST", 404: "NOT_FOUND"})
    @bp.response(status_code=200, schema=ZonesSchema)
    def get(self):
        """Get zones list"""

        logger.info(f"GET zones/")

        zones = clients_manager_service.get_zones_list()
        return {"zones": zones}
