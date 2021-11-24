# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import account_pb2 as proto_dot_account__pb2


class AccountStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.signup = channel.unary_unary(
                '/account.Account/signup',
                request_serializer=proto_dot_account__pb2.CreateAccountRequest.SerializeToString,
                response_deserializer=proto_dot_account__pb2.CreateAccountResponse.FromString,
                )


class AccountServicer(object):
    """Missing associated documentation comment in .proto file."""

    def signup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'signup': grpc.unary_unary_rpc_method_handler(
                    servicer.signup,
                    request_deserializer=proto_dot_account__pb2.CreateAccountRequest.FromString,
                    response_serializer=proto_dot_account__pb2.CreateAccountResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'account.Account', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Account(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def signup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.Account/signup',
            proto_dot_account__pb2.CreateAccountRequest.SerializeToString,
            proto_dot_account__pb2.CreateAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
