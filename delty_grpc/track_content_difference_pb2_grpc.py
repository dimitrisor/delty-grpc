# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc

import delty_grpc.track_content_difference_pb2 as protos_dot_track__content__difference__pb2

GRPC_GENERATED_VERSION = "1.66.1"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + " but the generated code in protos/track_content_difference_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class TrackContentDifferenceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TriggerTrackContentDifference = channel.unary_unary(
            "/track_content_difference.TrackContentDifferenceService/TriggerTrackContentDifference",
            request_serializer=protos_dot_track__content__difference__pb2.TriggerRequest.SerializeToString,
            response_deserializer=protos_dot_track__content__difference__pb2.TriggerResponse.FromString,
            _registered_method=True,
        )


class TrackContentDifferenceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TriggerTrackContentDifference(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TrackContentDifferenceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "TriggerTrackContentDifference": grpc.unary_unary_rpc_method_handler(
            servicer.TriggerTrackContentDifference,
            request_deserializer=protos_dot_track__content__difference__pb2.TriggerRequest.FromString,
            response_serializer=protos_dot_track__content__difference__pb2.TriggerResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "track_content_difference.TrackContentDifferenceService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers(
        "track_content_difference.TrackContentDifferenceService", rpc_method_handlers
    )


# This class is part of an EXPERIMENTAL API.
class TrackContentDifferenceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TriggerTrackContentDifference(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/track_content_difference.TrackContentDifferenceService/TriggerTrackContentDifference",
            protos_dot_track__content__difference__pb2.TriggerRequest.SerializeToString,
            protos_dot_track__content__difference__pb2.TriggerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
