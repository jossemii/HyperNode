# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gateway_pb2 as gateway__pb2
import ipss_pb2 as ipss__pb2


class GatewayStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartService = channel.stream_unary(
                '/gateway.Gateway/StartService',
                request_serializer=gateway__pb2.ServiceTransport.SerializeToString,
                response_deserializer=gateway__pb2.Instance.FromString,
                )
        self.StopService = channel.unary_unary(
                '/gateway.Gateway/StopService',
                request_serializer=gateway__pb2.Token.SerializeToString,
                response_deserializer=gateway__pb2.Empty.FromString,
                )
        self.Hynode = channel.unary_unary(
                '/gateway.Gateway/Hynode',
                request_serializer=ipss__pb2.Instance.SerializeToString,
                response_deserializer=ipss__pb2.Instance.FromString,
                )
        self.GetServiceZip = channel.unary_unary(
                '/gateway.Gateway/GetServiceZip',
                request_serializer=ipss__pb2.Service.SerializeToString,
                response_deserializer=gateway__pb2.ContainerZip.FromString,
                )


class GatewayServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartService(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopService(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Hynode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceZip(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GatewayServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartService': grpc.stream_unary_rpc_method_handler(
                    servicer.StartService,
                    request_deserializer=gateway__pb2.ServiceTransport.FromString,
                    response_serializer=gateway__pb2.Instance.SerializeToString,
            ),
            'StopService': grpc.unary_unary_rpc_method_handler(
                    servicer.StopService,
                    request_deserializer=gateway__pb2.Token.FromString,
                    response_serializer=gateway__pb2.Empty.SerializeToString,
            ),
            'Hynode': grpc.unary_unary_rpc_method_handler(
                    servicer.Hynode,
                    request_deserializer=ipss__pb2.Instance.FromString,
                    response_serializer=ipss__pb2.Instance.SerializeToString,
            ),
            'GetServiceZip': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServiceZip,
                    request_deserializer=ipss__pb2.Service.FromString,
                    response_serializer=gateway__pb2.ContainerZip.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gateway.Gateway', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Gateway(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartService(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/gateway.Gateway/StartService',
            gateway__pb2.ServiceTransport.SerializeToString,
            gateway__pb2.Instance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopService(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gateway.Gateway/StopService',
            gateway__pb2.Token.SerializeToString,
            gateway__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Hynode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gateway.Gateway/Hynode',
            ipss__pb2.Instance.SerializeToString,
            ipss__pb2.Instance.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServiceZip(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/gateway.Gateway/GetServiceZip',
            ipss__pb2.Service.SerializeToString,
            gateway__pb2.ContainerZip.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
