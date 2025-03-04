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

from typing import (
    Any,
    AsyncIterable,
    Awaitable,
    Callable,
    Iterable,
    Sequence,
    Tuple,
    Optional,
)

from google.cloud.dialogflow_v2.types import conversation
from google.cloud.dialogflow_v2.types import participant


class ListConversationsPager:
    """A pager for iterating through ``list_conversations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dialogflow_v2.types.ListConversationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``conversations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListConversations`` requests and continue to iterate
    through the ``conversations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dialogflow_v2.types.ListConversationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., conversation.ListConversationsResponse],
        request: conversation.ListConversationsRequest,
        response: conversation.ListConversationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dialogflow_v2.types.ListConversationsRequest):
                The initial request object.
            response (google.cloud.dialogflow_v2.types.ListConversationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = conversation.ListConversationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[conversation.ListConversationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[conversation.Conversation]:
        for page in self.pages:
            yield from page.conversations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListConversationsAsyncPager:
    """A pager for iterating through ``list_conversations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dialogflow_v2.types.ListConversationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``conversations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListConversations`` requests and continue to iterate
    through the ``conversations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dialogflow_v2.types.ListConversationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[conversation.ListConversationsResponse]],
        request: conversation.ListConversationsRequest,
        response: conversation.ListConversationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dialogflow_v2.types.ListConversationsRequest):
                The initial request object.
            response (google.cloud.dialogflow_v2.types.ListConversationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = conversation.ListConversationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[conversation.ListConversationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[conversation.Conversation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.conversations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMessagesPager:
    """A pager for iterating through ``list_messages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dialogflow_v2.types.ListMessagesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``messages`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMessages`` requests and continue to iterate
    through the ``messages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dialogflow_v2.types.ListMessagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., conversation.ListMessagesResponse],
        request: conversation.ListMessagesRequest,
        response: conversation.ListMessagesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dialogflow_v2.types.ListMessagesRequest):
                The initial request object.
            response (google.cloud.dialogflow_v2.types.ListMessagesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = conversation.ListMessagesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[conversation.ListMessagesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[participant.Message]:
        for page in self.pages:
            yield from page.messages

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListMessagesAsyncPager:
    """A pager for iterating through ``list_messages`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dialogflow_v2.types.ListMessagesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``messages`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMessages`` requests and continue to iterate
    through the ``messages`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dialogflow_v2.types.ListMessagesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[conversation.ListMessagesResponse]],
        request: conversation.ListMessagesRequest,
        response: conversation.ListMessagesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dialogflow_v2.types.ListMessagesRequest):
                The initial request object.
            response (google.cloud.dialogflow_v2.types.ListMessagesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = conversation.ListMessagesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[conversation.ListMessagesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[participant.Message]:
        async def async_generator():
            async for page in self.pages:
                for response in page.messages:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
