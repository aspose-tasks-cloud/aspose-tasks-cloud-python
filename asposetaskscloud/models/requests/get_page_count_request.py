# coding: utf-8
# --------------------------------------------------------------------------------
# <copyright company="Aspose" file="get_page_count_request.py">
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
# --------------------------------------------------------------------------------


class GetPageCountRequest(object):
    """
    Request model for get_page_count operation.
    Initializes a new instance.
    :param name The name of the file.
    :param page_size PageSize to get page count for.
    :param presentation_format PresentationFormat to get page count for.
    :param timescale Timescale to get page count for.
    :param start_date Start date to get page count for.
    :param end_date End date to get page count for.
    :param folder The document folder
    :param storage The document storage.
    """

    def __init__(self, name, page_size=None, presentation_format=None, timescale=None, start_date=None, end_date=None, folder=None, storage=None):
        self.name = name
        self.page_size = page_size
        self.presentation_format = presentation_format
        self.timescale = timescale
        self.start_date = start_date
        self.end_date = end_date
        self.folder = folder
        self.storage = storage


