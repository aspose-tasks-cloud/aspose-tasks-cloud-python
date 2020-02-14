# Aspose.Tasks Cloud SDK for Python
This repository contains Aspose.Tasks Cloud SDK for Python source code. This SDK allows you to work with Aspose.Tasks Cloud REST APIs in your Python applications quickly and easily, with zero initial cost.

[Aspose.Tasks Cloud](https://products.aspose.cloud/tasks/family "Aspose.Tasks Cloud")  
[API Reference](https://apireference.aspose.cloud/tasks/)  

## Key Features
* Conversion between various file formats, including MPP->PDF conversion
* Read, change and write Microsoft Project® documents 
* Create, update and write projects in XML project format
* Manage extended attributes
* Define weekdays for calendars and calendar exceptions
* Manage task baseline scheduling and duration
* Create and manage links between tasks
* Manage resources costs and variances
* Access assignment costs and budget

## How to use the SDK?
The complete source code is available in this repository folder. You can either directly use it in your project via source code or get [PyPi](https://pypi.org/project/aspose-tasks-cloud ) (recommended). For more details, please visit our [documentation website](https://docs.aspose.cloud/display/taskscloud/Available+SDKs ).

### Prerequisites

To use Aspose Tasks for Cloud Python SDK you need to register an account with [Aspose Cloud](https://www.aspose.cloud/) and lookup/create App Key and SID at [Cloud Dashboard](https://dashboard.aspose.cloud/#/apps). There is free quota available. For more details, see [Aspose Cloud Pricing](https://purchase.aspose.cloud/pricing).

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install aspose-tasks-cloud
```
(you may need to run `pip` with root permission: `sudo pip install aspose-tasks-cloud`)

Then import the package:
```python
import asposetaskscloud
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import asposetaskscloud
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

[Test](test/) contain various examples of using the SDK.

## Dependencies
- Python 2.7(End of Life in 2020) and 3.7
- referenced packages (see [here](setup.py) for more details)

## Licensing
 
All Aspose.Tasks Cloud SDKs, helper scripts and templates are licensed under [MIT License](https://github.com/aspose-tasks-cloud/aspose-tasks-cloud-python/blob/master/LICENSE). 

## Contact Us
Your feedback is very important to us. Please feel free to contact us using our [Support Forums](https://forum.aspose.cloud/c/tasks).

## Resources
 
[Website](https://www.aspose.cloud/)  
[Product Home](https://products.aspose.cloud/tasks/family)  
[API Reference](https://apireference.aspose.cloud/tasks/)  
[Documentation](https://docs.aspose.cloud/display/taskscloud/Home)  
[Blog](https://blog.aspose.cloud/category/tasks/) 
 
## Other languages
We generate our SDKs in different languages so you may check if yours is available in our [list](https://github.com/aspose-tasks-cloud).
 
If you don't find your language in the list, feel free to request it from us, or use raw REST API requests as you can find it [here](https://products.aspose.cloud/tasks/curl).
