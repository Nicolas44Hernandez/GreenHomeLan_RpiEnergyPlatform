""" REST controller for clients ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.common.authentication import token_required
from server.managers.clients_manager import clients_manager_service
from .rest_model import ClientSchema


logger = logging.getLogger(__name__)

bp = Blueprint("clients", __name__, url_prefix="/api/clients")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class ClientsApi(MethodView):
    """API to retrieve clients list"""

    @token_required
    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.response(status_code=200, schema=ClientSchema(many=True))
    def get(self):
        """Get clients list"""

        logger.info(f"GET clients/")

        clients = clients_manager_service.get_clients_list()
        return clients
