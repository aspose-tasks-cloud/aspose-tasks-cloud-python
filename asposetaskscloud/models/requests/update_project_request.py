# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="update_project_request.py">
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
# coding: utf-8
# --------------------------------------------------------------------------------


class UpdateProjectRequest(object):
    """
    Request model for update_project operation.
    Initializes a new instance.
    :param name The name of the file.
    :param site_url The URL of PWA (Project Web Access) API of Project Online.
    :param user_name The user name for the sharepoint site.
    :param save_options Dispensable save options for Project Server\\Project Online.
    :param folder The document folder.
    :param storage The document storage.
    :param x_project_online_token Authorization token for the SharePoint. For example, in c# it can be retrieved using SharePointOnlineCredentials class from Microsoft.SharePoint.Client.Runtime assembly
    :param x_sharepoint_password The password for the SharePoint site.
    """

    def __init__(self, name, site_url, user_name=None, save_options=None, folder=None, storage=None, x_project_online_token=None, x_sharepoint_password=None):
        self.name = name
        self.site_url = site_url
        self.user_name = user_name
        self.save_options = save_options
        self.folder = folder
        self.storage = storage
        self.x_project_online_token = x_project_online_token
        self.x_sharepoint_password = x_sharepoint_password



