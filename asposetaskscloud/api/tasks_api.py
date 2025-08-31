# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="tasks_api.py">
#   Copyright (c) 2020 Aspose.Tasks Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
from asposetaskscloud.rest import ApiException
from asposetaskscloud.api_client import ApiClient


class TasksApi(object):
    """
    Aspose.Tasks Cloud API

    :param api_client: an api client to perfom http requests
    """
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.__request_token()

    def __downcase_first_letter(self, s):
        if len(s) == 0:
            return s
        else:
            return s[0].lower() + s[1:]

    def __request_token(self):
        config = self.api_client.configuration
        api_version = config.api_version
        request_url = ''
        host = ''
        config.api_version = ''
        if config.auth_url is not None:
                host = config.host
                config.host = config.auth_url
        else:
                request_url = "connect/token"

        form_params = [('grant_type', 'client_credentials'), ('client_id', config.api_key['app_sid']),
                       ('client_secret', config.api_key['api_key'])]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        if config.auth_url is not None:
                config.host = host
        self.api_client.configuration.access_token = access_token
        self.api_client.configuration.api_version = api_version

    def copy_file(self, request, **kwargs):  # noqa: E501
        """Copy file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param src_path str : Source file path e.g. '/folder/file.ext' (required)
        :param dest_path str : Destination file path (required)
        :param src_storage_name str : Source storage name
        :param dest_storage_name str : Destination storage name
        :param version_id str : File version ID to copy
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def copy_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Copy file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request copy_file_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method copy_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if request.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `copy_file`")  # noqa: E501
        # verify the required parameter 'dest_path' is set
        if request.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `copy_file`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/file/copy/{srcPath}'
        path_params = {}
        if request.src_path is not None:
            path_params[self.__downcase_first_letter('srcPath')] = request.src_path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('destPath') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('destPath' + '}'), request.dest_path if request.dest_path is not None else '')
        else:
            if request.dest_path is not None:
                query_params.append((self.__downcase_first_letter('destPath'), request.dest_path))  # noqa: E501
        if '{' + self.__downcase_first_letter('srcStorageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('srcStorageName' + '}'), request.src_storage_name if request.src_storage_name is not None else '')
        else:
            if request.src_storage_name is not None:
                query_params.append((self.__downcase_first_letter('srcStorageName'), request.src_storage_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('destStorageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('destStorageName' + '}'), request.dest_storage_name if request.dest_storage_name is not None else '')
        else:
            if request.dest_storage_name is not None:
                query_params.append((self.__downcase_first_letter('destStorageName'), request.dest_storage_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('versionId') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('versionId' + '}'), request.version_id if request.version_id is not None else '')
        else:
            if request.version_id is not None:
                query_params.append((self.__downcase_first_letter('versionId'), request.version_id))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_file(self, request, **kwargs):  # noqa: E501
        """Delete file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : File path e.g. '/folder/file.ext' (required)
        :param storage_name str : Storage name
        :param version_id str : File version ID to delete
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_file_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `delete_file`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/file/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('versionId') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('versionId' + '}'), request.version_id if request.version_id is not None else '')
        else:
            if request.version_id is not None:
                query_params.append((self.__downcase_first_letter('versionId'), request.version_id))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_file(self, request, **kwargs):  # noqa: E501
        """Download file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : File path e.g. '/folder/file.ext' (required)
        :param storage_name str : Storage name
        :param version_id str : File version ID to download
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.download_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def download_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Download file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request download_file_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `download_file`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/file/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('versionId') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('versionId' + '}'), request.version_id if request.version_id is not None else '')
        else:
            if request.version_id is not None:
                query_params.append((self.__downcase_first_letter('versionId'), request.version_id))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def move_file(self, request, **kwargs):  # noqa: E501
        """Move file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param src_path str : Source file path e.g. '/src.ext' (required)
        :param dest_path str : Destination file path e.g. '/dest.ext' (required)
        :param src_storage_name str : Source storage name
        :param dest_storage_name str : Destination storage name
        :param version_id str : File version ID to move
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def move_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Move file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request move_file_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if request.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `move_file`")  # noqa: E501
        # verify the required parameter 'dest_path' is set
        if request.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `move_file`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/file/move/{srcPath}'
        path_params = {}
        if request.src_path is not None:
            path_params[self.__downcase_first_letter('srcPath')] = request.src_path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('destPath') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('destPath' + '}'), request.dest_path if request.dest_path is not None else '')
        else:
            if request.dest_path is not None:
                query_params.append((self.__downcase_first_letter('destPath'), request.dest_path))  # noqa: E501
        if '{' + self.__downcase_first_letter('srcStorageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('srcStorageName' + '}'), request.src_storage_name if request.src_storage_name is not None else '')
        else:
            if request.src_storage_name is not None:
                query_params.append((self.__downcase_first_letter('srcStorageName'), request.src_storage_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('destStorageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('destStorageName' + '}'), request.dest_storage_name if request.dest_storage_name is not None else '')
        else:
            if request.dest_storage_name is not None:
                query_params.append((self.__downcase_first_letter('destStorageName'), request.dest_storage_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('versionId') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('versionId' + '}'), request.version_id if request.version_id is not None else '')
        else:
            if request.version_id is not None:
                query_params.append((self.__downcase_first_letter('versionId'), request.version_id))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_file(self, request, **kwargs):  # noqa: E501
        """Upload file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              (required)
        :param file file : File to upload (required)
        :param storage_name str : Storage name
        :return: FilesUploadResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.upload_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def upload_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Upload file  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request upload_file_request object with parameters
        :return: FilesUploadResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `upload_file`")  # noqa: E501
        # verify the required parameter 'file' is set
        if request.file is None:
            raise ValueError("Missing the required parameter `file` when calling `upload_file`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/file/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.file is not None:
            local_var_files.append((self.__downcase_first_letter('File'), request.file))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilesUploadResult',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def copy_folder(self, request, **kwargs):  # noqa: E501
        """Copy folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param src_path str : Source folder path e.g. '/src' (required)
        :param dest_path str : Destination folder path e.g. '/dst' (required)
        :param src_storage_name str : Source storage name
        :param dest_storage_name str : Destination storage name
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.copy_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def copy_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Copy folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request copy_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method copy_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if request.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `copy_folder`")  # noqa: E501
        # verify the required parameter 'dest_path' is set
        if request.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `copy_folder`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/folder/copy/{srcPath}'
        path_params = {}
        if request.src_path is not None:
            path_params[self.__downcase_first_letter('srcPath')] = request.src_path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('destPath') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('destPath' + '}'), request.dest_path if request.dest_path is not None else '')
        else:
            if request.dest_path is not None:
                query_params.append((self.__downcase_first_letter('destPath'), request.dest_path))  # noqa: E501
        if '{' + self.__downcase_first_letter('srcStorageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('srcStorageName' + '}'), request.src_storage_name if request.src_storage_name is not None else '')
        else:
            if request.src_storage_name is not None:
                query_params.append((self.__downcase_first_letter('srcStorageName'), request.src_storage_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('destStorageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('destStorageName' + '}'), request.dest_storage_name if request.dest_storage_name is not None else '')
        else:
            if request.dest_storage_name is not None:
                query_params.append((self.__downcase_first_letter('destStorageName'), request.dest_storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_folder(self, request, **kwargs):  # noqa: E501
        """Create the folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : Folder path to create e.g. 'folder_1/folder_2/' (required)
        :param storage_name str : Storage name
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def create_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Create the folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request create_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `create_folder`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/folder/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_folder(self, request, **kwargs):  # noqa: E501
        """Delete folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : Folder path e.g. '/folder' (required)
        :param storage_name str : Storage name
        :param recursive bool : Enable to delete folders, subfolders and files
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `delete_folder`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/folder/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('recursive') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('recursive' + '}'), request.recursive if request.recursive is not None else '')
        else:
            if request.recursive is not None:
                query_params.append((self.__downcase_first_letter('recursive'), request.recursive))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_files_list(self, request, **kwargs):  # noqa: E501
        """Get all files and folders within a folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : Folder path e.g. '/folder' (required)
        :param storage_name str : Storage name
        :return: FilesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_files_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_files_list_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get all files and folders within a folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_files_list_request object with parameters
        :return: FilesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_files_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `get_files_list`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/folder/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FilesList',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def move_folder(self, request, **kwargs):  # noqa: E501
        """Move folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param src_path str : Folder path to move e.g. '/folder' (required)
        :param dest_path str : Destination folder path to move to e.g '/dst' (required)
        :param src_storage_name str : Source storage name
        :param dest_storage_name str : Destination storage name
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.move_folder_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def move_folder_with_http_info(self, request, **kwargs):  # noqa: E501
        """Move folder  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request move_folder_request object with parameters
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if request.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `move_folder`")  # noqa: E501
        # verify the required parameter 'dest_path' is set
        if request.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `move_folder`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/folder/move/{srcPath}'
        path_params = {}
        if request.src_path is not None:
            path_params[self.__downcase_first_letter('srcPath')] = request.src_path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('destPath') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('destPath' + '}'), request.dest_path if request.dest_path is not None else '')
        else:
            if request.dest_path is not None:
                query_params.append((self.__downcase_first_letter('destPath'), request.dest_path))  # noqa: E501
        if '{' + self.__downcase_first_letter('srcStorageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('srcStorageName' + '}'), request.src_storage_name if request.src_storage_name is not None else '')
        else:
            if request.src_storage_name is not None:
                query_params.append((self.__downcase_first_letter('srcStorageName'), request.src_storage_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('destStorageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('destStorageName' + '}'), request.dest_storage_name if request.dest_storage_name is not None else '')
        else:
            if request.dest_storage_name is not None:
                query_params.append((self.__downcase_first_letter('destStorageName'), request.dest_storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def get_disc_usage(self, request, **kwargs):  # noqa: E501
        """Get disc usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param storage_name str : Storage name
        :return: DiscUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_disc_usage_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_disc_usage_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_disc_usage_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_disc_usage_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_disc_usage_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get disc usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_disc_usage_request object with parameters
        :return: DiscUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_disc_usage" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path = '/tasks/storage/disc'
        path_params = {}

        query_params = []
        if '{' + self.__downcase_first_letter('storageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DiscUsage',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_file_versions(self, request, **kwargs):  # noqa: E501
        """Get file versions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : File path e.g. '/file.ext' (required)
        :param storage_name str : Storage name
        :return: FileVersions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_file_versions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_file_versions_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_file_versions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_file_versions_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_file_versions_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get file versions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_file_versions_request object with parameters
        :return: FileVersions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_versions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `get_file_versions`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/version/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileVersions',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def object_exists(self, request, **kwargs):  # noqa: E501
        """Check if file or folder exists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param path str : File or folder path e.g. '/file.ext' or '/folder' (required)
        :param storage_name str : Storage name
        :param version_id str : File version ID
        :return: ObjectExist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.object_exists_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.object_exists_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.object_exists_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.object_exists_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def object_exists_with_http_info(self, request, **kwargs):  # noqa: E501
        """Check if file or folder exists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request object_exists_request object with parameters
        :return: ObjectExist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method object_exists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if request.path is None:
            raise ValueError("Missing the required parameter `path` when calling `object_exists`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/exist/{path}'
        path_params = {}
        if request.path is not None:
            path_params[self.__downcase_first_letter('path')] = request.path  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storageName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storageName' + '}'), request.storage_name if request.storage_name is not None else '')
        else:
            if request.storage_name is not None:
                query_params.append((self.__downcase_first_letter('storageName'), request.storage_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('versionId') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('versionId' + '}'), request.version_id if request.version_id is not None else '')
        else:
            if request.version_id is not None:
                query_params.append((self.__downcase_first_letter('versionId'), request.version_id))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectExist',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def storage_exists(self, request, **kwargs):  # noqa: E501
        """Check if storage exists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param storage_name str : Storage name (required)
        :return: StorageExist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.storage_exists_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.storage_exists_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.storage_exists_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.storage_exists_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def storage_exists_with_http_info(self, request, **kwargs):  # noqa: E501
        """Check if storage exists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request storage_exists_request object with parameters
        :return: StorageExist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method storage_exists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'storage_name' is set
        if request.storage_name is None:
            raise ValueError("Missing the required parameter `storage_name` when calling `storage_exists`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/storage/{storageName}/exist'
        path_params = {}
        if request.storage_name is not None:
            path_params[self.__downcase_first_letter('storageName')] = request.storage_name  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StorageExist',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def delete_assignment(self, request, **kwargs):  # noqa: E501
        """Deletes a project assignment with all references to it.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param assignment_uid int : assignment Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :param file_name str : The name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_assignment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_assignment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_assignment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_assignment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_assignment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes a project assignment with all references to it.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_assignment_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_assignment`")  # noqa: E501
        # verify the required parameter 'assignment_uid' is set
        if request.assignment_uid is None:
            raise ValueError("Missing the required parameter `assignment_uid` when calling `delete_assignment`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/assignments/{assignmentUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.assignment_uid is not None:
            path_params[self.__downcase_first_letter('assignmentUid')] = request.assignment_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_assignment(self, request, **kwargs):  # noqa: E501
        """Read project assignment with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param assignment_uid int : Assignment Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AssignmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_assignment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_assignment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_assignment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_assignment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_assignment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read project assignment with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_assignment_request object with parameters
        :return: AssignmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_assignment`")  # noqa: E501
        # verify the required parameter 'assignment_uid' is set
        if request.assignment_uid is None:
            raise ValueError("Missing the required parameter `assignment_uid` when calling `get_assignment`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/assignments/{assignmentUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.assignment_uid is not None:
            path_params[self.__downcase_first_letter('assignmentUid')] = request.assignment_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssignmentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_assignment_timephased_data(self, request, **kwargs):  # noqa: E501
        """Get timescaled data for an assignment with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param assignment_uid int : Uid of assignment to get timephased data for. (required)
        :param type str : Type of timephased data to get.
        :param start_date datetime : Start date.
        :param end_date datetime : End date.
        :param folder str : The document folder.
        :param storage str : The document storage.
        :return: TimephasedDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_assignment_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_assignment_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_assignment_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_assignment_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_assignment_timephased_data_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get timescaled data for an assignment with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_assignment_timephased_data_request object with parameters
        :return: TimephasedDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_assignment_timephased_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_assignment_timephased_data`")  # noqa: E501
        # verify the required parameter 'assignment_uid' is set
        if request.assignment_uid is None:
            raise ValueError("Missing the required parameter `assignment_uid` when calling `get_assignment_timephased_data`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/assignments/{assignmentUid}/timeScaleData'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.assignment_uid is not None:
            path_params[self.__downcase_first_letter('assignmentUid')] = request.assignment_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('type') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('type' + '}'), request.type if request.type is not None else '')
        else:
            if request.type is not None:
                query_params.append((self.__downcase_first_letter('type'), request.type))  # noqa: E501
        if '{' + self.__downcase_first_letter('startDate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('startDate' + '}'), request.start_date if request.start_date is not None else '')
        else:
            if request.start_date is not None:
                query_params.append((self.__downcase_first_letter('startDate'), request.start_date))  # noqa: E501
        if '{' + self.__downcase_first_letter('endDate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('endDate' + '}'), request.end_date if request.end_date is not None else '')
        else:
            if request.end_date is not None:
                query_params.append((self.__downcase_first_letter('endDate'), request.end_date))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TimephasedDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_assignments(self, request, **kwargs):  # noqa: E501
        """Get project&#39;s assignment items.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AssignmentItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_assignments_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_assignments_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_assignments_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_assignments_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_assignments_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get project&#39;s assignment items.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_assignments_request object with parameters
        :return: AssignmentItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_assignments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_assignments`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/assignments'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssignmentItemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_assignment(self, request, **kwargs):  # noqa: E501
        """Adds a new assignment to a project and returns assignment item in a response.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : The unique id of the task to be assigned. (required)
        :param resource_uid int : The unique id of the resource to be assigned. (required)
        :param units float : The units for the new assignment. If not specified, 'cost' value is used.
        :param cost float : The cost for a new assignment. If not specified, default value is used.
        :param file_name str : The name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AssignmentItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_assignment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_assignment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_assignment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_assignment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_assignment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds a new assignment to a project and returns assignment item in a response.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_assignment_request object with parameters
        :return: AssignmentItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_assignment`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `post_assignment`")  # noqa: E501
        # verify the required parameter 'resource_uid' is set
        if request.resource_uid is None:
            raise ValueError("Missing the required parameter `resource_uid` when calling `post_assignment`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/assignments'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('taskUid') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('taskUid' + '}'), request.task_uid if request.task_uid is not None else '')
        else:
            if request.task_uid is not None:
                query_params.append((self.__downcase_first_letter('taskUid'), request.task_uid))  # noqa: E501
        if '{' + self.__downcase_first_letter('resourceUid') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('resourceUid' + '}'), request.resource_uid if request.resource_uid is not None else '')
        else:
            if request.resource_uid is not None:
                query_params.append((self.__downcase_first_letter('resourceUid'), request.resource_uid))  # noqa: E501
        if '{' + self.__downcase_first_letter('units') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('units' + '}'), request.units if request.units is not None else '')
        else:
            if request.units is not None:
                query_params.append((self.__downcase_first_letter('units'), request.units))  # noqa: E501
        if '{' + self.__downcase_first_letter('cost') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('cost' + '}'), request.cost if request.cost is not None else '')
        else:
            if request.cost is not None:
                query_params.append((self.__downcase_first_letter('cost'), request.cost))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssignmentItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_assignment(self, request, **kwargs):  # noqa: E501
        """Updates resources assignment with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name (required)
        :param assignment_uid int : Assignment UID (required)
        :param assignment ResourceAssignment : Assignment DTO (required)
        :param mode str : Project's calculation mode
        :param recalculate bool : boolean value
        :param storage str : The document storage
        :param folder str : The document storage
        :param file_name str : The filename to save Changes
        :return: AssignmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_assignment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_assignment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_assignment_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_assignment_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_assignment_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates resources assignment with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_assignment_request object with parameters
        :return: AssignmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_assignment`")  # noqa: E501
        # verify the required parameter 'assignment_uid' is set
        if request.assignment_uid is None:
            raise ValueError("Missing the required parameter `assignment_uid` when calling `put_assignment`")  # noqa: E501
        # verify the required parameter 'assignment' is set
        if request.assignment is None:
            raise ValueError("Missing the required parameter `assignment` when calling `put_assignment`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/assignments/{assignmentUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.assignment_uid is not None:
            path_params[self.__downcase_first_letter('assignmentUid')] = request.assignment_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('mode') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('mode' + '}'), request.mode if request.mode is not None else '')
        else:
            if request.mode is not None:
                query_params.append((self.__downcase_first_letter('mode'), request.mode))  # noqa: E501
        if '{' + self.__downcase_first_letter('recalculate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('recalculate' + '}'), request.recalculate if request.recalculate is not None else '')
        else:
            if request.recalculate is not None:
                query_params.append((self.__downcase_first_letter('recalculate'), request.recalculate))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.assignment is not None:
            body_params = request.assignment
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssignmentResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def delete_calendar(self, request, **kwargs):  # noqa: E501
        """Deletes a project calendar  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param calendar_uid int : Calendar's Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_calendar_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_calendar_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_calendar_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_calendar_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_calendar_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes a project calendar  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_calendar_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_calendar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_calendar`")  # noqa: E501
        # verify the required parameter 'calendar_uid' is set
        if request.calendar_uid is None:
            raise ValueError("Missing the required parameter `calendar_uid` when calling `delete_calendar`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/calendars/{calendarUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.calendar_uid is not None:
            path_params[self.__downcase_first_letter('calendarUid')] = request.calendar_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_calendar_exception(self, request, **kwargs):  # noqa: E501
        """Deletes calendar exception from calendar exceptions collection.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param calendar_uid int : Calendar Uid (required)
        :param index int : Index of the calendar exception. See CalendarException.Index property. (required)
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_calendar_exception_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes calendar exception from calendar exceptions collection.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_calendar_exception_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_calendar_exception" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_calendar_exception`")  # noqa: E501
        # verify the required parameter 'calendar_uid' is set
        if request.calendar_uid is None:
            raise ValueError("Missing the required parameter `calendar_uid` when calling `delete_calendar_exception`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_calendar_exception`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/calendars/{calendarUid}/calendarExceptions/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.calendar_uid is not None:
            path_params[self.__downcase_first_letter('calendarUid')] = request.calendar_uid  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('index')] = request.index  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_calendar(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s calendar with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param calendar_uid int : Calendar's Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: CalendarResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_calendar_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_calendar_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_calendar_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_calendar_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_calendar_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s calendar with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_calendar_request object with parameters
        :return: CalendarResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_calendar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_calendar`")  # noqa: E501
        # verify the required parameter 'calendar_uid' is set
        if request.calendar_uid is None:
            raise ValueError("Missing the required parameter `calendar_uid` when calling `get_calendar`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/calendars/{calendarUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.calendar_uid is not None:
            path_params[self.__downcase_first_letter('calendarUid')] = request.calendar_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CalendarResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_calendar_exceptions(self, request, **kwargs):  # noqa: E501
        """Get a list of calendar&#39;s exceptions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param calendar_uid int : Calendar's Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: CalendarExceptionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_calendar_exceptions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_calendar_exceptions_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_calendar_exceptions_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_calendar_exceptions_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_calendar_exceptions_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a list of calendar&#39;s exceptions.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_calendar_exceptions_request object with parameters
        :return: CalendarExceptionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_calendar_exceptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_calendar_exceptions`")  # noqa: E501
        # verify the required parameter 'calendar_uid' is set
        if request.calendar_uid is None:
            raise ValueError("Missing the required parameter `calendar_uid` when calling `get_calendar_exceptions`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/calendars/{calendarUid}/calendarExceptions'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.calendar_uid is not None:
            path_params[self.__downcase_first_letter('calendarUid')] = request.calendar_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CalendarExceptionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_calendar_work_weeks(self, request, **kwargs):  # noqa: E501
        """Gets the collection of work weeks of the specified calendar.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param calendar_uid int : Calendar Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: CalendarWorkWeeksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_calendar_work_weeks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_calendar_work_weeks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_calendar_work_weeks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_calendar_work_weeks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_calendar_work_weeks_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets the collection of work weeks of the specified calendar.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_calendar_work_weeks_request object with parameters
        :return: CalendarWorkWeeksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_calendar_work_weeks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_calendar_work_weeks`")  # noqa: E501
        # verify the required parameter 'calendar_uid' is set
        if request.calendar_uid is None:
            raise ValueError("Missing the required parameter `calendar_uid` when calling `get_calendar_work_weeks`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/calendars/{calendarUid}/workWeeks'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.calendar_uid is not None:
            path_params[self.__downcase_first_letter('calendarUid')] = request.calendar_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CalendarWorkWeeksResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_calendars(self, request, **kwargs):  # noqa: E501
        """Read project calendar items.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: CalendarItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_calendars_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_calendars_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_calendars_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_calendars_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_calendars_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read project calendar items.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_calendars_request object with parameters
        :return: CalendarItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_calendars" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_calendars`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/calendars'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CalendarItemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_calendar(self, request, **kwargs):  # noqa: E501
        """Adds a new calendar to project file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param calendar Calendar : Calendar DTO (required)
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: CalendarItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_calendar_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_calendar_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_calendar_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_calendar_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_calendar_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds a new calendar to project file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_calendar_request object with parameters
        :return: CalendarItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_calendar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_calendar`")  # noqa: E501
        # verify the required parameter 'calendar' is set
        if request.calendar is None:
            raise ValueError("Missing the required parameter `calendar` when calling `post_calendar`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/calendars'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.calendar is not None:
            body_params = request.calendar
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CalendarItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_calendar_exception(self, request, **kwargs):  # noqa: E501
        """Adds a new calendar exception to a calendar.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param calendar_uid int : Calendar's Uid (required)
        :param calendar_exception CalendarException : CalendarException DTO (required)
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_calendar_exception_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds a new calendar exception to a calendar.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_calendar_exception_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_calendar_exception" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_calendar_exception`")  # noqa: E501
        # verify the required parameter 'calendar_uid' is set
        if request.calendar_uid is None:
            raise ValueError("Missing the required parameter `calendar_uid` when calling `post_calendar_exception`")  # noqa: E501
        # verify the required parameter 'calendar_exception' is set
        if request.calendar_exception is None:
            raise ValueError("Missing the required parameter `calendar_exception` when calling `post_calendar_exception`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/calendars/{calendarUid}/calendarExceptions'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.calendar_uid is not None:
            path_params[self.__downcase_first_letter('calendarUid')] = request.calendar_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.calendar_exception is not None:
            body_params = request.calendar_exception
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_calendar(self, request, **kwargs):  # noqa: E501
        """Edits an existing project calendar.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param calendar_uid int : The Uid of an existing calendar to edit. (required)
        :param calendar Calendar : Modified calendar DTO (required)
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_calendar_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_calendar_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_calendar_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_calendar_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_calendar_with_http_info(self, request, **kwargs):  # noqa: E501
        """Edits an existing project calendar.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_calendar_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_calendar" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_calendar`")  # noqa: E501
        # verify the required parameter 'calendar_uid' is set
        if request.calendar_uid is None:
            raise ValueError("Missing the required parameter `calendar_uid` when calling `put_calendar`")  # noqa: E501
        # verify the required parameter 'calendar' is set
        if request.calendar is None:
            raise ValueError("Missing the required parameter `calendar` when calling `put_calendar`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/calendars'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('calendarUid') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('calendarUid' + '}'), request.calendar_uid if request.calendar_uid is not None else '')
        else:
            if request.calendar_uid is not None:
                query_params.append((self.__downcase_first_letter('calendarUid'), request.calendar_uid))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.calendar is not None:
            body_params = request.calendar
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_calendar_exception(self, request, **kwargs):  # noqa: E501
        """Updates calendar exception.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param calendar_uid int : Calendar Uid (required)
        :param index int : Index of the calendar exception. See CalendarException.Index property. (required)
        :param calendar_exception CalendarException : CalendarException DTO (required)
        :param file_name str : The name of the project document to save changes to. If this parameter              is omitted then the changes will be saved to the source project document.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_calendar_exception_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_calendar_exception_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates calendar exception.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_calendar_exception_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_calendar_exception" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_calendar_exception`")  # noqa: E501
        # verify the required parameter 'calendar_uid' is set
        if request.calendar_uid is None:
            raise ValueError("Missing the required parameter `calendar_uid` when calling `put_calendar_exception`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `put_calendar_exception`")  # noqa: E501
        # verify the required parameter 'calendar_exception' is set
        if request.calendar_exception is None:
            raise ValueError("Missing the required parameter `calendar_exception` when calling `put_calendar_exception`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/calendars/{calendarUid}/calendarExceptions/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.calendar_uid is not None:
            path_params[self.__downcase_first_letter('calendarUid')] = request.calendar_uid  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('index')] = request.index  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.calendar_exception is not None:
            body_params = request.calendar_exception
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def get_critical_path(self, request, **kwargs):  # noqa: E501
        """Returns the list of the tasks which must be completed on time for a project to finish on schedule. Each task of the project is represented as a task item here, which is light-weighted task representation of the project task..  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: TaskItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_critical_path_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_critical_path_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_critical_path_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_critical_path_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_critical_path_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns the list of the tasks which must be completed on time for a project to finish on schedule. Each task of the project is represented as a task item here, which is light-weighted task representation of the project task..  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_critical_path_request object with parameters
        :return: TaskItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_critical_path" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_critical_path`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/criticalPath'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskItemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def get_page_count(self, request, **kwargs):  # noqa: E501
        """Returns page count for the project to be rendered using given Timescale and PresentationFormat  or specified PageSize.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param page_size str : PageSize to get page count for.
        :param presentation_format str : PresentationFormat to get page count for.
        :param timescale str : Timescale to get page count for.
        :param start_date datetime : Start date to get page count for.
        :param end_date datetime : End date to get page count for.
        :param folder str : The document folder
        :param storage str : The document storage.
        :return: PageCountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_page_count_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_page_count_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_page_count_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_page_count_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_page_count_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns page count for the project to be rendered using given Timescale and PresentationFormat  or specified PageSize.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_page_count_request object with parameters
        :return: PageCountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_page_count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_page_count`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/pagecount'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('pageSize') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('pageSize' + '}'), request.page_size if request.page_size is not None else '')
        else:
            if request.page_size is not None:
                query_params.append((self.__downcase_first_letter('pageSize'), request.page_size))  # noqa: E501
        if '{' + self.__downcase_first_letter('presentationFormat') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('presentationFormat' + '}'), request.presentation_format if request.presentation_format is not None else '')
        else:
            if request.presentation_format is not None:
                query_params.append((self.__downcase_first_letter('presentationFormat'), request.presentation_format))  # noqa: E501
        if '{' + self.__downcase_first_letter('timescale') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('timescale' + '}'), request.timescale if request.timescale is not None else '')
        else:
            if request.timescale is not None:
                query_params.append((self.__downcase_first_letter('timescale'), request.timescale))  # noqa: E501
        if '{' + self.__downcase_first_letter('startDate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('startDate' + '}'), request.start_date if request.start_date is not None else '')
        else:
            if request.start_date is not None:
                query_params.append((self.__downcase_first_letter('startDate'), request.start_date))  # noqa: E501
        if '{' + self.__downcase_first_letter('endDate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('endDate' + '}'), request.end_date if request.end_date is not None else '')
        else:
            if request.end_date is not None:
                query_params.append((self.__downcase_first_letter('endDate'), request.end_date))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageCountResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_ids(self, request, **kwargs):  # noqa: E501
        """Get Uids of projects contained in the file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: ProjectIdsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_project_ids_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_project_ids_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_project_ids_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_project_ids_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_project_ids_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get Uids of projects contained in the file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_project_ids_request object with parameters
        :return: ProjectIdsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_ids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_project_ids`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/projectids'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectIdsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_task_document(self, request, **kwargs):  # noqa: E501
        """Get a project document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_task_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_task_document_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_document_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_task_document_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a project document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_task_document_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task_document" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_task_document`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_task_document_with_format(self, request, **kwargs):  # noqa: E501
        """Get a project document in the specified format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param format str : The format of the resulting file. (required)
        :param return_as_zip_archive bool : If parameter is true, HTML resources are included as separate files and returned along with the resulting html file as a zip package.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_task_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_task_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_task_document_with_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a project document in the specified format  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_task_document_with_format_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task_document_with_format" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_task_document_with_format`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `get_task_document_with_format`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/format'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('format') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if '{' + self.__downcase_first_letter('returnAsZipArchive') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('returnAsZipArchive' + '}'), request.return_as_zip_archive if request.return_as_zip_archive is not None else '')
        else:
            if request.return_as_zip_archive is not None:
                query_params.append((self.__downcase_first_letter('returnAsZipArchive'), request.return_as_zip_archive))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_import_project_from_db(self, request, **kwargs):  # noqa: E501
        """Imports project from database with the specified connection string and saves it to specified file with the specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param database_type str : The type of source database. The supported values are (Msp, Mpd, Primavera). (required)
        :param connection_string str : The connection string to the source database. (required)
        :param project_uid str : Uid of the project to import. (required)
        :param filename str : The name of the resulting file. (required)
        :param format str : Format of the resulting file.
        :param folder str : The document folder.
        :param storage str : The document storage.
        :param database_schema str : Schema of Microsoft project database (if applicable)
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_import_project_from_db_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_import_project_from_db_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_import_project_from_db_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_import_project_from_db_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_import_project_from_db_with_http_info(self, request, **kwargs):  # noqa: E501
        """Imports project from database with the specified connection string and saves it to specified file with the specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_import_project_from_db_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_import_project_from_db" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'database_type' is set
        if request.database_type is None:
            raise ValueError("Missing the required parameter `database_type` when calling `put_import_project_from_db`")  # noqa: E501
        # verify the required parameter 'connection_string' is set
        if request.connection_string is None:
            raise ValueError("Missing the required parameter `connection_string` when calling `put_import_project_from_db`")  # noqa: E501
        # verify the required parameter 'project_uid' is set
        if request.project_uid is None:
            raise ValueError("Missing the required parameter `project_uid` when calling `put_import_project_from_db`")  # noqa: E501
        # verify the required parameter 'filename' is set
        if request.filename is None:
            raise ValueError("Missing the required parameter `filename` when calling `put_import_project_from_db`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/importfromdb'
        path_params = {}

        query_params = []
        if '{' + self.__downcase_first_letter('databaseType') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('databaseType' + '}'), request.database_type if request.database_type is not None else '')
        else:
            if request.database_type is not None:
                query_params.append((self.__downcase_first_letter('databaseType'), request.database_type))  # noqa: E501
        if '{' + self.__downcase_first_letter('projectUid') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('projectUid' + '}'), request.project_uid if request.project_uid is not None else '')
        else:
            if request.project_uid is not None:
                query_params.append((self.__downcase_first_letter('projectUid'), request.project_uid))  # noqa: E501
        if '{' + self.__downcase_first_letter('filename') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('filename' + '}'), request.filename if request.filename is not None else '')
        else:
            if request.filename is not None:
                query_params.append((self.__downcase_first_letter('filename'), request.filename))  # noqa: E501
        if '{' + self.__downcase_first_letter('format') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('databaseSchema') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('databaseSchema' + '}'), request.database_schema if request.database_schema is not None else '')
        else:
            if request.database_schema is not None:
                query_params.append((self.__downcase_first_letter('databaseSchema'), request.database_schema))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.connection_string is not None:
            body_params = request.connection_string
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_import_project_from_file(self, request, **kwargs):  # noqa: E501
        """Imports project from primavera db formats (Primavera SQLite .db or Primavera xml) and saves it to specified file with the specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param project_uid str : Uid of the project to import. (required)
        :param filename str : The name of the resulting file. (required)
        :param file_type str : The type of file to import. The supported values are (PrimaveraSqliteDb, PrimaveraXml).
        :param folder str : The document folder.
        :param storage str : The document storage.
        :param output_file_format str : The format of the resulting file.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_import_project_from_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_import_project_from_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_import_project_from_file_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_import_project_from_file_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_import_project_from_file_with_http_info(self, request, **kwargs):  # noqa: E501
        """Imports project from primavera db formats (Primavera SQLite .db or Primavera xml) and saves it to specified file with the specified format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_import_project_from_file_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_import_project_from_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_import_project_from_file`")  # noqa: E501
        # verify the required parameter 'project_uid' is set
        if request.project_uid is None:
            raise ValueError("Missing the required parameter `project_uid` when calling `put_import_project_from_file`")  # noqa: E501
        # verify the required parameter 'filename' is set
        if request.filename is None:
            raise ValueError("Missing the required parameter `filename` when calling `put_import_project_from_file`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/import'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('projectUid') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('projectUid' + '}'), request.project_uid if request.project_uid is not None else '')
        else:
            if request.project_uid is not None:
                query_params.append((self.__downcase_first_letter('projectUid'), request.project_uid))  # noqa: E501
        if '{' + self.__downcase_first_letter('filename') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('filename' + '}'), request.filename if request.filename is not None else '')
        else:
            if request.filename is not None:
                query_params.append((self.__downcase_first_letter('filename'), request.filename))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileType') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileType' + '}'), request.file_type if request.file_type is not None else '')
        else:
            if request.file_type is not None:
                query_params.append((self.__downcase_first_letter('fileType'), request.file_type))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('outputFileFormat') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('outputFileFormat' + '}'), request.output_file_format if request.output_file_format is not None else '')
        else:
            if request.output_file_format is not None:
                query_params.append((self.__downcase_first_letter('outputFileFormat'), request.output_file_format))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_import_project_from_project_online(self, request, **kwargs):  # noqa: E501
        """Imports project from Project Online and saves it to specified file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the resulting file. (required)
        :param guid str : Guid of the project to import. (required)
        :param site_url str : The URL of PWA (Project Web Access) API of Project Online (required)
        :param user_name str : The user name for the sharepoint site.
        :param format str : Format of the resulting file.
        :param folder str : The document folder.
        :param storage str : The document storage.
        :param x_project_online_token str : Authorization token (SPOIDCRL) for SharePoint's PWA (Project Web Access). For example, in c# it can be retrieved using SharePointOnlineCredentials class from Microsoft.SharePoint.Client.Runtime assembly
        :param x_sharepoint_password str : The password for the SharePoint site.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_import_project_from_project_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_import_project_from_project_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_import_project_from_project_online_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_import_project_from_project_online_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_import_project_from_project_online_with_http_info(self, request, **kwargs):  # noqa: E501
        """Imports project from Project Online and saves it to specified file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_import_project_from_project_online_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_import_project_from_project_online" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_import_project_from_project_online`")  # noqa: E501
        # verify the required parameter 'guid' is set
        if request.guid is None:
            raise ValueError("Missing the required parameter `guid` when calling `put_import_project_from_project_online`")  # noqa: E501
        # verify the required parameter 'site_url' is set
        if request.site_url is None:
            raise ValueError("Missing the required parameter `site_url` when calling `put_import_project_from_project_online`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/importfromprojectonline'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('siteUrl') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('siteUrl' + '}'), request.site_url if request.site_url is not None else '')
        else:
            if request.site_url is not None:
                query_params.append((self.__downcase_first_letter('siteUrl'), request.site_url))  # noqa: E501
        if '{' + self.__downcase_first_letter('userName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('userName' + '}'), request.user_name if request.user_name is not None else '')
        else:
            if request.user_name is not None:
                query_params.append((self.__downcase_first_letter('userName'), request.user_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('format') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}
        if request.x_project_online_token is not None:
            header_params[self.__downcase_first_letter('x-project-online-token')] = request.x_project_online_token  # noqa: E501
        if request.x_sharepoint_password is not None:
            header_params[self.__downcase_first_letter('x-sharepoint-password')] = request.x_sharepoint_password  # noqa: E501

        form_params = []
        local_var_files = []

        body_params = None
        if request.guid is not None:
            body_params = request.guid
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def get_document_properties(self, request, **kwargs):  # noqa: E501
        """Get a collection of a project&#39;s document properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: DocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a collection of a project&#39;s document properties.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_document_properties_request object with parameters
        :return: DocumentPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_properties`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/documentproperties'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentPropertiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_property(self, request, **kwargs):  # noqa: E501
        """Get a document property by name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param property_name str : The property name. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a document property by name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_document_property_request object with parameters
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_property" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_document_property`")  # noqa: E501
        # verify the required parameter 'property_name' is set
        if request.property_name is None:
            raise ValueError("Missing the required parameter `property_name` when calling `get_document_property`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/documentproperties/{propertyName}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.property_name is not None:
            path_params[self.__downcase_first_letter('propertyName')] = request.property_name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentPropertyResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_document_property(self, request, **kwargs):  # noqa: E501
        """Set/create document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param property_name str : The property name. (required)
        :param _property DocumentProperty : DocumentProperty with new property value. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :param filename str : Name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document.
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Set/create document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_document_property_request object with parameters
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_document_property" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_document_property`")  # noqa: E501
        # verify the required parameter 'property_name' is set
        if request.property_name is None:
            raise ValueError("Missing the required parameter `property_name` when calling `post_document_property`")  # noqa: E501
        # verify the required parameter '_property' is set
        if request._property is None:
            raise ValueError("Missing the required parameter `_property` when calling `post_document_property`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/documentproperties/{propertyName}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.property_name is not None:
            path_params[self.__downcase_first_letter('propertyName')] = request.property_name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('filename') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('filename' + '}'), request.filename if request.filename is not None else '')
        else:
            if request.filename is not None:
                query_params.append((self.__downcase_first_letter('filename'), request.filename))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request._property is not None:
            body_params = request._property
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentPropertyResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_document_property(self, request, **kwargs):  # noqa: E501
        """Set/create document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The document name. (required)
        :param property_name str : The property name. (required)
        :param _property DocumentProperty : DocumentProperty with new property value. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :param filename str : Name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document.
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_document_property_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_document_property_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_document_property_with_http_info(self, request, **kwargs):  # noqa: E501
        """Set/create document property.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_document_property_request object with parameters
        :return: DocumentPropertyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_document_property" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_document_property`")  # noqa: E501
        # verify the required parameter 'property_name' is set
        if request.property_name is None:
            raise ValueError("Missing the required parameter `property_name` when calling `put_document_property`")  # noqa: E501
        # verify the required parameter '_property' is set
        if request._property is None:
            raise ValueError("Missing the required parameter `_property` when calling `put_document_property`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/documentproperties/{propertyName}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.property_name is not None:
            path_params[self.__downcase_first_letter('propertyName')] = request.property_name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('filename') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('filename' + '}'), request.filename if request.filename is not None else '')
        else:
            if request.filename is not None:
                query_params.append((self.__downcase_first_letter('filename'), request.filename))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request._property is not None:
            body_params = request._property
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentPropertyResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def delete_extended_attribute_by_index(self, request, **kwargs):  # noqa: E501
        """Delete a project extended attribute.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param index int : Index (See ExtendedAttributeItem.Index property) or FieldId of the extended attribute. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_extended_attribute_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_extended_attribute_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_extended_attribute_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_extended_attribute_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_extended_attribute_by_index_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete a project extended attribute.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_extended_attribute_by_index_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_extended_attribute_by_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_extended_attribute_by_index`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_extended_attribute_by_index`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/extendedAttributes/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('index')] = request.index  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_extended_attribute_by_index(self, request, **kwargs):  # noqa: E501
        """Get a project extended attribute definition with the specified index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param index int : Index (See ExtendedAttributeItem.Index property) or FieldId of the extended attribute. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: ExtendedAttributeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_extended_attribute_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_extended_attribute_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_extended_attribute_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_extended_attribute_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_extended_attribute_by_index_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a project extended attribute definition with the specified index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_extended_attribute_by_index_request object with parameters
        :return: ExtendedAttributeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_extended_attribute_by_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_extended_attribute_by_index`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_extended_attribute_by_index`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/extendedAttributes/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('index')] = request.index  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExtendedAttributeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_extended_attributes(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s extended attributes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: ExtendedAttributeItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_extended_attributes_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_extended_attributes_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_extended_attributes_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_extended_attributes_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_extended_attributes_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s extended attributes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_extended_attributes_request object with parameters
        :return: ExtendedAttributeItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_extended_attributes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_extended_attributes`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/extendedAttributes'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExtendedAttributeItemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_extended_attribute(self, request, **kwargs):  # noqa: E501
        """Add a new extended attribute definition to a project or  updates existing attribute definition (with the same FieldId).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param extended_attribute ExtendedAttributeDefinition : Definition of the extended attribute to add. (required)
        :param name str : The name of the file. (required)
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: ExtendedAttributeItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_extended_attribute_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_extended_attribute_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_extended_attribute_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_extended_attribute_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_extended_attribute_with_http_info(self, request, **kwargs):  # noqa: E501
        """Add a new extended attribute definition to a project or  updates existing attribute definition (with the same FieldId).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_extended_attribute_request object with parameters
        :return: ExtendedAttributeItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_extended_attribute" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'extended_attribute' is set
        if request.extended_attribute is None:
            raise ValueError("Missing the required parameter `extended_attribute` when calling `put_extended_attribute`")  # noqa: E501
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_extended_attribute`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/extendedAttributes'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.extended_attribute is not None:
            body_params = request.extended_attribute
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExtendedAttributeItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def delete_outline_code_by_index(self, request, **kwargs):  # noqa: E501
        """Deletes a project outline code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param index int : Index of the outline code. See OutlineCodeItem.Index property. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_outline_code_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_outline_code_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_outline_code_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_outline_code_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_outline_code_by_index_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes a project outline code  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_outline_code_by_index_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_outline_code_by_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_outline_code_by_index`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_outline_code_by_index`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/outlineCodes/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('index')] = request.index  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_outline_code_by_index(self, request, **kwargs):  # noqa: E501
        """Get outline code by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param index int : Index of the outline code. See OutlineCodeItem.Index property. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: OutlineCodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_outline_code_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_outline_code_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_outline_code_by_index_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_outline_code_by_index_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_outline_code_by_index_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get outline code by index.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_outline_code_by_index_request object with parameters
        :return: OutlineCodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_outline_code_by_index" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_outline_code_by_index`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `get_outline_code_by_index`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/outlineCodes/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('index')] = request.index  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OutlineCodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_outline_codes(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s outline codes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: OutlineCodeItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_outline_codes_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_outline_codes_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_outline_codes_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_outline_codes_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_outline_codes_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s outline codes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_outline_codes_request object with parameters
        :return: OutlineCodeItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_outline_codes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_outline_codes`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/outlineCodes'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OutlineCodeItemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def create_new_project(self, request, **kwargs):  # noqa: E501
        """Creates new project in Project Server\\Project Online instance.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param site_url str : The URL of PWA (Project Web Access) API of Project Online. (required)
        :param user_name str : The user name for the sharepoint site.
        :param save_options ProjectServerSaveOptionsDTO : Dispensable save options for Project Server\\Project Online.
        :param folder str : The document folder.
        :param storage str : The document storage.
        :param x_project_online_token str : Authorization token (SPOIDCRL) for SharePoint's PWA (Project Web Access). For example, in c# it can be retrieved using SharePointOnlineCredentials class from Microsoft.SharePoint.Client.Runtime assembly
        :param x_sharepoint_password str : The password for the SharePoint site.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.create_new_project_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_new_project_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.create_new_project_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_new_project_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def create_new_project_with_http_info(self, request, **kwargs):  # noqa: E501
        """Creates new project in Project Server\\Project Online instance.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request create_new_project_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_new_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `create_new_project`")  # noqa: E501
        # verify the required parameter 'site_url' is set
        if request.site_url is None:
            raise ValueError("Missing the required parameter `site_url` when calling `create_new_project`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/projectOnline/{siteUrl}/{name}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.site_url is not None:
            path_params[self.__downcase_first_letter('siteUrl')] = request.site_url  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('userName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('userName' + '}'), request.user_name if request.user_name is not None else '')
        else:
            if request.user_name is not None:
                query_params.append((self.__downcase_first_letter('userName'), request.user_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}
        if request.x_project_online_token is not None:
            header_params[self.__downcase_first_letter('x-project-online-token')] = request.x_project_online_token  # noqa: E501
        if request.x_sharepoint_password is not None:
            header_params[self.__downcase_first_letter('x-sharepoint-password')] = request.x_sharepoint_password  # noqa: E501

        form_params = []
        local_var_files = []

        body_params = None
        if request.save_options is not None:
            body_params = request.save_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project_list(self, request, **kwargs):  # noqa: E501
        """Gets the list of published projects in the current Project Online account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param site_url str : The URL of PWA (Project Web Access) API of Project Online. (required)
        :param user_name str : The user name for the sharepoint site.
        :param x_project_online_token str : Authorization token (SPOIDCRL) for SharePoint's PWA (Project Web Access). For example, in c# it can be retrieved using SharePointOnlineCredentials class from Microsoft.SharePoint.Client.Runtime assembly
        :param x_sharepoint_password str : The password for the SharePoint site.
        :return: ProjectListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_project_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_project_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_project_list_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_project_list_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_project_list_with_http_info(self, request, **kwargs):  # noqa: E501
        """Gets the list of published projects in the current Project Online account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_project_list_request object with parameters
        :return: ProjectListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_url' is set
        if request.site_url is None:
            raise ValueError("Missing the required parameter `site_url` when calling `get_project_list`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/projectOnline/projectList'
        path_params = {}

        query_params = []
        if '{' + self.__downcase_first_letter('siteUrl') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('siteUrl' + '}'), request.site_url if request.site_url is not None else '')
        else:
            if request.site_url is not None:
                query_params.append((self.__downcase_first_letter('siteUrl'), request.site_url))  # noqa: E501
        if '{' + self.__downcase_first_letter('userName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('userName' + '}'), request.user_name if request.user_name is not None else '')
        else:
            if request.user_name is not None:
                query_params.append((self.__downcase_first_letter('userName'), request.user_name))  # noqa: E501

        header_params = {}
        if request.x_project_online_token is not None:
            header_params[self.__downcase_first_letter('x-project-online-token')] = request.x_project_online_token  # noqa: E501
        if request.x_sharepoint_password is not None:
            header_params[self.__downcase_first_letter('x-sharepoint-password')] = request.x_sharepoint_password  # noqa: E501

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectListResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_project(self, request, **kwargs):  # noqa: E501
        """Updates existing project in Project Server\\Project Online instance. The existing project will be overwritten.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param site_url str : The URL of PWA (Project Web Access) API of Project Online. (required)
        :param user_name str : The user name for the sharepoint site.
        :param save_options ProjectServerSaveOptionsDTO : Dispensable save options for Project Server\\Project Online.
        :param folder str : The document folder.
        :param storage str : The document storage.
        :param x_project_online_token str : Authorization token (SPOIDCRL) for SharePoint's PWA (Project Web Access). For example, in c# it can be retrieved using SharePointOnlineCredentials class from Microsoft.SharePoint.Client.Runtime assembly
        :param x_sharepoint_password str : The password for the SharePoint site.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_project_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_project_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.update_project_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_project_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_project_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates existing project in Project Server\\Project Online instance. The existing project will be overwritten.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request update_project_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `update_project`")  # noqa: E501
        # verify the required parameter 'site_url' is set
        if request.site_url is None:
            raise ValueError("Missing the required parameter `site_url` when calling `update_project`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/projectOnline/{siteUrl}/{name}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.site_url is not None:
            path_params[self.__downcase_first_letter('siteUrl')] = request.site_url  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('userName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('userName' + '}'), request.user_name if request.user_name is not None else '')
        else:
            if request.user_name is not None:
                query_params.append((self.__downcase_first_letter('userName'), request.user_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}
        if request.x_project_online_token is not None:
            header_params[self.__downcase_first_letter('x-project-online-token')] = request.x_project_online_token  # noqa: E501
        if request.x_sharepoint_password is not None:
            header_params[self.__downcase_first_letter('x-sharepoint-password')] = request.x_sharepoint_password  # noqa: E501

        form_params = []
        local_var_files = []

        body_params = None
        if request.save_options is not None:
            body_params = request.save_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def put_recalculate_project(self, request, **kwargs):  # noqa: E501
        """Reschedules all project tasks ids, outline levels, start/finish dates, sets early/late dates, calculates slacks, work and cost fields.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The filename (required)
        :param mode str : Project's calculation mode
        :param validate bool : If true the validation of recalculation will be performed. What data is validated:     At the moment only basic validation of task and task link date ranges is implemented.     Task's date ranges (e.g. ActualStart - ActualFinish, EarlyStart - EarlyFinish, etc.) as well as Task Links dates will be checked against the date criteria that start date is less or equal than finish date.
        :param file_name str : The filename to save the changes
        :param storage str : The document storage
        :param folder str : The document folder
        :return: ProjectRecalculateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_recalculate_project_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_recalculate_project_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_recalculate_project_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_recalculate_project_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_recalculate_project_with_http_info(self, request, **kwargs):  # noqa: E501
        """Reschedules all project tasks ids, outline levels, start/finish dates, sets early/late dates, calculates slacks, work and cost fields.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_recalculate_project_request object with parameters
        :return: ProjectRecalculateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_recalculate_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_recalculate_project`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/recalculate/project'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('mode') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('mode' + '}'), request.mode if request.mode is not None else '')
        else:
            if request.mode is not None:
                query_params.append((self.__downcase_first_letter('mode'), request.mode))  # noqa: E501
        if '{' + self.__downcase_first_letter('validate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('validate' + '}'), request.validate if request.validate is not None else '')
        else:
            if request.validate is not None:
                query_params.append((self.__downcase_first_letter('validate'), request.validate))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProjectRecalculateResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_recalculate_project_resource_fields(self, request, **kwargs):  # noqa: E501
        """Recalculate project resource fields  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file (required)
        :param storage str : The document storage
        :param folder str : The document folder
        :param file_name str : The document fileName
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_recalculate_project_resource_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_recalculate_project_resource_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_recalculate_project_resource_fields_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_recalculate_project_resource_fields_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_recalculate_project_resource_fields_with_http_info(self, request, **kwargs):  # noqa: E501
        """Recalculate project resource fields  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_recalculate_project_resource_fields_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_recalculate_project_resource_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_recalculate_project_resource_fields`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/recalculate/resourceFields'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_recalculate_project_uncomplete_work_to_start_after(self, request, **kwargs):  # noqa: E501
        """Recalculate project uncomplete work  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name (required)
        :param after datetime : DateTime (from System lib) (required)
        :param storage str : The document storage 
        :param folder str : The document folder
        :param file_name str : The filename to save the changes
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_recalculate_project_uncomplete_work_to_start_after_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_recalculate_project_uncomplete_work_to_start_after_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_recalculate_project_uncomplete_work_to_start_after_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_recalculate_project_uncomplete_work_to_start_after_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_recalculate_project_uncomplete_work_to_start_after_with_http_info(self, request, **kwargs):  # noqa: E501
        """Recalculate project uncomplete work  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_recalculate_project_uncomplete_work_to_start_after_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_recalculate_project_uncomplete_work_to_start_after" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_recalculate_project_uncomplete_work_to_start_after`")  # noqa: E501
        # verify the required parameter 'after' is set
        if request.after is None:
            raise ValueError("Missing the required parameter `after` when calling `put_recalculate_project_uncomplete_work_to_start_after`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/recalculate/uncompleteWorkToStartAfter'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.after is not None:
            body_params = request.after
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_recalculate_project_work_as_complete(self, request, **kwargs):  # noqa: E501
        """Recalculate project work as complete   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The filename (required)
        :param complete_through datetime : DateTime (type from System lib) (required)
        :param set_zero_or_hundred_percent_complete_only bool : boolean value
        :param storage str : The document storage
        :param folder str : The document folder
        :param file_name str : The filename to save the changes
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_recalculate_project_work_as_complete_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_recalculate_project_work_as_complete_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_recalculate_project_work_as_complete_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_recalculate_project_work_as_complete_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_recalculate_project_work_as_complete_with_http_info(self, request, **kwargs):  # noqa: E501
        """Recalculate project work as complete   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_recalculate_project_work_as_complete_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_recalculate_project_work_as_complete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_recalculate_project_work_as_complete`")  # noqa: E501
        # verify the required parameter 'complete_through' is set
        if request.complete_through is None:
            raise ValueError("Missing the required parameter `complete_through` when calling `put_recalculate_project_work_as_complete`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/recalculate/projectWorkAsComplete'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('setZeroOrHundredPercentCompleteOnly') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('setZeroOrHundredPercentCompleteOnly' + '}'), request.set_zero_or_hundred_percent_complete_only if request.set_zero_or_hundred_percent_complete_only is not None else '')
        else:
            if request.set_zero_or_hundred_percent_complete_only is not None:
                query_params.append((self.__downcase_first_letter('setZeroOrHundredPercentCompleteOnly'), request.set_zero_or_hundred_percent_complete_only))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.complete_through is not None:
            body_params = request.complete_through
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def get_report_pdf(self, request, **kwargs):  # noqa: E501
        """Returns created report in PDF format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param type str : A type of the project's graphical report. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_report_pdf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_report_pdf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_report_pdf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_report_pdf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_report_pdf_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns created report in PDF format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_report_pdf_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_report_pdf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_report_pdf`")  # noqa: E501
        # verify the required parameter 'type' is set
        if request.type is None:
            raise ValueError("Missing the required parameter `type` when calling `get_report_pdf`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/report'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('type') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('type' + '}'), request.type if request.type is not None else '')
        else:
            if request.type is not None:
                query_params.append((self.__downcase_first_letter('type'), request.type))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def delete_resource(self, request, **kwargs):  # noqa: E501
        """Deletes a project resource with all references to it  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param resource_uid int : Resource Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_resource_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_resource_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_resource_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_resource_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_resource_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes a project resource with all references to it  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_resource_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_resource`")  # noqa: E501
        # verify the required parameter 'resource_uid' is set
        if request.resource_uid is None:
            raise ValueError("Missing the required parameter `resource_uid` when calling `delete_resource`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/resources/{resourceUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.resource_uid is not None:
            path_params[self.__downcase_first_letter('resourceUid')] = request.resource_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_resource(self, request, **kwargs):  # noqa: E501
        """Get project resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param resource_uid int : Resource Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: ResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_resource_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_resource_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_resource_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_resource_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_resource_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get project resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_resource_request object with parameters
        :return: ResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_resource`")  # noqa: E501
        # verify the required parameter 'resource_uid' is set
        if request.resource_uid is None:
            raise ValueError("Missing the required parameter `resource_uid` when calling `get_resource`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/resources/{resourceUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.resource_uid is not None:
            path_params[self.__downcase_first_letter('resourceUid')] = request.resource_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_resource_assignments(self, request, **kwargs):  # noqa: E501
        """Get resource&#39;s assignments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param resource_uid int : Resource Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AssignmentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_resource_assignments_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_resource_assignments_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_resource_assignments_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_resource_assignments_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_resource_assignments_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get resource&#39;s assignments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_resource_assignments_request object with parameters
        :return: AssignmentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_assignments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_resource_assignments`")  # noqa: E501
        # verify the required parameter 'resource_uid' is set
        if request.resource_uid is None:
            raise ValueError("Missing the required parameter `resource_uid` when calling `get_resource_assignments`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/resources/{resourceUid}/assignments'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.resource_uid is not None:
            path_params[self.__downcase_first_letter('resourceUid')] = request.resource_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssignmentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_resource_timephased_data(self, request, **kwargs):  # noqa: E501
        """Get timescaled data for a resource with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param resource_uid int : Uid of resource to get timephased data for. (required)
        :param type str : Type of timephased data to get.
        :param start_date datetime : Start date.
        :param end_date datetime : End date.
        :param folder str : The document folder.
        :param storage str : The document storage.
        :return: TimephasedDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_resource_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_resource_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_resource_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_resource_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_resource_timephased_data_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get timescaled data for a resource with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_resource_timephased_data_request object with parameters
        :return: TimephasedDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_timephased_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_resource_timephased_data`")  # noqa: E501
        # verify the required parameter 'resource_uid' is set
        if request.resource_uid is None:
            raise ValueError("Missing the required parameter `resource_uid` when calling `get_resource_timephased_data`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/resources/{resourceUid}/timeScaleData'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.resource_uid is not None:
            path_params[self.__downcase_first_letter('resourceUid')] = request.resource_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('type') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('type' + '}'), request.type if request.type is not None else '')
        else:
            if request.type is not None:
                query_params.append((self.__downcase_first_letter('type'), request.type))  # noqa: E501
        if '{' + self.__downcase_first_letter('startDate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('startDate' + '}'), request.start_date if request.start_date is not None else '')
        else:
            if request.start_date is not None:
                query_params.append((self.__downcase_first_letter('startDate'), request.start_date))  # noqa: E501
        if '{' + self.__downcase_first_letter('endDate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('endDate' + '}'), request.end_date if request.end_date is not None else '')
        else:
            if request.end_date is not None:
                query_params.append((self.__downcase_first_letter('endDate'), request.end_date))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TimephasedDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_resources(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s resources.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: ResourceItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_resources_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_resources_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_resources_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_resources_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_resources_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s resources.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_resources_request object with parameters
        :return: ResourceItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_resources`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/resources'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceItemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_resource(self, request, **kwargs):  # noqa: E501
        """Add a new resource to a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param resource_name str : The name of the new resource. The default value is an empty string
        :param before_resource_id int : The id of the resource to insert the new resource before. The default value is the id of the last resource in a project file.
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: ResourceItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_resource_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_resource_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_resource_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_resource_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_resource_with_http_info(self, request, **kwargs):  # noqa: E501
        """Add a new resource to a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_resource_request object with parameters
        :return: ResourceItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_resource`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/resources'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('resourceName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('resourceName' + '}'), request.resource_name if request.resource_name is not None else '')
        else:
            if request.resource_name is not None:
                query_params.append((self.__downcase_first_letter('resourceName'), request.resource_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('beforeResourceId') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('beforeResourceId' + '}'), request.before_resource_id if request.before_resource_id is not None else '')
        else:
            if request.before_resource_id is not None:
                query_params.append((self.__downcase_first_letter('beforeResourceId'), request.before_resource_id))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_resource(self, request, **kwargs):  # noqa: E501
        """Updates resource with the specified Uid  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The file name (required)
        :param resource_uid int : The Uid of a resource (required)
        :param resource Resource : The representation of the modified resource (required)
        :param mode str : The calculation mode of a project
        :param recalculate bool : Specifies whether the project's recalculation should be performed
        :param storage str : The document storage
        :param folder str : The document storage
        :param file_name str : The filename to save Changes
        :return: ResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_resource_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_resource_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_resource_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_resource_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_resource_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates resource with the specified Uid  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_resource_request object with parameters
        :return: ResourceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_resource" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_resource`")  # noqa: E501
        # verify the required parameter 'resource_uid' is set
        if request.resource_uid is None:
            raise ValueError("Missing the required parameter `resource_uid` when calling `put_resource`")  # noqa: E501
        # verify the required parameter 'resource' is set
        if request.resource is None:
            raise ValueError("Missing the required parameter `resource` when calling `put_resource`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/resources/{resourceUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.resource_uid is not None:
            path_params[self.__downcase_first_letter('resourceUid')] = request.resource_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('mode') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('mode' + '}'), request.mode if request.mode is not None else '')
        else:
            if request.mode is not None:
                query_params.append((self.__downcase_first_letter('mode'), request.mode))  # noqa: E501
        if '{' + self.__downcase_first_letter('recalculate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('recalculate' + '}'), request.recalculate if request.recalculate is not None else '')
        else:
            if request.recalculate is not None:
                query_params.append((self.__downcase_first_letter('recalculate'), request.recalculate))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.resource is not None:
            body_params = request.resource
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def clear_leveling(self, request, **kwargs):  # noqa: E501
        """Clears leveling delays that was previously added to the project during resource leveling.  If request body is empty, all leveling delays will be cleared.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file (required)
        :param task_uids list[int] : The array containing task uids              for which leveling delay should be cleared.              If not specified, all leveling delays will be cleared. 
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :param folder str : The folder storage
        :param storage str : The document storage.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.clear_leveling_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.clear_leveling_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.clear_leveling_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.clear_leveling_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def clear_leveling_with_http_info(self, request, **kwargs):  # noqa: E501
        """Clears leveling delays that was previously added to the project during resource leveling.  If request body is empty, all leveling delays will be cleared.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request clear_leveling_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clear_leveling" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `clear_leveling`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/resourceLevel'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.task_uids is not None:
            body_params = request.task_uids
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def level_tasks(self, request, **kwargs):  # noqa: E501
        """Levels tasks for project’s resources. If request body is empty,  all project&#39;s resources with default leveling options will be leveled.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file (required)
        :param options LevelingOptions : Options which specifies how to level resources.              If not specified, default leveling options will be used. 
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :param folder str : The folder storage
        :param storage str : The document storage.
        :return: LevelingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.level_tasks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.level_tasks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.level_tasks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.level_tasks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def level_tasks_with_http_info(self, request, **kwargs):  # noqa: E501
        """Levels tasks for project’s resources. If request body is empty,  all project&#39;s resources with default leveling options will be leveled.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request level_tasks_request object with parameters
        :return: LevelingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method level_tasks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `level_tasks`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/resourceLevel'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.options is not None:
            body_params = request.options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LevelingResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def get_risk_analysis_report(self, request, **kwargs):  # noqa: E501
        """Performs a risk analysys using Monte Carlo simulation and creates a risk analysis report.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : The uid of the task for which this risk will be applied in Monte Carlo simulation. (required)
        :param distribution_type str : Gets or sets the probability distribution used in Monte Carlo simulation. The default value is ProbabilityDistributionType.Normal.
        :param optimistic int : The percentage of the most likely task duration which can happen in the best possible project scenario. The default value is 75, which means that if the estimated specified task duration is 4 days then the optimistic duration will be 3 days.
        :param pessimistic int : The percentage of the most likely task duration which can happen in the worst possible project scenario. The default value is 125, which means that if the estimated specified task duration is 4 days then the pessimistic duration will be 5 days.
        :param confidence_level str : Gets or sets the confidence level that correspond to the percentage of the time the actual generated values will be within optimistic and pessimistic estimates. The default value is CL99.
        :param iterations int : The number of iterations to use in Monte Carlo simulation. The default value is 100.
        :param storage str : The document storage.
        :param folder str : The folder storage.
        :param file_name str : The resulting report fileName.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_risk_analysis_report_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_risk_analysis_report_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_risk_analysis_report_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_risk_analysis_report_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_risk_analysis_report_with_http_info(self, request, **kwargs):  # noqa: E501
        """Performs a risk analysys using Monte Carlo simulation and creates a risk analysis report.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_risk_analysis_report_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_risk_analysis_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_risk_analysis_report`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `get_risk_analysis_report`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/riskAnalysisReport'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('taskUid') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('taskUid' + '}'), request.task_uid if request.task_uid is not None else '')
        else:
            if request.task_uid is not None:
                query_params.append((self.__downcase_first_letter('taskUid'), request.task_uid))  # noqa: E501
        if '{' + self.__downcase_first_letter('distributionType') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('distributionType' + '}'), request.distribution_type if request.distribution_type is not None else '')
        else:
            if request.distribution_type is not None:
                query_params.append((self.__downcase_first_letter('distributionType'), request.distribution_type))  # noqa: E501
        if '{' + self.__downcase_first_letter('optimistic') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('optimistic' + '}'), request.optimistic if request.optimistic is not None else '')
        else:
            if request.optimistic is not None:
                query_params.append((self.__downcase_first_letter('optimistic'), request.optimistic))  # noqa: E501
        if '{' + self.__downcase_first_letter('pessimistic') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('pessimistic' + '}'), request.pessimistic if request.pessimistic is not None else '')
        else:
            if request.pessimistic is not None:
                query_params.append((self.__downcase_first_letter('pessimistic'), request.pessimistic))  # noqa: E501
        if '{' + self.__downcase_first_letter('confidenceLevel') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('confidenceLevel' + '}'), request.confidence_level if request.confidence_level is not None else '')
        else:
            if request.confidence_level is not None:
                query_params.append((self.__downcase_first_letter('confidenceLevel'), request.confidence_level))  # noqa: E501
        if '{' + self.__downcase_first_letter('iterations') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('iterations' + '}'), request.iterations if request.iterations is not None else '')
        else:
            if request.iterations is not None:
                query_params.append((self.__downcase_first_letter('iterations'), request.iterations))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def delete_task(self, request, **kwargs):  # noqa: E501
        """Deletes a project task with all references to it and rebuilds tasks tree.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : Task Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :param file_name str : The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_task_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_task_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_task_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_task_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_task_with_http_info(self, request, **kwargs):  # noqa: E501
        """Deletes a project task with all references to it and rebuilds tasks tree.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_task_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_task`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `delete_task`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/{taskUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.task_uid is not None:
            path_params[self.__downcase_first_letter('taskUid')] = request.task_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_primavera_task_properties(self, request, **kwargs):  # noqa: E501
        """Get primavera properties for a task with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : Uid of task to get primavera properties for. (required)
        :param folder str : The document folder.
        :param storage str : The document storage.
        :return: PrimaveraTaskPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_primavera_task_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_primavera_task_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_primavera_task_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_primavera_task_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_primavera_task_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get primavera properties for a task with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_primavera_task_properties_request object with parameters
        :return: PrimaveraTaskPropertiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_primavera_task_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_primavera_task_properties`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `get_primavera_task_properties`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/{taskUid}/primaveraProperties'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.task_uid is not None:
            path_params[self.__downcase_first_letter('taskUid')] = request.task_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PrimaveraTaskPropertiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_task(self, request, **kwargs):  # noqa: E501
        """Read project task.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : Task Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: TaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_task_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_task_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_task_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read project task.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_task_request object with parameters
        :return: TaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_task`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `get_task`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/{taskUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.task_uid is not None:
            path_params[self.__downcase_first_letter('taskUid')] = request.task_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_task_assignments(self, request, **kwargs):  # noqa: E501
        """Get task assignments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : Task Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AssignmentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_task_assignments_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_assignments_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_task_assignments_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_assignments_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_task_assignments_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get task assignments.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_task_assignments_request object with parameters
        :return: AssignmentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task_assignments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_task_assignments`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `get_task_assignments`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/{taskUid}/assignments'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.task_uid is not None:
            path_params[self.__downcase_first_letter('taskUid')] = request.task_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssignmentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_task_recurring_info(self, request, **kwargs):  # noqa: E501
        """Get recurring info for a task with the specified Uid  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : Task Uid (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: RecurringInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_task_recurring_info_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get recurring info for a task with the specified Uid  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_task_recurring_info_request object with parameters
        :return: RecurringInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task_recurring_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_task_recurring_info`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `get_task_recurring_info`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/{taskUid}/recurringInfo'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.task_uid is not None:
            path_params[self.__downcase_first_letter('taskUid')] = request.task_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecurringInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_task_timephased_data(self, request, **kwargs):  # noqa: E501
        """Get timescaled data for a task with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : Uid of task to get timephased data for. (required)
        :param type str : Type of timephased data to get.
        :param start_date datetime : Start date.
        :param end_date datetime : End date.
        :param folder str : The document folder.
        :param storage str : The document storage.
        :return: TimephasedDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_task_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_task_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_timephased_data_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_task_timephased_data_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get timescaled data for a task with the specified Uid.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_task_timephased_data_request object with parameters
        :return: TimephasedDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task_timephased_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_task_timephased_data`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `get_task_timephased_data`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/{taskUid}/timeScaleData'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.task_uid is not None:
            path_params[self.__downcase_first_letter('taskUid')] = request.task_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('type') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('type' + '}'), request.type if request.type is not None else '')
        else:
            if request.type is not None:
                query_params.append((self.__downcase_first_letter('type'), request.type))  # noqa: E501
        if '{' + self.__downcase_first_letter('startDate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('startDate' + '}'), request.start_date if request.start_date is not None else '')
        else:
            if request.start_date is not None:
                query_params.append((self.__downcase_first_letter('startDate'), request.start_date))  # noqa: E501
        if '{' + self.__downcase_first_letter('endDate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('endDate' + '}'), request.end_date if request.end_date is not None else '')
        else:
            if request.end_date is not None:
                query_params.append((self.__downcase_first_letter('endDate'), request.end_date))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TimephasedDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tasks(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s tasks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: TaskItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_tasks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_tasks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_tasks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_tasks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_tasks_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s tasks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_tasks_request object with parameters
        :return: TaskItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tasks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_tasks`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskItemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_task(self, request, **kwargs):  # noqa: E501
        """Add a new task to a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_name str : The name of the new task. The default value is an empty string
        :param before_task_id int : The id of the task to insert the new task before.              The default value is the id of the last task in a project file.
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: TaskItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_task_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_task_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_task_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_task_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_task_with_http_info(self, request, **kwargs):  # noqa: E501
        """Add a new task to a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_task_request object with parameters
        :return: TaskItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_task`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('taskName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('taskName' + '}'), request.task_name if request.task_name is not None else '')
        else:
            if request.task_name is not None:
                query_params.append((self.__downcase_first_letter('taskName'), request.task_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('beforeTaskId') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('beforeTaskId' + '}'), request.before_task_id if request.before_task_id is not None else '')
        else:
            if request.before_task_id is not None:
                query_params.append((self.__downcase_first_letter('beforeTaskId'), request.before_task_id))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_task_recurring_info(self, request, **kwargs):  # noqa: E501
        """Adds a new recurring task.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param parent_task_uid int : The Uid of parent task for the created recurring task (required)
        :param task_name str : Name of the task to create. (required)
        :param recurring_info RecurringInfo : DTO which defines task's recurring info. (required)
        :param calendar_name str : Name of the project's calendar to use for recurring task's scheduling. (required)
        :param file_name str : File name to save changes to.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: TaskItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_task_recurring_info_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds a new recurring task.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_task_recurring_info_request object with parameters
        :return: TaskItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_task_recurring_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_task_recurring_info`")  # noqa: E501
        # verify the required parameter 'parent_task_uid' is set
        if request.parent_task_uid is None:
            raise ValueError("Missing the required parameter `parent_task_uid` when calling `post_task_recurring_info`")  # noqa: E501
        # verify the required parameter 'task_name' is set
        if request.task_name is None:
            raise ValueError("Missing the required parameter `task_name` when calling `post_task_recurring_info`")  # noqa: E501
        # verify the required parameter 'recurring_info' is set
        if request.recurring_info is None:
            raise ValueError("Missing the required parameter `recurring_info` when calling `post_task_recurring_info`")  # noqa: E501
        # verify the required parameter 'calendar_name' is set
        if request.calendar_name is None:
            raise ValueError("Missing the required parameter `calendar_name` when calling `post_task_recurring_info`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/recurringInfo'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('parentTaskUid') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('parentTaskUid' + '}'), request.parent_task_uid if request.parent_task_uid is not None else '')
        else:
            if request.parent_task_uid is not None:
                query_params.append((self.__downcase_first_letter('parentTaskUid'), request.parent_task_uid))  # noqa: E501
        if '{' + self.__downcase_first_letter('taskName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('taskName' + '}'), request.task_name if request.task_name is not None else '')
        else:
            if request.task_name is not None:
                query_params.append((self.__downcase_first_letter('taskName'), request.task_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('calendarName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('calendarName' + '}'), request.calendar_name if request.calendar_name is not None else '')
        else:
            if request.calendar_name is not None:
                query_params.append((self.__downcase_first_letter('calendarName'), request.calendar_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.recurring_info is not None:
            body_params = request.recurring_info
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskItemResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_tasks(self, request, **kwargs):  # noqa: E501
        """Create multiple tasks by single request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param requests list[TaskCreationRequest] : Requests to create tasks. (required)
        :param file_name str : The name of the project document to save changes to.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: TaskItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_tasks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_tasks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_tasks_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_tasks_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_tasks_with_http_info(self, request, **kwargs):  # noqa: E501
        """Create multiple tasks by single request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_tasks_request object with parameters
        :return: TaskItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_tasks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_tasks`")  # noqa: E501
        # verify the required parameter 'requests' is set
        if request.requests is None:
            raise ValueError("Missing the required parameter `requests` when calling `post_tasks`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/batch'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.requests is not None:
            body_params = request.requests
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskItemsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_move_task(self, request, **kwargs):  # noqa: E501
        """Move one task to another parent task.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : Unique id of the task to be moved. (required)
        :param parent_task_uid int : Unique id of the new parent task. (required)
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. 
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_move_task_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_move_task_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_move_task_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_move_task_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_move_task_with_http_info(self, request, **kwargs):  # noqa: E501
        """Move one task to another parent task.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_move_task_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_move_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_move_task`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `put_move_task`")  # noqa: E501
        # verify the required parameter 'parent_task_uid' is set
        if request.parent_task_uid is None:
            raise ValueError("Missing the required parameter `parent_task_uid` when calling `put_move_task`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/{taskUid}/move'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.task_uid is not None:
            path_params[self.__downcase_first_letter('taskUid')] = request.task_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('parentTaskUid') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('parentTaskUid' + '}'), request.parent_task_uid if request.parent_task_uid is not None else '')
        else:
            if request.parent_task_uid is not None:
                query_params.append((self.__downcase_first_letter('parentTaskUid'), request.parent_task_uid))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_move_task_to_sibling(self, request, **kwargs):  # noqa: E501
        """Move a task to another position under the same parent and the same outline level  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : Task Unique Id. (required)
        :param before_task_uid int : Unique Id of the task after which the current task will be placed. (required)
        :param file_name str : The name of the project document to save changes to.             If this parameter is omitted then the changes will be saved to the source project document.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_move_task_to_sibling_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_move_task_to_sibling_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_move_task_to_sibling_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_move_task_to_sibling_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_move_task_to_sibling_with_http_info(self, request, **kwargs):  # noqa: E501
        """Move a task to another position under the same parent and the same outline level  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_move_task_to_sibling_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_move_task_to_sibling" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_move_task_to_sibling`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `put_move_task_to_sibling`")  # noqa: E501
        # verify the required parameter 'before_task_uid' is set
        if request.before_task_uid is None:
            raise ValueError("Missing the required parameter `before_task_uid` when calling `put_move_task_to_sibling`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/{taskUid}/moveToSibling'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.task_uid is not None:
            path_params[self.__downcase_first_letter('taskUid')] = request.task_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('beforeTaskUid') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('beforeTaskUid' + '}'), request.before_task_uid if request.before_task_uid is not None else '')
        else:
            if request.before_task_uid is not None:
                query_params.append((self.__downcase_first_letter('beforeTaskUid'), request.before_task_uid))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_task(self, request, **kwargs):  # noqa: E501
        """Updates special task getting by task UID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : Task UID (required)
        :param task Task : TaskDTO (required)
        :param mode str : CalculationModeDTO
        :param recalculate bool : boolean value 
        :param storage str : The document strorage
        :param folder str : The document folder
        :param file_name str : The name of the file to save changes
        :return: TaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_task_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_task_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_task_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_task_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_task_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates special task getting by task UID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_task_request object with parameters
        :return: TaskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_task`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `put_task`")  # noqa: E501
        # verify the required parameter 'task' is set
        if request.task is None:
            raise ValueError("Missing the required parameter `task` when calling `put_task`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/{taskUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.task_uid is not None:
            path_params[self.__downcase_first_letter('taskUid')] = request.task_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('mode') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('mode' + '}'), request.mode if request.mode is not None else '')
        else:
            if request.mode is not None:
                query_params.append((self.__downcase_first_letter('mode'), request.mode))  # noqa: E501
        if '{' + self.__downcase_first_letter('recalculate') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('recalculate' + '}'), request.recalculate if request.recalculate is not None else '')
        else:
            if request.recalculate is not None:
                query_params.append((self.__downcase_first_letter('recalculate'), request.recalculate))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.task is not None:
            body_params = request.task
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_task_recurring_info(self, request, **kwargs):  # noqa: E501
        """Updates existing task&#39;s recurring info. Note that task should be already recurring.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uid int : Task Uid. (required)
        :param recurring_info RecurringInfo : A modified DTO of task's recurring info. (required)
        :param file_name str : File name to save changes to.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_task_recurring_info_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_task_recurring_info_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates existing task&#39;s recurring info. Note that task should be already recurring.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_task_recurring_info_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_task_recurring_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_task_recurring_info`")  # noqa: E501
        # verify the required parameter 'task_uid' is set
        if request.task_uid is None:
            raise ValueError("Missing the required parameter `task_uid` when calling `put_task_recurring_info`")  # noqa: E501
        # verify the required parameter 'recurring_info' is set
        if request.recurring_info is None:
            raise ValueError("Missing the required parameter `recurring_info` when calling `put_task_recurring_info`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/tasks/{taskUid}/recurringInfo'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.task_uid is not None:
            path_params[self.__downcase_first_letter('taskUid')] = request.task_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.recurring_info is not None:
            body_params = request.recurring_info
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def delete_task_link(self, request, **kwargs):  # noqa: E501
        """Delete task link.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param index int : Index of the task link object. See TaskLink.Index property. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :param file_name str : The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_task_link_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_task_link_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_task_link_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_task_link_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_task_link_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete task link.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_task_link_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_task_link" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_task_link`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `delete_task_link`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/taskLinks/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('index')] = request.index  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_task_links(self, request, **kwargs):  # noqa: E501
        """Get tasks&#39; links of a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: TaskLinksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_task_links_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_links_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_task_links_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_task_links_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_task_links_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get tasks&#39; links of a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_task_links_request object with parameters
        :return: TaskLinksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task_links" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_task_links`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/taskLinks'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskLinksResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_task_link(self, request, **kwargs):  # noqa: E501
        """Adds a new task link to a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_link TaskLink : The TaskLink object representation that should be added. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :param file_name str : The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_task_link_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_task_link_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_task_link_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_task_link_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_task_link_with_http_info(self, request, **kwargs):  # noqa: E501
        """Adds a new task link to a project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_task_link_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_task_link" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_task_link`")  # noqa: E501
        # verify the required parameter 'task_link' is set
        if request.task_link is None:
            raise ValueError("Missing the required parameter `task_link` when calling `post_task_link`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/taskLinks'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.task_link is not None:
            body_params = request.task_link
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_task_link(self, request, **kwargs):  # noqa: E501
        """Updates existing task link.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param index int : Index of the task link object. See TaskLink.Index property. (required)
        :param task_link TaskLink : The representation of the modified TaskLink object. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :param file_name str : The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document.
        :return: TaskLinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_task_link_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_task_link_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_task_link_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_task_link_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_task_link_with_http_info(self, request, **kwargs):  # noqa: E501
        """Updates existing task link.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_task_link_request object with parameters
        :return: TaskLinkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_task_link" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_task_link`")  # noqa: E501
        # verify the required parameter 'index' is set
        if request.index is None:
            raise ValueError("Missing the required parameter `index` when calling `put_task_link`")  # noqa: E501
        # verify the required parameter 'task_link' is set
        if request.task_link is None:
            raise ValueError("Missing the required parameter `task_link` when calling `put_task_link`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/taskLinks/{index}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.index is not None:
            path_params[self.__downcase_first_letter('index')] = request.index  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.task_link is not None:
            body_params = request.task_link
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskLinkResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def get_vba_project(self, request, **kwargs):  # noqa: E501
        """Returns VBA project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file (required)
        :param folder str : The folder storage
        :param storage str : The document storage.
        :return: VbaProjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_vba_project_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_vba_project_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_vba_project_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_vba_project_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_vba_project_with_http_info(self, request, **kwargs):  # noqa: E501
        """Returns VBA project.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_vba_project_request object with parameters
        :return: VbaProjectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_vba_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_vba_project`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/vbaproject'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VbaProjectResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def create_table_text_style(self, request, **kwargs):  # noqa: E501
        """Create table text style in specified view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param view_uid int : Uid of the view. (required)
        :param table_text_style TableTextStyle : A DTO of TableTextStyle to create (required)
        :param file_name str : File name to save changes to.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.create_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.create_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.create_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def create_table_text_style_with_http_info(self, request, **kwargs):  # noqa: E501
        """Create table text style in specified view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request create_table_text_style_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_table_text_style" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `create_table_text_style`")  # noqa: E501
        # verify the required parameter 'view_uid' is set
        if request.view_uid is None:
            raise ValueError("Missing the required parameter `view_uid` when calling `create_table_text_style`")  # noqa: E501
        # verify the required parameter 'table_text_style' is set
        if request.table_text_style is None:
            raise ValueError("Missing the required parameter `table_text_style` when calling `create_table_text_style`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/views/{viewUid}/tabletextstyles'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.view_uid is not None:
            path_params[self.__downcase_first_letter('viewUid')] = request.view_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.table_text_style is not None:
            body_params = request.table_text_style
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_table_text_style(self, request, **kwargs):  # noqa: E501
        """Delete specified table text style from specified view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param view_uid int : Uid of the view. (required)
        :param row_uid int : Uid of the row. (required)
        :param field str : Specifies exact field of the row
        :param file_name str : File name to save changes to.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.delete_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.delete_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.delete_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def delete_table_text_style_with_http_info(self, request, **kwargs):  # noqa: E501
        """Delete specified table text style from specified view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request delete_table_text_style_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_table_text_style" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `delete_table_text_style`")  # noqa: E501
        # verify the required parameter 'view_uid' is set
        if request.view_uid is None:
            raise ValueError("Missing the required parameter `view_uid` when calling `delete_table_text_style`")  # noqa: E501
        # verify the required parameter 'row_uid' is set
        if request.row_uid is None:
            raise ValueError("Missing the required parameter `row_uid` when calling `delete_table_text_style`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/views/{viewUid}/tabletextstyles/{rowUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.view_uid is not None:
            path_params[self.__downcase_first_letter('viewUid')] = request.view_uid  # noqa: E501
        if request.row_uid is not None:
            path_params[self.__downcase_first_letter('rowUid')] = request.row_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('field') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('field' + '}'), request.field if request.field is not None else '')
        else:
            if request.field is not None:
                query_params.append((self.__downcase_first_letter('field'), request.field))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_table_text_styles(self, request, **kwargs):  # noqa: E501
        """Read all table text styles from specified view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param view_uid int : Uid of the view. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: TableTextStylesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_all_table_text_styles_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_all_table_text_styles_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_all_table_text_styles_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_all_table_text_styles_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_all_table_text_styles_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read all table text styles from specified view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_all_table_text_styles_request object with parameters
        :return: TableTextStylesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_table_text_styles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_all_table_text_styles`")  # noqa: E501
        # verify the required parameter 'view_uid' is set
        if request.view_uid is None:
            raise ValueError("Missing the required parameter `view_uid` when calling `get_all_table_text_styles`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/views/{viewUid}/tabletextstyles'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.view_uid is not None:
            path_params[self.__downcase_first_letter('viewUid')] = request.view_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableTextStylesResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_table_text_style(self, request, **kwargs):  # noqa: E501
        """Read specified table text style from specified view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param view_uid int : Uid of the view. (required)
        :param row_uid int : Uid of the row. (required)
        :param field str : Specifies exact field of the row
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: TableTextStyleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_table_text_style_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read specified table text style from specified view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_table_text_style_request object with parameters
        :return: TableTextStyleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_table_text_style" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_table_text_style`")  # noqa: E501
        # verify the required parameter 'view_uid' is set
        if request.view_uid is None:
            raise ValueError("Missing the required parameter `view_uid` when calling `get_table_text_style`")  # noqa: E501
        # verify the required parameter 'row_uid' is set
        if request.row_uid is None:
            raise ValueError("Missing the required parameter `row_uid` when calling `get_table_text_style`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/views/{viewUid}/tabletextstyles/{rowUid}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.view_uid is not None:
            path_params[self.__downcase_first_letter('viewUid')] = request.view_uid  # noqa: E501
        if request.row_uid is not None:
            path_params[self.__downcase_first_letter('rowUid')] = request.row_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('field') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('field' + '}'), request.field if request.field is not None else '')
        else:
            if request.field is not None:
                query_params.append((self.__downcase_first_letter('field'), request.field))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TableTextStyleResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_views(self, request, **kwargs):  # noqa: E501
        """Read all project views.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: ViewsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_views_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_views_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_views_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_views_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_views_with_http_info(self, request, **kwargs):  # noqa: E501
        """Read all project views.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_views_request object with parameters
        :return: ViewsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_views" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_views`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/views'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ViewsResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_table_text_style(self, request, **kwargs):  # noqa: E501
        """Update table text style in specified view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param view_uid int : Uid of the view. (required)
        :param table_text_style TableTextStyle : A DTO of TableTextStyle to update (required)
        :param file_name str : File name to save changes to.
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.update_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.update_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.update_table_text_style_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def update_table_text_style_with_http_info(self, request, **kwargs):  # noqa: E501
        """Update table text style in specified view.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request update_table_text_style_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_table_text_style" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `update_table_text_style`")  # noqa: E501
        # verify the required parameter 'view_uid' is set
        if request.view_uid is None:
            raise ValueError("Missing the required parameter `view_uid` when calling `update_table_text_style`")  # noqa: E501
        # verify the required parameter 'table_text_style' is set
        if request.table_text_style is None:
            raise ValueError("Missing the required parameter `table_text_style` when calling `update_table_text_style`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/views/{viewUid}/tabletextstyles'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.view_uid is not None:
            path_params[self.__downcase_first_letter('viewUid')] = request.view_uid  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.table_text_style is not None:
            body_params = request.table_text_style
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    def get_wbs_definition(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s WBS Definition.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param storage str : The document storage.
        :param folder str : The document folder.
        :return: WBSDefinitionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_wbs_definition_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_wbs_definition_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_wbs_definition_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_wbs_definition_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_wbs_definition_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a project&#39;s WBS Definition.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request get_wbs_definition_request object with parameters
        :return: WBSDefinitionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wbs_definition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_wbs_definition`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/wbsDefinition'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WBSDefinitionResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_renumber_wbs_code(self, request, **kwargs):  # noqa: E501
        """Renumber WBS code of passed tasks (if specified) or all project&#39;s tasks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : The name of the file. (required)
        :param task_uids list[int] : Uids of task for WBS codes renumbering. If not specified, WBS codes for all tasks will be renumbered. (required)
        :param storage str : The document storage.
        :param file_name str : The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.
        :param folder str : The document folder.
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_renumber_wbs_code_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_renumber_wbs_code_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_renumber_wbs_code_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_renumber_wbs_code_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_renumber_wbs_code_with_http_info(self, request, **kwargs):  # noqa: E501
        """Renumber WBS code of passed tasks (if specified) or all project&#39;s tasks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request put_renumber_wbs_code_request object with parameters
        :return: AsposeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_renumber_wbs_code" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `put_renumber_wbs_code`")  # noqa: E501
        # verify the required parameter 'task_uids' is set
        if request.task_uids is None:
            raise ValueError("Missing the required parameter `task_uids` when calling `put_renumber_wbs_code`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/renumberWbsCode'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('fileName') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('fileName' + '}'), request.file_name if request.file_name is not None else '')
        else:
            if request.file_name is not None:
                query_params.append((self.__downcase_first_letter('fileName'), request.file_name))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.task_uids is not None:
            body_params = request.task_uids
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AsposeResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_task_document_with_format(self, request, **kwargs):  # noqa: E501
        """Get a project document in the specified format and with the specified save options.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request contains request parameters.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_task_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_task_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_task_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_task_document_with_format_with_http_info(request, **kwargs)  # noqa: E501
            return data

    def post_task_document_with_format_with_http_info(self, request, **kwargs):  # noqa: E501
        """Get a project document in the specified format and with the specified save options.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request post_task_document_with_format_request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_task_document_with_format" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_task_document_with_format`")  # noqa: E501
        # verify the required parameter 'format' is set
        if request.format is None:
            raise ValueError("Missing the required parameter `format` when calling `post_task_document_with_format`")  # noqa: E501
        # verify the required parameter 'save_options' is set
        if request.save_options is None:
            raise ValueError("Missing the required parameter `save_options` when calling `post_task_document_with_format`")  # noqa: E501

        collection_formats = {}
        path = '/tasks/{name}/format'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if '{' + self.__downcase_first_letter('format') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('format' + '}'), request.format if request.format is not None else '')
        else:
            if request.format is not None:
                query_params.append((self.__downcase_first_letter('format'), request.format))  # noqa: E501
        if '{' + self.__downcase_first_letter('returnAsZipArchive') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('returnAsZipArchive' + '}'), request.return_as_zip_archive if request.return_as_zip_archive is not None else '')
        else:
            if request.return_as_zip_archive is not None:
                query_params.append((self.__downcase_first_letter('returnAsZipArchive'), request.return_as_zip_archive))  # noqa: E501
        if '{' + self.__downcase_first_letter('storage') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501
        if '{' + self.__downcase_first_letter('folder') + '}' in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.save_options is not None:
            body_params = request.save_options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWT']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
        
