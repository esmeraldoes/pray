# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import prayer_tracker_pb2 as prayer__tracker__pb2

# from . import bible_pb2 as bible__pb2



class PrayerTrackerStub(object):
    """Define the service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartPrayer = channel.unary_unary(
                '/prayertracker.PrayerTracker/StartPrayer',
                request_serializer=prayer__tracker__pb2.StartPrayerRequest.SerializeToString,
                response_deserializer=prayer__tracker__pb2.StartPrayerResponse.FromString,
                )
        self.EndPrayer = channel.unary_unary(
                '/prayertracker.PrayerTracker/EndPrayer',
                request_serializer=prayer__tracker__pb2.EndPrayerRequest.SerializeToString,
                response_deserializer=prayer__tracker__pb2.EndPrayerResponse.FromString,
                )
        self.PrayerUpdates = channel.unary_stream(
                '/prayertracker.PrayerTracker/PrayerUpdates',
                request_serializer=prayer__tracker__pb2.PrayerUpdatesRequest.SerializeToString,
                response_deserializer=prayer__tracker__pb2.PrayerUpdateResponse.FromString,
                )
        self.PrayerDuration = channel.unary_unary(
                '/prayertracker.PrayerTracker/PrayerDuration',
                request_serializer=prayer__tracker__pb2.PrayerDurationRequest.SerializeToString,
                response_deserializer=prayer__tracker__pb2.PrayerDurationResponse.FromString,
                )
        self.VoiceDuration = channel.unary_unary(
                '/prayertracker.PrayerTracker/VoiceDuration',
                request_serializer=prayer__tracker__pb2.VoiceDurationRequest.SerializeToString,
                response_deserializer=prayer__tracker__pb2.VoiceDurationResponse.FromString,
                )


class PrayerTrackerServicer(object):
    """Define the service
    """

    def StartPrayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EndPrayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrayerUpdates(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PrayerDuration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoiceDuration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PrayerTrackerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartPrayer': grpc.unary_unary_rpc_method_handler(
                    servicer.StartPrayer,
                    request_deserializer=prayer__tracker__pb2.StartPrayerRequest.FromString,
                    response_serializer=prayer__tracker__pb2.StartPrayerResponse.SerializeToString,
            ),
            'EndPrayer': grpc.unary_unary_rpc_method_handler(
                    servicer.EndPrayer,
                    request_deserializer=prayer__tracker__pb2.EndPrayerRequest.FromString,
                    response_serializer=prayer__tracker__pb2.EndPrayerResponse.SerializeToString,
            ),
            'PrayerUpdates': grpc.unary_stream_rpc_method_handler(
                    servicer.PrayerUpdates,
                    request_deserializer=prayer__tracker__pb2.PrayerUpdatesRequest.FromString,
                    response_serializer=prayer__tracker__pb2.PrayerUpdateResponse.SerializeToString,
            ),
            'PrayerDuration': grpc.unary_unary_rpc_method_handler(
                    servicer.PrayerDuration,
                    request_deserializer=prayer__tracker__pb2.PrayerDurationRequest.FromString,
                    response_serializer=prayer__tracker__pb2.PrayerDurationResponse.SerializeToString,
            ),
            'VoiceDuration': grpc.unary_unary_rpc_method_handler(
                    servicer.VoiceDuration,
                    request_deserializer=prayer__tracker__pb2.VoiceDurationRequest.FromString,
                    response_serializer=prayer__tracker__pb2.VoiceDurationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'prayertracker.PrayerTracker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PrayerTracker(object):
    """Define the service
    """

    @staticmethod
    def StartPrayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prayertracker.PrayerTracker/StartPrayer',
            prayer__tracker__pb2.StartPrayerRequest.SerializeToString,
            prayer__tracker__pb2.StartPrayerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EndPrayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prayertracker.PrayerTracker/EndPrayer',
            prayer__tracker__pb2.EndPrayerRequest.SerializeToString,
            prayer__tracker__pb2.EndPrayerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PrayerUpdates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/prayertracker.PrayerTracker/PrayerUpdates',
            prayer__tracker__pb2.PrayerUpdatesRequest.SerializeToString,
            prayer__tracker__pb2.PrayerUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PrayerDuration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prayertracker.PrayerTracker/PrayerDuration',
            prayer__tracker__pb2.PrayerDurationRequest.SerializeToString,
            prayer__tracker__pb2.PrayerDurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoiceDuration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prayertracker.PrayerTracker/VoiceDuration',
            prayer__tracker__pb2.VoiceDurationRequest.SerializeToString,
            prayer__tracker__pb2.VoiceDurationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
