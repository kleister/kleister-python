"""
    Kleister OpenAPI

    API definition for Kleister, manage mod packs for Minecraft  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from kleister.api_client import ApiClient, Endpoint as _Endpoint
from kleister.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from kleister.model.build import Build
from kleister.model.general_error import GeneralError
from kleister.model.minecraft import Minecraft
from kleister.model.minecraft_build_params import MinecraftBuildParams
from kleister.model.validation_error import ValidationError


class MinecraftApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __append_minecraft_to_build(self, minecraft_id, minecraft_build, **kwargs):
            """Assign a build to a Minecraft version  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.append_minecraft_to_build(minecraft_id, minecraft_build, async_req=True)
            >>> result = thread.get()

            Args:
                minecraft_id (str): A minecraft UUID or slug
                minecraft_build (MinecraftBuildParams): The build data to append

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
                [Build]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["minecraft_id"] = minecraft_id
            kwargs["minecraft_build"] = minecraft_build
            return self.call_with_http_info(**kwargs)

        self.append_minecraft_to_build = _Endpoint(
            settings={
                "response_type": ([Build],),
                "auth": [],
                "endpoint_path": "/minecraft/{minecraft_id}/builds",
                "operation_id": "append_minecraft_to_build",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "minecraft_id",
                    "minecraft_build",
                ],
                "required": [
                    "minecraft_id",
                    "minecraft_build",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "minecraft_id": (str,),
                    "minecraft_build": (MinecraftBuildParams,),
                },
                "attribute_map": {
                    "minecraft_id": "minecraft_id",
                },
                "location_map": {
                    "minecraft_id": "path",
                    "minecraft_build": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__append_minecraft_to_build,
        )

        def __delete_minecraft_from_build(
            self, minecraft_id, minecraft_build, **kwargs
        ):
            """Unlink a build from a Minecraft version  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_minecraft_from_build(minecraft_id, minecraft_build, async_req=True)
            >>> result = thread.get()

            Args:
                minecraft_id (str): A minecraft UUID or slug
                minecraft_build (MinecraftBuildParams): The build data to unlink

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
                [Build]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["minecraft_id"] = minecraft_id
            kwargs["minecraft_build"] = minecraft_build
            return self.call_with_http_info(**kwargs)

        self.delete_minecraft_from_build = _Endpoint(
            settings={
                "response_type": ([Build],),
                "auth": [],
                "endpoint_path": "/minecraft/{minecraft_id}/builds",
                "operation_id": "delete_minecraft_from_build",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "minecraft_id",
                    "minecraft_build",
                ],
                "required": [
                    "minecraft_id",
                    "minecraft_build",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "minecraft_id": (str,),
                    "minecraft_build": (MinecraftBuildParams,),
                },
                "attribute_map": {
                    "minecraft_id": "minecraft_id",
                },
                "location_map": {
                    "minecraft_id": "path",
                    "minecraft_build": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__delete_minecraft_from_build,
        )

        def __list_minecraft_builds(self, minecraft_id, **kwargs):
            """Fetch the builds assigned to a Minecraft version  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_minecraft_builds(minecraft_id, async_req=True)
            >>> result = thread.get()

            Args:
                minecraft_id (str): A minecraft UUID or slug

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
                [Build]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["minecraft_id"] = minecraft_id
            return self.call_with_http_info(**kwargs)

        self.list_minecraft_builds = _Endpoint(
            settings={
                "response_type": ([Build],),
                "auth": [],
                "endpoint_path": "/minecraft/{minecraft_id}/builds",
                "operation_id": "list_minecraft_builds",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "minecraft_id",
                ],
                "required": [
                    "minecraft_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "minecraft_id": (str,),
                },
                "attribute_map": {
                    "minecraft_id": "minecraft_id",
                },
                "location_map": {
                    "minecraft_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__list_minecraft_builds,
        )

        def __list_minecrafts(self, **kwargs):
            """Fetch the available Minecraft versions  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_minecrafts(async_req=True)
            >>> result = thread.get()


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
                [Minecraft]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.list_minecrafts = _Endpoint(
            settings={
                "response_type": ([Minecraft],),
                "auth": [],
                "endpoint_path": "/minecraft",
                "operation_id": "list_minecrafts",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__list_minecrafts,
        )

        def __search_minecrafts(self, minecraft_id, **kwargs):
            """Search for available Minecraft versions  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.search_minecrafts(minecraft_id, async_req=True)
            >>> result = thread.get()

            Args:
                minecraft_id (str): A search token to search Minecraft versions

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
                [Minecraft]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["minecraft_id"] = minecraft_id
            return self.call_with_http_info(**kwargs)

        self.search_minecrafts = _Endpoint(
            settings={
                "response_type": ([Minecraft],),
                "auth": [],
                "endpoint_path": "/minecraft/{minecraft_id}",
                "operation_id": "search_minecrafts",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "minecraft_id",
                ],
                "required": [
                    "minecraft_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "minecraft_id": (str,),
                },
                "attribute_map": {
                    "minecraft_id": "minecraft_id",
                },
                "location_map": {
                    "minecraft_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__search_minecrafts,
        )

        def __update_minecraft(self, **kwargs):
            """Update the available Minecraft versions  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_minecraft(async_req=True)
            >>> result = thread.get()


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
                GeneralError
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.update_minecraft = _Endpoint(
            settings={
                "response_type": (GeneralError,),
                "auth": [],
                "endpoint_path": "/minecraft",
                "operation_id": "update_minecraft",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {},
                "attribute_map": {},
                "location_map": {},
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__update_minecraft,
        )
