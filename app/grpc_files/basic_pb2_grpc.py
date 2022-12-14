# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import app.grpc_files.basic_pb2 as basic__pb2


class SimpleActionsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddNumbers = channel.unary_unary(
                '/SimpleActions/AddNumbers',
                request_serializer=basic__pb2.SumRequest.SerializeToString,
                response_deserializer=basic__pb2.SumReply.FromString,
                )


class SimpleActionsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddNumbers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SimpleActionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddNumbers': grpc.unary_unary_rpc_method_handler(
                    servicer.AddNumbers,
                    request_deserializer=basic__pb2.SumRequest.FromString,
                    response_serializer=basic__pb2.SumReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SimpleActions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SimpleActions(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddNumbers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SimpleActions/AddNumbers',
            basic__pb2.SumRequest.SerializeToString,
            basic__pb2.SumReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
