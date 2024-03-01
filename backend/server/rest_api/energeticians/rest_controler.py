""" REST controller for energeticians ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.common.authentication.service import token_required
from server.managers.clients_manager import clients_manager_service
from .rest_model import EnergeticiansSchema


logger = logging.getLogger(__name__)

bp = Blueprint("energeticians", __name__, url_prefix="/api/energeticians")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class EnergeticiansApi(MethodView):
    """API to retrieve energeticians list"""
    
    @token_required
    @bp.doc(responses={400: "BAD_REQUEST", 404: "NOT_FOUND"})
    @bp.response(status_code=200, schema=EnergeticiansSchema)
    def get(self):
        """Get energeticians list"""

        logger.info(f"GET energeticians/")

        energeticians = clients_manager_service.get_energeticians_list()
        return {"energeticians": energeticians}
