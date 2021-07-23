![](https://img.shields.io/badge/api-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/aspose-tasks-cloud) ![PyPI - Format](https://img.shields.io/pypi/format/aspose-tasks-cloud) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aspose-tasks-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aspose-tasks-cloud) [![GitHub license](https://img.shields.io/github/license/aspose-tasks-cloud/aspose-tasks-cloud-python)](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-php/blob/master/LICENSE) ![GitHub last commit](https://img.shields.io/github/last-commit/Aspose-tasks-Cloud/aspose-tasks-cloud-python)

# Manipulate MS Project Files in Python via Cloud REST API

Aspose.Tasks for Cloud offers the ability to manipulate and convert Microsoft Project MPT, MPP, MPX & Oracle Primavera XER, XML, and PrimaveraP6XML files in Python. [Aspose.Tasks Cloud SDK for Python](https://products.aspose.cloud/tasks/python) wraps the REST API to make it easier for the developers to integrate MS Project Task Management features in their own cloud-based Python applications on Linux, MacOS, Windows or Android.

Feel free to explore the [Developer's Guide](https://docs.aspose.cloud/display/taskscloud/Developer+Guide) & [API Reference](https://apireference.aspose.cloud/tasks/) to know all about Aspose.Tasks Cloud API.

## MS Project Processing Features
- Add project assignments or delete project assignments along with their references.
- Get the project's outline codes by index & get links to all project tasks.
- Import projects from Primavera DB formats or from databases with the specified connection string.
- Get UIDs of all projects contained in the file & fetch the required assignment with the project based on UID.
- Manage project tasks, resource data, calendars & Work Breakdown Structure (WBS).
- Perform risk analysis using Monte Carlo simulation and create a report.
- Create and set project document properties & fetch all or specific existing properties.
- Get a project's extended attributes, time-scaled data, or recurring info of a specific task.
- Reschedule project tasks, dates, and other settings.
- Calculate slacks & recalculate project completion or incompletion work.
- Fetch a project document in the desired format.
- Delete project task with its related references & rebuild the task tree.
- [Convert project documents](https://docs.aspose.cloud/tasks/convert-project-document-to-the-specified-format/) to other formats.
- Manipulate task data.
- [Manage project's resources](https://docs.aspose.cloud/tasks/working-with-resources/).
- Handle task links & task assignments.
- Work with project's extended attributes.
- [Read Microsoft Project’s document properties](https://docs.aspose.cloud/tasks/working-with-calendars/) such as start and finish date, tasks scheduling types and so on.
- [Read Microsoft Project’s Calendars](https://docs.aspose.cloud/tasks/working-with-calendars/) and Calendar Exceptions information.

## Read & Write Project Data
**Microsoft Project** MPP, XML, MPT **Primavera** MPX

## Save Project Data As
XER, XLSX, HTML, XML, TXT, TIF, SVG, PNG, JPEG


## Enhancements in Version 20.11
- Support for the batch creation of tasks (i.e. the ability to create multiple tasks in a single *API* call).

## Enhancements in Version 20.8
- Ability to specify the non-default path for Project Server's *PWA* URL.
- Ability to modify *timephasedData* collection in assignments.

## Enhancements in Version 20.6
- Possibility to render comments when saving as image, HTML or PDF.
- Option to use username and password to connect Project Online (Server) instead of auth token, incase you don't have it.
- Ability to add assignments to your project file along with specifying its cost.
- Quickly adding new tasks to project, when calculation mode is set to automatic.
- Ability to add project in Microsoft Project Server.
- Added support of reading shared resource assignments.

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

## Convert MS Project MPP to PDF in Python

```python
	# Get your ClientId and ClientSecret from https://dashboard.aspose.cloud (free registration required).

	api_client = asposetaskscloud.ApiClient()
	api_client.configuration.host = 'https://api.aspose.cloud'
	api_client.configuration.api_key['api_key'] = 'MY_CLIENT_SECRET'
	api_client.configuration.api_key['app_sid'] = 'MY_CLIENT_ID'
	tasks_api = asposetaskscloud.TasksApi(api_client)

	file_name = 'SomeSeriousPlan.mpp'

	upload_request = asposetaskscloud.models.requests.UploadFileRequest(os.path.join(self.remote_test_folder, file_name), file_name)
	upload_result = self.tasks_api.upload_file(upload_request)

	request = asposetaskscloud.models.requests.GetReportPdfRequest(file_name, ReportType.MILESTONES)
	result = tasks_api.get_report_pdf(request)
```
## Aspose.Tasks Cloud SDKs in Popular Languages

| .NET | PHP | Python| Node.js | Go |
|---|---|---|---|---|
| [GitHub](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-dotnet) |[GitHub](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-php) | [GitHub](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-python) | [GitHub](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-node) |[GitHub](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-go)|
| [NuGet](https://www.nuget.org/packages/Aspose.tasks-Cloud/)| [Composer](https://packagist.org/packages/aspose/tasks-cloud-php) | [PIP](https://pypi.org/project/aspose-tasks-cloud/) | [NPM](https://www.npmjs.com/package/@asposecloud/aspose-tasks-cloud) | [Go.Dev](https://pkg.go.dev/github.com/aspose-tasks-cloud/aspose-tasks-cloud-go/) |

[Product Page](https://products.aspose.cloud/tasks/python) | [Documentation](https://docs.aspose.cloud/display/taskscloud/Home) | [API Reference](https://apireference.aspose.cloud/tasks/) | [Code Samples](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-python) | [Blog](https://blog.aspose.cloud/category/tasks/) | [Free Support](https://forum.aspose.cloud/c/tasks) | [Free Trial](https://dashboard.aspose.cloud/#/apps)
