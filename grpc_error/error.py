import grpc
from grpc._server import _Context

from grpc_error.exceptions import *


def set_exception(context: _Context, error):
    if error == InvalidArgument:
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details("INVALID_ARGUMENT")
    elif error == AlreadyExists:
        context.set_code(grpc.StatusCode.ALREADY_EXISTS)
        context.set_details("ALREADY_EXISTS")
    elif error == NotFound:
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("NOT_FOUND")
    elif error == UnAuthenticated:
        context.set_code(grpc.StatusCode.UNAUTHENTICATED)
        context.set_details("UNAUTHENTICATED")
    elif error == IncorrectPassword:
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details("INCORRECT_PASSWORD")
    elif error == SamePassword:
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details("SAME_PASSWORD")
