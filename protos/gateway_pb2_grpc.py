# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bee_rpc import buffer_pb2 as buffer__pb2


class GatewayStub(object):
    """GRPC.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartService = channel.stream_stream(
                '/gateway.Gateway/StartService',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.StopService = channel.stream_stream(
                '/gateway.Gateway/StopService',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.ModifyGasDeposit = channel.stream_stream(
                '/gateway.Gateway/ModifyGasDeposit',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.GetPeerInfo = channel.stream_stream(
                '/gateway.Gateway/GetPeerInfo',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.IntroducePeer = channel.stream_stream(
                '/gateway.Gateway/IntroducePeer',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.GenerateClient = channel.stream_stream(
                '/gateway.Gateway/GenerateClient',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.GenerateDepositToken = channel.stream_stream(
                '/gateway.Gateway/GenerateDepositToken',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.Payable = channel.stream_stream(
                '/gateway.Gateway/Payable',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.SignPublicKey = channel.stream_stream(
                '/gateway.Gateway/SignPublicKey',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.ModifyServiceSystemResources = channel.stream_stream(
                '/gateway.Gateway/ModifyServiceSystemResources',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.Pack = channel.stream_stream(
                '/gateway.Gateway/Pack',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.GetServiceEstimatedCost = channel.stream_stream(
                '/gateway.Gateway/GetServiceEstimatedCost',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.GetService = channel.stream_stream(
                '/gateway.Gateway/GetService',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.GetMetrics = channel.stream_stream(
                '/gateway.Gateway/GetMetrics',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )
        self.ServiceTunnel = channel.stream_stream(
                '/gateway.Gateway/ServiceTunnel',
                request_serializer=buffer__pb2.Buffer.SerializeToString,
                response_deserializer=buffer__pb2.Buffer.FromString,
                )


class GatewayServicer(object):
    """GRPC.

    """

    def StartService(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopService(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyGasDeposit(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPeerInfo(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IntroducePeer(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateClient(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateDepositToken(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Payable(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignPublicKey(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyServiceSystemResources(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pack(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServiceEstimatedCost(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetService(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMetrics(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ServiceTunnel(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GatewayServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartService': grpc.stream_stream_rpc_method_handler(
                    servicer.StartService,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'StopService': grpc.stream_stream_rpc_method_handler(
                    servicer.StopService,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'ModifyGasDeposit': grpc.stream_stream_rpc_method_handler(
                    servicer.ModifyGasDeposit,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'GetPeerInfo': grpc.stream_stream_rpc_method_handler(
                    servicer.GetPeerInfo,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'IntroducePeer': grpc.stream_stream_rpc_method_handler(
                    servicer.IntroducePeer,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'GenerateClient': grpc.stream_stream_rpc_method_handler(
                    servicer.GenerateClient,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'GenerateDepositToken': grpc.stream_stream_rpc_method_handler(
                    servicer.GenerateDepositToken,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'Payable': grpc.stream_stream_rpc_method_handler(
                    servicer.Payable,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'SignPublicKey': grpc.stream_stream_rpc_method_handler(
                    servicer.SignPublicKey,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'ModifyServiceSystemResources': grpc.stream_stream_rpc_method_handler(
                    servicer.ModifyServiceSystemResources,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'Pack': grpc.stream_stream_rpc_method_handler(
                    servicer.Pack,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'GetServiceEstimatedCost': grpc.stream_stream_rpc_method_handler(
                    servicer.GetServiceEstimatedCost,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'GetService': grpc.stream_stream_rpc_method_handler(
                    servicer.GetService,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'GetMetrics': grpc.stream_stream_rpc_method_handler(
                    servicer.GetMetrics,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
            'ServiceTunnel': grpc.stream_stream_rpc_method_handler(
                    servicer.ServiceTunnel,
                    request_deserializer=buffer__pb2.Buffer.FromString,
                    response_serializer=buffer__pb2.Buffer.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'gateway.Gateway', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Gateway(object):
    """GRPC.

    """

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
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/StartService',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopService(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/StopService',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifyGasDeposit(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/ModifyGasDeposit',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPeerInfo(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/GetPeerInfo',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IntroducePeer(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/IntroducePeer',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateClient(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/GenerateClient',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateDepositToken(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/GenerateDepositToken',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Payable(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/Payable',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignPublicKey(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/SignPublicKey',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifyServiceSystemResources(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/ModifyServiceSystemResources',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pack(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/Pack',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServiceEstimatedCost(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/GetServiceEstimatedCost',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetService(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/GetService',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMetrics(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/GetMetrics',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ServiceTunnel(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/gateway.Gateway/ServiceTunnel',
            buffer__pb2.Buffer.SerializeToString,
            buffer__pb2.Buffer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
