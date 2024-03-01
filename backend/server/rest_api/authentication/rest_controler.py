""" REST controller for authentication ressource """
import logging
from flask.views import MethodView
from flask_smorest import Blueprint
from server.common import AdminAuth, ErrorCode, ServerException
from .rest_model import AdminSchema, LoginResponseSchema


logger = logging.getLogger(__name__)

bp = Blueprint("login", __name__, url_prefix="/api/login")
""" The api blueprint. Should be registered in app main api object """


@bp.route("/")
class LoginApi(MethodView):
    """API to login"""

    @bp.doc(security=[{"tokenAuth": []}], responses={400: "BAD_REQUEST", 401: "UNAUTHORIZED"})
    @bp.arguments(AdminSchema, location="query")
    @bp.response(status_code=200, schema=LoginResponseSchema)
    def post(self, args: AdminSchema):
        """
        Login
        """
        logger.info(f"POST /login")

        auth_token = AdminAuth.authenticate(**args)
        if not auth_token:
            raise ServerException(ErrorCode.LOGIN_INVALID_CREDENTIALS_ERROR)

        return {
            "email":args["email"], 
            "password":args["password"], 
            "token":auth_token
        }

