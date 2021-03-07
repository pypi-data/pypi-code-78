"""
    Diahook

    The Diahook server API documentation  # noqa: E501

    The version of the OpenAPI document: 0.8.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from diahook.openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from diahook.openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from diahook.openapi_client.model.http_validation_error import HTTPValidationError
from diahook.openapi_client.model.http_error_out import HttpErrorOut
from diahook.openapi_client.model.list_response_endpoint_message_out import ListResponseEndpointMessageOut
from diahook.openapi_client.model.list_response_message_attempt_endpoint_out import ListResponseMessageAttemptEndpointOut
from diahook.openapi_client.model.list_response_message_attempt_out import ListResponseMessageAttemptOut
from diahook.openapi_client.model.list_response_message_endpoint_out import ListResponseMessageEndpointOut
from diahook.openapi_client.model.message_attempt_out import MessageAttemptOut
from diahook.openapi_client.model.message_status import MessageStatus


class MessageAttemptApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_attempt_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_get(
            self,
            attempt_id,
            msg_id,
            app_id,
            **kwargs
        ):
            """Get Attempt  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_attempt_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_get(attempt_id, msg_id, app_id, async_req=True)
            >>> result = thread.get()

            Args:
                attempt_id (str):
                msg_id (str):
                app_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                MessageAttemptOut
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['attempt_id'] = \
                attempt_id
            kwargs['msg_id'] = \
                msg_id
            kwargs['app_id'] = \
                app_id
            return self.call_with_http_info(**kwargs)

        self.get_attempt_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_get = _Endpoint(
            settings={
                'response_type': (MessageAttemptOut,),
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/app/{app_id}/msg/{msg_id}/attempt/{attempt_id}/',
                'operation_id': 'get_attempt_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'attempt_id',
                    'msg_id',
                    'app_id',
                ],
                'required': [
                    'attempt_id',
                    'msg_id',
                    'app_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'attempt_id':
                        (str,),
                    'msg_id':
                        (str,),
                    'app_id':
                        (str,),
                },
                'attribute_map': {
                    'attempt_id': 'attempt_id',
                    'msg_id': 'msg_id',
                    'app_id': 'app_id',
                },
                'location_map': {
                    'attempt_id': 'path',
                    'msg_id': 'path',
                    'app_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_attempt_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_get
        )

        def __list_attempted_destinations_api_v1_app_app_id_msg_msg_id_endpoint_get(
            self,
            msg_id,
            app_id,
            **kwargs
        ):
            """List Attempted Destinations  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_attempted_destinations_api_v1_app_app_id_msg_msg_id_endpoint_get(msg_id, app_id, async_req=True)
            >>> result = thread.get()

            Args:
                msg_id (str):
                app_id (str):

            Keyword Args:
                iterator (str): [optional]
                limit (int): [optional] if omitted the server will use the default value of 50
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListResponseMessageEndpointOut
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['msg_id'] = \
                msg_id
            kwargs['app_id'] = \
                app_id
            return self.call_with_http_info(**kwargs)

        self.list_attempted_destinations_api_v1_app_app_id_msg_msg_id_endpoint_get = _Endpoint(
            settings={
                'response_type': (ListResponseMessageEndpointOut,),
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/app/{app_id}/msg/{msg_id}/endpoint/',
                'operation_id': 'list_attempted_destinations_api_v1_app_app_id_msg_msg_id_endpoint_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'msg_id',
                    'app_id',
                    'iterator',
                    'limit',
                ],
                'required': [
                    'msg_id',
                    'app_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'msg_id':
                        (str,),
                    'app_id':
                        (str,),
                    'iterator':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'msg_id': 'msg_id',
                    'app_id': 'app_id',
                    'iterator': 'iterator',
                    'limit': 'limit',
                },
                'location_map': {
                    'msg_id': 'path',
                    'app_id': 'path',
                    'iterator': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_attempted_destinations_api_v1_app_app_id_msg_msg_id_endpoint_get
        )

        def __list_attempted_messages_api_v1_app_app_id_endpoint_endpoint_id_msg_get(
            self,
            endpoint_id,
            app_id,
            **kwargs
        ):
            """List Attempted Messages  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_attempted_messages_api_v1_app_app_id_endpoint_endpoint_id_msg_get(endpoint_id, app_id, async_req=True)
            >>> result = thread.get()

            Args:
                endpoint_id (str):
                app_id (str):

            Keyword Args:
                iterator (str): [optional]
                limit (int): [optional] if omitted the server will use the default value of 50
                status (MessageStatus): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListResponseEndpointMessageOut
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['endpoint_id'] = \
                endpoint_id
            kwargs['app_id'] = \
                app_id
            return self.call_with_http_info(**kwargs)

        self.list_attempted_messages_api_v1_app_app_id_endpoint_endpoint_id_msg_get = _Endpoint(
            settings={
                'response_type': (ListResponseEndpointMessageOut,),
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/app/{app_id}/endpoint/{endpoint_id}/msg/',
                'operation_id': 'list_attempted_messages_api_v1_app_app_id_endpoint_endpoint_id_msg_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'endpoint_id',
                    'app_id',
                    'iterator',
                    'limit',
                    'status',
                ],
                'required': [
                    'endpoint_id',
                    'app_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'endpoint_id':
                        (str,),
                    'app_id':
                        (str,),
                    'iterator':
                        (str,),
                    'limit':
                        (int,),
                    'status':
                        (MessageStatus,),
                },
                'attribute_map': {
                    'endpoint_id': 'endpoint_id',
                    'app_id': 'app_id',
                    'iterator': 'iterator',
                    'limit': 'limit',
                    'status': 'status',
                },
                'location_map': {
                    'endpoint_id': 'path',
                    'app_id': 'path',
                    'iterator': 'query',
                    'limit': 'query',
                    'status': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_attempted_messages_api_v1_app_app_id_endpoint_endpoint_id_msg_get
        )

        def __list_attempts_api_v1_app_app_id_msg_msg_id_attempt_get(
            self,
            msg_id,
            app_id,
            **kwargs
        ):
            """List Attempts  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_attempts_api_v1_app_app_id_msg_msg_id_attempt_get(msg_id, app_id, async_req=True)
            >>> result = thread.get()

            Args:
                msg_id (str):
                app_id (str):

            Keyword Args:
                iterator (str): [optional]
                limit (int): [optional] if omitted the server will use the default value of 50
                status (MessageStatus): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListResponseMessageAttemptOut
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['msg_id'] = \
                msg_id
            kwargs['app_id'] = \
                app_id
            return self.call_with_http_info(**kwargs)

        self.list_attempts_api_v1_app_app_id_msg_msg_id_attempt_get = _Endpoint(
            settings={
                'response_type': (ListResponseMessageAttemptOut,),
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/app/{app_id}/msg/{msg_id}/attempt/',
                'operation_id': 'list_attempts_api_v1_app_app_id_msg_msg_id_attempt_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'msg_id',
                    'app_id',
                    'iterator',
                    'limit',
                    'status',
                ],
                'required': [
                    'msg_id',
                    'app_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'msg_id':
                        (str,),
                    'app_id':
                        (str,),
                    'iterator':
                        (str,),
                    'limit':
                        (int,),
                    'status':
                        (MessageStatus,),
                },
                'attribute_map': {
                    'msg_id': 'msg_id',
                    'app_id': 'app_id',
                    'iterator': 'iterator',
                    'limit': 'limit',
                    'status': 'status',
                },
                'location_map': {
                    'msg_id': 'path',
                    'app_id': 'path',
                    'iterator': 'query',
                    'limit': 'query',
                    'status': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_attempts_api_v1_app_app_id_msg_msg_id_attempt_get
        )

        def __list_attempts_for_endpoint_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_attempt_get(
            self,
            msg_id,
            endpoint_id,
            app_id,
            **kwargs
        ):
            """List Attempts For Endpoint  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_attempts_for_endpoint_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_attempt_get(msg_id, endpoint_id, app_id, async_req=True)
            >>> result = thread.get()

            Args:
                msg_id (str):
                endpoint_id (str):
                app_id (str):

            Keyword Args:
                iterator (str): [optional]
                limit (int): [optional] if omitted the server will use the default value of 50
                status (MessageStatus): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListResponseMessageAttemptEndpointOut
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['msg_id'] = \
                msg_id
            kwargs['endpoint_id'] = \
                endpoint_id
            kwargs['app_id'] = \
                app_id
            return self.call_with_http_info(**kwargs)

        self.list_attempts_for_endpoint_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_attempt_get = _Endpoint(
            settings={
                'response_type': (ListResponseMessageAttemptEndpointOut,),
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/app/{app_id}/msg/{msg_id}/endpoint/{endpoint_id}/attempt/',
                'operation_id': 'list_attempts_for_endpoint_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_attempt_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'msg_id',
                    'endpoint_id',
                    'app_id',
                    'iterator',
                    'limit',
                    'status',
                ],
                'required': [
                    'msg_id',
                    'endpoint_id',
                    'app_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'msg_id':
                        (str,),
                    'endpoint_id':
                        (str,),
                    'app_id':
                        (str,),
                    'iterator':
                        (str,),
                    'limit':
                        (int,),
                    'status':
                        (MessageStatus,),
                },
                'attribute_map': {
                    'msg_id': 'msg_id',
                    'endpoint_id': 'endpoint_id',
                    'app_id': 'app_id',
                    'iterator': 'iterator',
                    'limit': 'limit',
                    'status': 'status',
                },
                'location_map': {
                    'msg_id': 'path',
                    'endpoint_id': 'path',
                    'app_id': 'path',
                    'iterator': 'query',
                    'limit': 'query',
                    'status': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_attempts_for_endpoint_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_attempt_get
        )

        def __resend_webhook_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_resend_post(
            self,
            endpoint_id,
            msg_id,
            app_id,
            **kwargs
        ):
            """Resend Webhook  # noqa: E501

            Resend a message to the specified endpoint.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.resend_webhook_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_resend_post(endpoint_id, msg_id, app_id, async_req=True)
            >>> result = thread.get()

            Args:
                endpoint_id (str):
                msg_id (str):
                app_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['endpoint_id'] = \
                endpoint_id
            kwargs['msg_id'] = \
                msg_id
            kwargs['app_id'] = \
                app_id
            return self.call_with_http_info(**kwargs)

        self.resend_webhook_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_resend_post = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/app/{app_id}/msg/{msg_id}/endpoint/{endpoint_id}/resend/',
                'operation_id': 'resend_webhook_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_resend_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'endpoint_id',
                    'msg_id',
                    'app_id',
                ],
                'required': [
                    'endpoint_id',
                    'msg_id',
                    'app_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'endpoint_id':
                        (str,),
                    'msg_id':
                        (str,),
                    'app_id':
                        (str,),
                },
                'attribute_map': {
                    'endpoint_id': 'endpoint_id',
                    'msg_id': 'msg_id',
                    'app_id': 'app_id',
                },
                'location_map': {
                    'endpoint_id': 'path',
                    'msg_id': 'path',
                    'app_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__resend_webhook_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_resend_post
        )
