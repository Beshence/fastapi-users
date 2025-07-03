from fastapi_users.router.auth import get_auth_router
from fastapi_users.router.common import ErrorCode
from fastapi_users.router.register import get_register_router
from fastapi_users.router.reset import get_reset_password_router
from fastapi_users.router.users import get_users_router

__all__ = [
    "ErrorCode",
    "get_auth_router",
    "get_register_router",
    "get_reset_password_router",
    "get_users_router",
]

try:  # pragma: no cover
    from fastapi_users.router.oauth import get_oauth_router  # noqa: F401

    __all__.append("get_oauth_router")
except ModuleNotFoundError:  # pragma: no cover
    pass
