![](https://img.shields.io/badge/api-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/aspose-tasks-cloud) ![PyPI - Format](https://img.shields.io/pypi/format/aspose-tasks-cloud) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aspose-tasks-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aspose-tasks-cloud) [![GitHub license](https://img.shields.io/github/license/aspose-tasks-cloud/aspose-tasks-cloud-php)](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-php/blob/master/LICENSE) ![GitHub last commit](https://img.shields.io/github/last-commit/Aspose-tasks-Cloud/aspose-tasks-cloud-php)

# Python SDK to Manage Tasks in the Cloud

Aspose.Tasks for Cloud offers the ability to manipulate and convert Microsoft Project MPT, MPP, MPX & Oracle Primavera XER, XML, and PrimaveraP6XML files in the Cloud. [Aspose.Tasks Cloud SDK for Python](https://products.aspose.cloud/tasks/python) wraps the REST API to make it easier for Python developers to integrate Task Management features in their own applications.

## REST API for Task Management

* [Convert Microsoft Project & Oracle Primavera files](https://docs.aspose.cloud/tasks/convert-project-document-to-the-specified-format/) to other formats including MPP to PDF conversion.
* Read, change and write Microsoft Project documents.
* Create, update and write projects in XML project format.
* Manage extended attributes.
* [Define weekdays for calendars](https://docs.aspose.cloud/tasks/working-with-calendars/) and calendar exceptions.
* [Manage tasks](https://docs.aspose.cloud/tasks/working-with-tasks/), baseline scheduling and duration.
* Create and [manage task links](https://docs.aspose.cloud/tasks/working-with-task-links/).
* Manage resources costs and variances.
* Access assignment costs and budget.

## Read & Write Project Data

**Microsoft Project** MPP, XML, MPT **Primavera** MPX

## Save Project Data As

XER, XLSX, HTML, XML, TXT, TIF, SVG, PNG, JPEG

## Get Started with Aspose.Tasks Cloud SDK for Python

Register an account at [Aspose Cloud Dashboard](https://dashboard.aspose.cloud/#/apps) to get you application information. Next, either directly use the source from this repository in your project or get the package from [PyPi](https://pypi.org/project/aspose-tasks-cloud).

### Install via PIP

```sh
pip install aspose-tasks-cloud
```

You may need to run `pip` command with root permission as `sudo pip install aspose-tasks-cloud`.

Then import the package as follows.

```python
import asposetaskscloud
```

### Install via Setuptools

```sh
python setup.py install --user
```

Alternatively, execute `sudo python setup.py install` to install the package for all users.

Then import the package as follows.

```python
import asposetaskscloud
```

## Extract MPP Document Properties via Python

```python
import asposetaskscloud
import asposetaskscloud.models.requests
api_client = asposetaskscloud.ApiClient()
api_client.configuration.host = 'https://api.aspose.cloud'
api_client.configuration.api_key['api_key'] = '' # Put your appKey here
api_client.configuration.api_key['app_sid'] = '' # Put your appSid here
tasks_api = asposetaskscloud.TasksApi(api_client)
remote_name = 'SomeSeriousPlan.mpp'

upload_request = asposetaskscloud.models.requests.UploadFileRequest(file, remote_name)
upload_result = self.tasks_api.upload_file(request)
self.assertTrue(upload_result.code == 200, 'Error has occurred while uploading project file')

request = asposetaskscloud.models.requests.GetDocumentPropertiesRequest(remote_name)
result = tasks_api.get_document_properties(request)
self.assertTrue(result.code == 200, 'Error has occurred while getting document properties')
```

## Aspose.Tasks Cloud SDKs in Popular Languages

| .NET | PHP | Python | Node.js |
|---|---|---|---|
| [GitHub](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-dotnet) | [GitHub](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-php) | [GitHub](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-python) | [GitHub](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-node)  | 
| [NuGet](https://www.nuget.org/packages/Aspose.Tasks-Cloud/) | [Composer](https://packagist.org/packages/aspose/tasks-sdk-php) | [PIP](https://pypi.org/project/aspose-tasks-cloud/) | [NPM](https://www.npmjs.com/package/@asposecloud/aspose-tasks-cloud)  |

[Home](https://www.aspose.cloud) | [Product Page](https://products.aspose.cloud/tasks/python) | [Documentation](https://docs.aspose.cloud/tasks/) | [Live Demo](https://products.aspose.app/tasks/family) |  [API Reference](https://apireference.aspose.cloud/tasks/) | [Code Samples](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-python/tree/master/test) | [Blog](https://blog.aspose.cloud/category/tasks/) | [Free Support](https://forum.aspose.cloud/c/tasks) | [Free Trial](https://dashboard.aspose.cloud/#/apps)
