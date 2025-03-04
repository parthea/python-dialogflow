# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple

from google.api_core import gapic_v1  # type: ignore
from google.api_core import grpc_helpers_async  # type: ignore
from google import auth  # type: ignore
from google.auth import credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.dialogflow_v2beta1.types import conversation
from google.cloud.dialogflow_v2beta1.types import conversation as gcd_conversation

from .base import ConversationsTransport, DEFAULT_CLIENT_INFO
from .grpc import ConversationsGrpcTransport


class ConversationsGrpcAsyncIOTransport(ConversationsTransport):
    """gRPC AsyncIO backend transport for Conversations.

    Service for managing
    [Conversations][google.cloud.dialogflow.v2beta1.Conversation].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "dialogflow.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "dialogflow.googleapis.com",
        credentials: credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id=None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def create_conversation(
        self,
    ) -> Callable[
        [gcd_conversation.CreateConversationRequest],
        Awaitable[gcd_conversation.Conversation],
    ]:
        r"""Return a callable for the create conversation method over gRPC.

        Creates a new conversation. Conversations are auto-completed
        after 24 hours.

        Conversation Lifecycle: There are two stages during a
        conversation: Automated Agent Stage and Assist Stage.

        For Automated Agent Stage, there will be a dialogflow agent
        responding to user queries.

        For Assist Stage, there's no dialogflow agent responding to user
        queries. But we will provide suggestions which are generated
        from conversation.

        If
        [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile]
        is configured for a dialogflow agent, conversation will start
        from ``Automated Agent Stage``, otherwise, it will start from
        ``Assist Stage``. And during ``Automated Agent Stage``, once an
        [Intent][google.cloud.dialogflow.v2beta1.Intent] with
        [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff]
        is triggered, conversation will transfer to Assist Stage.

        Returns:
            Callable[[~.CreateConversationRequest],
                    Awaitable[~.Conversation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_conversation" not in self._stubs:
            self._stubs["create_conversation"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Conversations/CreateConversation",
                request_serializer=gcd_conversation.CreateConversationRequest.serialize,
                response_deserializer=gcd_conversation.Conversation.deserialize,
            )
        return self._stubs["create_conversation"]

    @property
    def list_conversations(
        self,
    ) -> Callable[
        [conversation.ListConversationsRequest],
        Awaitable[conversation.ListConversationsResponse],
    ]:
        r"""Return a callable for the list conversations method over gRPC.

        Returns the list of all conversations in the
        specified project.

        Returns:
            Callable[[~.ListConversationsRequest],
                    Awaitable[~.ListConversationsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_conversations" not in self._stubs:
            self._stubs["list_conversations"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Conversations/ListConversations",
                request_serializer=conversation.ListConversationsRequest.serialize,
                response_deserializer=conversation.ListConversationsResponse.deserialize,
            )
        return self._stubs["list_conversations"]

    @property
    def get_conversation(
        self,
    ) -> Callable[
        [conversation.GetConversationRequest], Awaitable[conversation.Conversation]
    ]:
        r"""Return a callable for the get conversation method over gRPC.

        Retrieves the specific conversation.

        Returns:
            Callable[[~.GetConversationRequest],
                    Awaitable[~.Conversation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_conversation" not in self._stubs:
            self._stubs["get_conversation"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Conversations/GetConversation",
                request_serializer=conversation.GetConversationRequest.serialize,
                response_deserializer=conversation.Conversation.deserialize,
            )
        return self._stubs["get_conversation"]

    @property
    def complete_conversation(
        self,
    ) -> Callable[
        [conversation.CompleteConversationRequest], Awaitable[conversation.Conversation]
    ]:
        r"""Return a callable for the complete conversation method over gRPC.

        Completes the specified conversation. Finished
        conversations are purged from the database after 30
        days.

        Returns:
            Callable[[~.CompleteConversationRequest],
                    Awaitable[~.Conversation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "complete_conversation" not in self._stubs:
            self._stubs["complete_conversation"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Conversations/CompleteConversation",
                request_serializer=conversation.CompleteConversationRequest.serialize,
                response_deserializer=conversation.Conversation.deserialize,
            )
        return self._stubs["complete_conversation"]

    @property
    def batch_create_messages(
        self,
    ) -> Callable[
        [conversation.BatchCreateMessagesRequest],
        Awaitable[conversation.BatchCreateMessagesResponse],
    ]:
        r"""Return a callable for the batch create messages method over gRPC.

        Batch ingests messages to conversation. Customers can
        use this RPC to ingest historical messages to
        conversation.

        Returns:
            Callable[[~.BatchCreateMessagesRequest],
                    Awaitable[~.BatchCreateMessagesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_create_messages" not in self._stubs:
            self._stubs["batch_create_messages"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Conversations/BatchCreateMessages",
                request_serializer=conversation.BatchCreateMessagesRequest.serialize,
                response_deserializer=conversation.BatchCreateMessagesResponse.deserialize,
            )
        return self._stubs["batch_create_messages"]

    @property
    def list_messages(
        self,
    ) -> Callable[
        [conversation.ListMessagesRequest], Awaitable[conversation.ListMessagesResponse]
    ]:
        r"""Return a callable for the list messages method over gRPC.

        Lists messages that belong to a given conversation. ``messages``
        are ordered by ``create_time`` in descending order. To fetch
        updates without duplication, send request with filter
        ``create_time_epoch_microseconds > [first item's create_time of previous request]``
        and empty page_token.

        Returns:
            Callable[[~.ListMessagesRequest],
                    Awaitable[~.ListMessagesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_messages" not in self._stubs:
            self._stubs["list_messages"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Conversations/ListMessages",
                request_serializer=conversation.ListMessagesRequest.serialize,
                response_deserializer=conversation.ListMessagesResponse.deserialize,
            )
        return self._stubs["list_messages"]


__all__ = ("ConversationsGrpcAsyncIOTransport",)
