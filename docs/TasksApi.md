# asposetaskscloud.TasksApi

All URIs are relative to *https://api.aspose.cloud/v3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_file**](TasksApi.md#copy_file) | **PUT** /tasks/storage/file/copy/{srcPath} | Copy file
[**delete_file**](TasksApi.md#delete_file) | **DELETE** /tasks/storage/file/{path} | Delete file
[**download_file**](TasksApi.md#download_file) | **GET** /tasks/storage/file/{path} | Download file
[**move_file**](TasksApi.md#move_file) | **PUT** /tasks/storage/file/move/{srcPath} | Move file
[**upload_file**](TasksApi.md#upload_file) | **POST** /tasks/storage/file/{path} | Upload file
[**copy_folder**](TasksApi.md#copy_folder) | **PUT** /tasks/storage/folder/copy/{srcPath} | Copy folder
[**create_folder**](TasksApi.md#create_folder) | **POST** /tasks/storage/folder/{path} | Create the folder
[**delete_folder**](TasksApi.md#delete_folder) | **DELETE** /tasks/storage/folder/{path} | Delete folder
[**get_files_list**](TasksApi.md#get_files_list) | **GET** /tasks/storage/folder/{path} | Get all files and folders within a folder
[**move_folder**](TasksApi.md#move_folder) | **PUT** /tasks/storage/folder/move/{srcPath} | Move folder
[**get_disc_usage**](TasksApi.md#get_disc_usage) | **GET** /tasks/storage/disc | Get disc usage
[**get_file_versions**](TasksApi.md#get_file_versions) | **GET** /tasks/storage/version/{path} | Get file versions
[**object_exists**](TasksApi.md#object_exists) | **GET** /tasks/storage/exist/{path} | Check if file or folder exists
[**storage_exists**](TasksApi.md#storage_exists) | **GET** /tasks/storage/{storageName}/exist | Check if storage exists
[**delete_assignment**](TasksApi.md#delete_assignment) | **DELETE** /tasks/{name}/assignments/{assignmentUid} | Deletes a project assignment with all references to it.
[**get_assignment**](TasksApi.md#get_assignment) | **GET** /tasks/{name}/assignments/{assignmentUid} | Read project assignment with the specified Uid.
[**get_assignment_timephased_data**](TasksApi.md#get_assignment_timephased_data) | **GET** /tasks/{name}/assignments/{assignmentUid}/timeScaleData | Get timescaled data for an assignment with the specified Uid.
[**get_assignments**](TasksApi.md#get_assignments) | **GET** /tasks/{name}/assignments | Get project&#39;s assignment items.
[**post_assignment**](TasksApi.md#post_assignment) | **POST** /tasks/{name}/assignments | Adds a new assignment to a project and returns assignment item in a response.
[**put_assignment**](TasksApi.md#put_assignment) | **PUT** /tasks/{name}/assignments/{assignmentUid} | Updates resources assignment with the specified Uid.
[**delete_calendar**](TasksApi.md#delete_calendar) | **DELETE** /tasks/{name}/calendars/{calendarUid} | Deletes a project calendar
[**delete_calendar_exception**](TasksApi.md#delete_calendar_exception) | **DELETE** /tasks/{name}/calendars/{calendarUid}/calendarExceptions/{index} | Deletes calendar exception from calendar exceptions collection.
[**get_calendar**](TasksApi.md#get_calendar) | **GET** /tasks/{name}/calendars/{calendarUid} | Get a project&#39;s calendar with the specified Uid.
[**get_calendar_exceptions**](TasksApi.md#get_calendar_exceptions) | **GET** /tasks/{name}/calendars/{calendarUid}/calendarExceptions | Get a list of calendar&#39;s exceptions.
[**get_calendar_work_weeks**](TasksApi.md#get_calendar_work_weeks) | **GET** /tasks/{name}/calendars/{calendarUid}/workWeeks | Gets the collection of work weeks of the specified calendar.
[**get_calendars**](TasksApi.md#get_calendars) | **GET** /tasks/{name}/calendars | Read project calendar items.
[**post_calendar**](TasksApi.md#post_calendar) | **POST** /tasks/{name}/calendars | Adds a new calendar to project file.
[**post_calendar_exception**](TasksApi.md#post_calendar_exception) | **POST** /tasks/{name}/calendars/{calendarUid}/calendarExceptions | Adds a new calendar exception to a calendar.
[**put_calendar**](TasksApi.md#put_calendar) | **PUT** /tasks/{name}/calendars | Edits an existing project calendar.
[**put_calendar_exception**](TasksApi.md#put_calendar_exception) | **PUT** /tasks/{name}/calendars/{calendarUid}/calendarExceptions/{index} | Updates calendar exception.
[**get_critical_path**](TasksApi.md#get_critical_path) | **GET** /tasks/{name}/criticalPath | Returns the list of the tasks which must be completed on time for a project to finish on schedule. Each task of the project is represented as a task item here, which is light-weighted task representation of the project task..
[**get_page_count**](TasksApi.md#get_page_count) | **GET** /tasks/{name}/pagecount | Returns page count for the project to be rendered using given Timescale and PresentationFormat  or specified PageSize.
[**get_project_ids**](TasksApi.md#get_project_ids) | **GET** /tasks/{name}/projectids | Get Uids of projects contained in the file.
[**get_task_document**](TasksApi.md#get_task_document) | **GET** /tasks/{name} | Get a project document.
[**get_task_document_with_format**](TasksApi.md#get_task_document_with_format) | **GET** /tasks/{name}/format | Get a project document in the specified format
[**put_import_project_from_db**](TasksApi.md#put_import_project_from_db) | **PUT** /tasks/importfromdb | Imports project from database with the specified connection string and saves it to specified file with the specified format.
[**put_import_project_from_file**](TasksApi.md#put_import_project_from_file) | **PUT** /tasks/{name}/import | Imports project from primavera db formats (Primavera SQLite .db or Primavera xml) and saves it to specified file with the specified format.
[**put_import_project_from_project_online**](TasksApi.md#put_import_project_from_project_online) | **PUT** /tasks/{name}/importfromprojectonline | Imports project from Project Online and saves it to specified file.
[**get_document_properties**](TasksApi.md#get_document_properties) | **GET** /tasks/{name}/documentproperties | Get a collection of a project&#39;s document properties.
[**get_document_property**](TasksApi.md#get_document_property) | **GET** /tasks/{name}/documentproperties/{propertyName} | Get a document property by name.
[**post_document_property**](TasksApi.md#post_document_property) | **POST** /tasks/{name}/documentproperties/{propertyName} | Set/create document property.
[**put_document_property**](TasksApi.md#put_document_property) | **PUT** /tasks/{name}/documentproperties/{propertyName} | Set/create document property.
[**delete_extended_attribute_by_index**](TasksApi.md#delete_extended_attribute_by_index) | **DELETE** /tasks/{name}/extendedAttributes/{index} | Delete a project extended attribute.
[**get_extended_attribute_by_index**](TasksApi.md#get_extended_attribute_by_index) | **GET** /tasks/{name}/extendedAttributes/{index} | Get a project extended attribute definition with the specified index.
[**get_extended_attributes**](TasksApi.md#get_extended_attributes) | **GET** /tasks/{name}/extendedAttributes | Get a project&#39;s extended attributes.
[**put_extended_attribute**](TasksApi.md#put_extended_attribute) | **PUT** /tasks/{name}/extendedAttributes | Add a new extended attribute definition to a project or  updates existing attribute definition (with the same FieldId).
[**delete_outline_code_by_index**](TasksApi.md#delete_outline_code_by_index) | **DELETE** /tasks/{name}/outlineCodes/{index} | Deletes a project outline code
[**get_outline_code_by_index**](TasksApi.md#get_outline_code_by_index) | **GET** /tasks/{name}/outlineCodes/{index} | Get outline code by index.
[**get_outline_codes**](TasksApi.md#get_outline_codes) | **GET** /tasks/{name}/outlineCodes | Get a project&#39;s outline codes.
[**get_project_list**](TasksApi.md#get_project_list) | **GET** /tasks/projectOnline/projectList | Gets the list of published projects in the current Project Online account.
[**put_recalculate_project**](TasksApi.md#put_recalculate_project) | **PUT** /tasks/{name}/recalculate/project | Reschedules all project tasks ids, outline levels, start/finish dates, sets early/late dates, calculates slacks, work and cost fields.
[**put_recalculate_project_resource_fields**](TasksApi.md#put_recalculate_project_resource_fields) | **PUT** /tasks/{name}/recalculate/resourceFields | Recalculate project resource fields
[**put_recalculate_project_uncomplete_work_to_start_after**](TasksApi.md#put_recalculate_project_uncomplete_work_to_start_after) | **PUT** /tasks/{name}/recalculate/uncompleteWorkToStartAfter | Recalculate project uncomplete work
[**put_recalculate_project_work_as_complete**](TasksApi.md#put_recalculate_project_work_as_complete) | **PUT** /tasks/{name}/recalculate/projectWorkAsComplete | Recalculate project work as complete 
[**get_report_pdf**](TasksApi.md#get_report_pdf) | **GET** /tasks/{name}/report | Returns created report in PDF format.
[**delete_resource**](TasksApi.md#delete_resource) | **DELETE** /tasks/{name}/resources/{resourceUid} | Deletes a project resource with all references to it
[**get_resource**](TasksApi.md#get_resource) | **GET** /tasks/{name}/resources/{resourceUid} | Get project resource.
[**get_resource_assignments**](TasksApi.md#get_resource_assignments) | **GET** /tasks/{name}/resources/{resourceUid}/assignments | Get resource&#39;s assignments.
[**get_resource_timephased_data**](TasksApi.md#get_resource_timephased_data) | **GET** /tasks/{name}/resources/{resourceUid}/timeScaleData | Get timescaled data for a resource with the specified Uid.
[**get_resources**](TasksApi.md#get_resources) | **GET** /tasks/{name}/resources | Get a project&#39;s resources.
[**post_resource**](TasksApi.md#post_resource) | **POST** /tasks/{name}/resources | Add a new resource to a project.
[**put_resource**](TasksApi.md#put_resource) | **PUT** /tasks/{name}/resources/{resourceUid} | Updates resource with the specified Uid
[**get_risk_analysis_report**](TasksApi.md#get_risk_analysis_report) | **GET** /tasks/{name}/riskAnalysisReport | Performs a risk analysys using Monte Carlo simulation and creates a risk analysis report.
[**delete_task**](TasksApi.md#delete_task) | **DELETE** /tasks/{name}/tasks/{taskUid} | Deletes a project task with all references to it and rebuilds tasks tree.
[**get_task**](TasksApi.md#get_task) | **GET** /tasks/{name}/tasks/{taskUid} | Read project task.
[**get_task_assignments**](TasksApi.md#get_task_assignments) | **GET** /tasks/{name}/tasks/{taskUid}/assignments | Get task assignments.
[**get_task_recurring_info**](TasksApi.md#get_task_recurring_info) | **GET** /tasks/{name}/tasks/{taskUid}/recurringInfo | Get recurring info for a task with the specified Uid
[**get_task_timephased_data**](TasksApi.md#get_task_timephased_data) | **GET** /tasks/{name}/tasks/{taskUid}/timeScaleData | Get timescaled data for a task with the specified Uid.
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /tasks/{name}/tasks | Get a project&#39;s tasks.
[**post_task**](TasksApi.md#post_task) | **POST** /tasks/{name}/tasks | Add a new task to a project.
[**post_task_recurring_info**](TasksApi.md#post_task_recurring_info) | **POST** /tasks/{name}/tasks/recurringInfo | Adds a new recurring task.
[**put_move_task**](TasksApi.md#put_move_task) | **PUT** /tasks/{name}/tasks/{taskUid}/move | Move one task to another parent task
[**put_move_task_to_sibling**](TasksApi.md#put_move_task_to_sibling) | **PUT** /tasks/{name}/tasks/{taskUid}/moveToSibling | Move a task to another position under the same parent and the same outline level
[**put_task**](TasksApi.md#put_task) | **PUT** /tasks/{name}/tasks/{taskUid} | Updates special task getting by task UID
[**put_task_recurring_info**](TasksApi.md#put_task_recurring_info) | **PUT** /tasks/{name}/tasks/{taskUid}/recurringInfo | Updates existing task&#39;s recurring info. Note that task should be already recurring.
[**delete_task_link**](TasksApi.md#delete_task_link) | **DELETE** /tasks/{name}/taskLinks/{index} | Delete task link.
[**get_task_links**](TasksApi.md#get_task_links) | **GET** /tasks/{name}/taskLinks | Get tasks&#39; links of a project.
[**post_task_link**](TasksApi.md#post_task_link) | **POST** /tasks/{name}/taskLinks | Adds a new task link to a project.
[**put_task_link**](TasksApi.md#put_task_link) | **PUT** /tasks/{name}/taskLinks/{index} | Updates existing task link.
[**get_vba_project**](TasksApi.md#get_vba_project) | **GET** /tasks/{name}/vbaproject | Returns VBA project.
[**get_wbs_definition**](TasksApi.md#get_wbs_definition) | **GET** /tasks/{name}/wbsDefinition | Get a project&#39;s WBS Definition.
[**put_renumber_wbs_code**](TasksApi.md#put_renumber_wbs_code) | **PUT** /tasks/{name}/renumberWbsCode | Renumber WBS code of passed tasks (if specified) or all project&#39;s tasks.


# **copy_file**
> copy_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Copy file

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
src_path = 'src_path_example' # str | Source file path e.g. '/folder/file.ext'
dest_path = 'dest_path_example' # str | Destination file path
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to copy (optional)

try:
    # Copy file
    api_instance.copy_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling TasksApi->copy_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str**| Destination file path | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(path, storage_name=storage_name, version_id=version_id)

Delete file

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
path = 'path_example' # str | File path e.g. '/folder/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to delete (optional)

try:
    # Delete file
    api_instance.delete_file(path, storage_name=storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling TasksApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> file download_file(path, storage_name=storage_name, version_id=version_id)

Download file

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
path = 'path_example' # str | File path e.g. '/folder/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID to download (optional)

try:
    # Download file
    api_response = api_instance.download_file(path, storage_name=storage_name, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->download_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_file**
> move_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)

Move file

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
src_path = 'src_path_example' # str | Source file path e.g. '/src.ext'
dest_path = 'dest_path_example' # str | Destination file path e.g. '/dest.ext'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)
version_id = 'version_id_example' # str | File version ID to move (optional)

try:
    # Move file
    api_instance.move_file(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name, version_id=version_id)
except ApiException as e:
    print("Exception when calling TasksApi->move_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> FilesUploadResult upload_file(path, file, storage_name=storage_name)

Upload file

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
path = 'path_example' # str | Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.             
file = '/path/to/file.txt' # file | File to upload
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Upload file
    api_response = api_instance.upload_file(path, file, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **file** | **file**| File to upload | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_folder**
> copy_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Copy folder

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
src_path = 'src_path_example' # str | Source folder path e.g. '/src'
dest_path = 'dest_path_example' # str | Destination folder path e.g. '/dst'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try:
    # Copy folder
    api_instance.copy_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling TasksApi->copy_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source folder path e.g. &#39;/src&#39; | 
 **dest_path** | **str**| Destination folder path e.g. &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> create_folder(path, storage_name=storage_name)

Create the folder

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
path = 'path_example' # str | Folder path to create e.g. 'folder_1/folder_2/'
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Create the folder
    api_instance.create_folder(path, storage_name=storage_name)
except ApiException as e:
    print("Exception when calling TasksApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path to create e.g. &#39;folder_1/folder_2/&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(path, storage_name=storage_name, recursive=recursive)

Delete folder

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
path = 'path_example' # str | Folder path e.g. '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)
recursive = false # bool | Enable to delete folders, subfolders and files (optional) (default to false)

try:
    # Delete folder
    api_instance.delete_folder(path, storage_name=storage_name, recursive=recursive)
except ApiException as e:
    print("Exception when calling TasksApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **recursive** | **bool**| Enable to delete folders, subfolders and files | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_list**
> FilesList get_files_list(path, storage_name=storage_name)

Get all files and folders within a folder

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
path = 'path_example' # str | Folder path e.g. '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Get all files and folders within a folder
    api_response = api_instance.get_files_list(path, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_files_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FilesList**](FilesList.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder**
> move_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)

Move folder

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
src_path = 'src_path_example' # str | Folder path to move e.g. '/folder'
dest_path = 'dest_path_example' # str | Destination folder path to move to e.g '/dst'
src_storage_name = 'src_storage_name_example' # str | Source storage name (optional)
dest_storage_name = 'dest_storage_name_example' # str | Destination storage name (optional)

try:
    # Move folder
    api_instance.move_folder(src_path, dest_path, src_storage_name=src_storage_name, dest_storage_name=dest_storage_name)
except ApiException as e:
    print("Exception when calling TasksApi->move_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Folder path to move e.g. &#39;/folder&#39; | 
 **dest_path** | **str**| Destination folder path to move to e.g &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disc_usage**
> DiscUsage get_disc_usage(storage_name=storage_name)

Get disc usage

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Get disc usage
    api_response = api_instance.get_disc_usage(storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_disc_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**DiscUsage**](DiscUsage.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_versions**
> FileVersions get_file_versions(path, storage_name=storage_name)

Get file versions

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
path = 'path_example' # str | File path e.g. '/file.ext'
storage_name = 'storage_name_example' # str | Storage name (optional)

try:
    # Get file versions
    api_response = api_instance.get_file_versions(path, storage_name=storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_file_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

### Return type

[**FileVersions**](FileVersions.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_exists**
> ObjectExist object_exists(path, storage_name=storage_name, version_id=version_id)

Check if file or folder exists

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
path = 'path_example' # str | File or folder path e.g. '/file.ext' or '/folder'
storage_name = 'storage_name_example' # str | Storage name (optional)
version_id = 'version_id_example' # str | File version ID (optional)

try:
    # Check if file or folder exists
    api_response = api_instance.object_exists(path, storage_name=storage_name, version_id=version_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->object_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID | [optional] 

### Return type

[**ObjectExist**](ObjectExist.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_exists**
> StorageExist storage_exists(storage_name)

Check if storage exists

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
storage_name = 'storage_name_example' # str | Storage name

try:
    # Check if storage exists
    api_response = api_instance.storage_exists(storage_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->storage_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | 

### Return type

[**StorageExist**](StorageExist.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assignment**
> AsposeResponse delete_assignment(name, assignment_uid, storage=storage, folder=folder, file_name=file_name)

Deletes a project assignment with all references to it.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
assignment_uid = 56 # int | assignment Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
file_name = 'file_name_example' # str | The name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document. (optional)

try:
    # Deletes a project assignment with all references to it.
    api_response = api_instance.delete_assignment(name, assignment_uid, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **assignment_uid** | **int**| assignment Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **file_name** | **str**| The name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assignment**
> AssignmentResponse get_assignment(name, assignment_uid, storage=storage, folder=folder)

Read project assignment with the specified Uid.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
assignment_uid = 56 # int | Assignment Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Read project assignment with the specified Uid.
    api_response = api_instance.get_assignment(name, assignment_uid, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **assignment_uid** | **int**| Assignment Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AssignmentResponse**](AssignmentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assignment_timephased_data**
> TimephasedDataResponse get_assignment_timephased_data(name, assignment_uid, type=type, start_date=start_date, end_date=end_date, folder=folder, storage=storage)

Get timescaled data for an assignment with the specified Uid.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
assignment_uid = 56 # int | Uid of assignment to get timephased data for.
type = 'type_example' # str | Type of timephased data to get. (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try:
    # Get timescaled data for an assignment with the specified Uid.
    api_response = api_instance.get_assignment_timephased_data(name, assignment_uid, type=type, start_date=start_date, end_date=end_date, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_assignment_timephased_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **assignment_uid** | **int**| Uid of assignment to get timephased data for. | 
 **type** | **str**| Type of timephased data to get. | [optional] 
 **start_date** | **datetime**| Start date. | [optional] 
 **end_date** | **datetime**| End date. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**TimephasedDataResponse**](TimephasedDataResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assignments**
> AssignmentItemsResponse get_assignments(name, storage=storage, folder=folder)

Get project's assignment items.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get project's assignment items.
    api_response = api_instance.get_assignments(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AssignmentItemsResponse**](AssignmentItemsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_assignment**
> AssignmentItemResponse post_assignment(name, task_uid, resource_uid, units=units, file_name=file_name, storage=storage, folder=folder)

Adds a new assignment to a project and returns assignment item in a response.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uid = 56 # int | The unique id of the task to be assigned.
resource_uid = 56 # int | The unique id of the resource to be assigned.
units = 1.2 # float | The units for the new assignment. Default value is 1. (optional)
file_name = 'file_name_example' # str | The name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Adds a new assignment to a project and returns assignment item in a response.
    api_response = api_instance.post_assignment(name, task_uid, resource_uid, units=units, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uid** | **int**| The unique id of the task to be assigned. | 
 **resource_uid** | **int**| The unique id of the resource to be assigned. | 
 **units** | **float**| The units for the new assignment. Default value is 1. | [optional] 
 **file_name** | **str**| The name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AssignmentItemResponse**](AssignmentItemResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_assignment**
> AssignmentResponse put_assignment(name, assignment_uid, assignment, mode=mode, recalculate=recalculate, storage=storage, folder=folder, file_name=file_name)

Updates resources assignment with the specified Uid.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The file name
assignment_uid = 56 # int | Assignment UID
assignment = asposetaskscloud.ResourceAssignment() # ResourceAssignment | Assignment DTO
mode = '0' # str | Project's calculation mode (optional) (default to 0)
recalculate = true # bool | boolean value (optional) (default to true)
storage = 'storage_example' # str | The document storage (optional)
folder = 'folder_example' # str | The document storage (optional)
file_name = 'file_name_example' # str | The filename to save Changes (optional)

try:
    # Updates resources assignment with the specified Uid.
    api_response = api_instance.put_assignment(name, assignment_uid, assignment, mode=mode, recalculate=recalculate, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name | 
 **assignment_uid** | **int**| Assignment UID | 
 **assignment** | [**ResourceAssignment**](ResourceAssignment.md)| Assignment DTO | 
 **mode** | **str**| Project&#39;s calculation mode | [optional] [default to 0]
 **recalculate** | **bool**| boolean value | [optional] [default to true]
 **storage** | **str**| The document storage | [optional] 
 **folder** | **str**| The document storage | [optional] 
 **file_name** | **str**| The filename to save Changes | [optional] 

### Return type

[**AssignmentResponse**](AssignmentResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_calendar**
> AsposeResponse delete_calendar(name, calendar_uid, storage=storage, folder=folder, file_name=file_name)

Deletes a project calendar

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
calendar_uid = 56 # int | Calendar's Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
file_name = 'file_name_example' # str | The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. (optional)

try:
    # Deletes a project calendar
    api_response = api_instance.delete_calendar(name, calendar_uid, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **calendar_uid** | **int**| Calendar&#39;s Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **file_name** | **str**| The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_calendar_exception**
> AsposeResponse delete_calendar_exception(name, calendar_uid, index, file_name=file_name, storage=storage, folder=folder)

Deletes calendar exception from calendar exceptions collection.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
calendar_uid = 56 # int | Calendar Uid
index = 56 # int | Index of the calendar exception. See CalendarException.Index property.
file_name = 'file_name_example' # str | The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Deletes calendar exception from calendar exceptions collection.
    api_response = api_instance.delete_calendar_exception(name, calendar_uid, index, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_calendar_exception: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **calendar_uid** | **int**| Calendar Uid | 
 **index** | **int**| Index of the calendar exception. See CalendarException.Index property. | 
 **file_name** | **str**| The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calendar**
> CalendarResponse get_calendar(name, calendar_uid, storage=storage, folder=folder)

Get a project's calendar with the specified Uid.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
calendar_uid = 56 # int | Calendar's Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a project's calendar with the specified Uid.
    api_response = api_instance.get_calendar(name, calendar_uid, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **calendar_uid** | **int**| Calendar&#39;s Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CalendarResponse**](CalendarResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calendar_exceptions**
> CalendarExceptionsResponse get_calendar_exceptions(name, calendar_uid, storage=storage, folder=folder)

Get a list of calendar's exceptions.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
calendar_uid = 56 # int | Calendar's Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a list of calendar's exceptions.
    api_response = api_instance.get_calendar_exceptions(name, calendar_uid, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_calendar_exceptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **calendar_uid** | **int**| Calendar&#39;s Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CalendarExceptionsResponse**](CalendarExceptionsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calendar_work_weeks**
> CalendarWorkWeeksResponse get_calendar_work_weeks(name, calendar_uid, storage=storage, folder=folder)

Gets the collection of work weeks of the specified calendar.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
calendar_uid = 56 # int | Calendar Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Gets the collection of work weeks of the specified calendar.
    api_response = api_instance.get_calendar_work_weeks(name, calendar_uid, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_calendar_work_weeks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **calendar_uid** | **int**| Calendar Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CalendarWorkWeeksResponse**](CalendarWorkWeeksResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calendars**
> CalendarItemsResponse get_calendars(name, storage=storage, folder=folder)

Read project calendar items.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Read project calendar items.
    api_response = api_instance.get_calendars(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_calendars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CalendarItemsResponse**](CalendarItemsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_calendar**
> CalendarItemResponse post_calendar(name, calendar, file_name=file_name, storage=storage, folder=folder)

Adds a new calendar to project file.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
calendar = asposetaskscloud.Calendar() # Calendar | Calendar DTO
file_name = 'file_name_example' # str | The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Adds a new calendar to project file.
    api_response = api_instance.post_calendar(name, calendar, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **calendar** | [**Calendar**](Calendar.md)| Calendar DTO | 
 **file_name** | **str**| The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**CalendarItemResponse**](CalendarItemResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_calendar_exception**
> AsposeResponse post_calendar_exception(name, calendar_uid, calendar_exception, file_name=file_name, storage=storage, folder=folder)

Adds a new calendar exception to a calendar.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
calendar_uid = 56 # int | Calendar's Uid
calendar_exception = asposetaskscloud.CalendarException() # CalendarException | CalendarException DTO
file_name = 'file_name_example' # str | The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Adds a new calendar exception to a calendar.
    api_response = api_instance.post_calendar_exception(name, calendar_uid, calendar_exception, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_calendar_exception: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **calendar_uid** | **int**| Calendar&#39;s Uid | 
 **calendar_exception** | [**CalendarException**](CalendarException.md)| CalendarException DTO | 
 **file_name** | **str**| The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_calendar**
> AsposeResponse put_calendar(name, calendar_uid, calendar, file_name=file_name, storage=storage, folder=folder)

Edits an existing project calendar.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
calendar_uid = 56 # int | The Uid of an existing calendar to edit.
calendar = asposetaskscloud.Calendar() # Calendar | Modified calendar DTO
file_name = 'file_name_example' # str | The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Edits an existing project calendar.
    api_response = api_instance.put_calendar(name, calendar_uid, calendar, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **calendar_uid** | **int**| The Uid of an existing calendar to edit. | 
 **calendar** | [**Calendar**](Calendar.md)| Modified calendar DTO | 
 **file_name** | **str**| The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_calendar_exception**
> AsposeResponse put_calendar_exception(name, calendar_uid, index, calendar_exception, file_name=file_name, storage=storage, folder=folder)

Updates calendar exception.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
calendar_uid = 56 # int | Calendar Uid
index = 56 # int | Index of the calendar exception. See CalendarException.Index property.
calendar_exception = asposetaskscloud.CalendarException() # CalendarException | CalendarException DTO
file_name = 'file_name_example' # str | The name of the project document to save changes to. If this parameter              is omitted then the changes will be saved to the source project document. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Updates calendar exception.
    api_response = api_instance.put_calendar_exception(name, calendar_uid, index, calendar_exception, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_calendar_exception: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **calendar_uid** | **int**| Calendar Uid | 
 **index** | **int**| Index of the calendar exception. See CalendarException.Index property. | 
 **calendar_exception** | [**CalendarException**](CalendarException.md)| CalendarException DTO | 
 **file_name** | **str**| The name of the project document to save changes to. If this parameter              is omitted then the changes will be saved to the source project document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_critical_path**
> TaskItemsResponse get_critical_path(name, storage=storage, folder=folder)

Returns the list of the tasks which must be completed on time for a project to finish on schedule. Each task of the project is represented as a task item here, which is light-weighted task representation of the project task..

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Returns the list of the tasks which must be completed on time for a project to finish on schedule. Each task of the project is represented as a task item here, which is light-weighted task representation of the project task..
    api_response = api_instance.get_critical_path(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_critical_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TaskItemsResponse**](TaskItemsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_count**
> PageCountResponse get_page_count(name, page_size=page_size, presentation_format=presentation_format, timescale=timescale, start_date=start_date, end_date=end_date, folder=folder, storage=storage)

Returns page count for the project to be rendered using given Timescale and PresentationFormat  or specified PageSize.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
page_size = 'page_size_example' # str | PageSize to get page count for. (optional)
presentation_format = 'presentation_format_example' # str | PresentationFormat to get page count for. (optional)
timescale = '1' # str | Timescale to get page count for. (optional) (default to 1)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date to get page count for. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date to get page count for. (optional)
folder = 'folder_example' # str | The document folder (optional)
storage = 'storage_example' # str | The document storage. (optional)

try:
    # Returns page count for the project to be rendered using given Timescale and PresentationFormat  or specified PageSize.
    api_response = api_instance.get_page_count(name, page_size=page_size, presentation_format=presentation_format, timescale=timescale, start_date=start_date, end_date=end_date, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_page_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **page_size** | **str**| PageSize to get page count for. | [optional] 
 **presentation_format** | **str**| PresentationFormat to get page count for. | [optional] 
 **timescale** | **str**| Timescale to get page count for. | [optional] [default to 1]
 **start_date** | **datetime**| Start date to get page count for. | [optional] 
 **end_date** | **datetime**| End date to get page count for. | [optional] 
 **folder** | **str**| The document folder | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**PageCountResponse**](PageCountResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_ids**
> ProjectIdsResponse get_project_ids(name, storage=storage, folder=folder)

Get Uids of projects contained in the file.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get Uids of projects contained in the file.
    api_response = api_instance.get_project_ids(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_project_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ProjectIdsResponse**](ProjectIdsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_document**
> file get_task_document(name, storage=storage, folder=folder)

Get a project document.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a project document.
    api_response = api_instance.get_task_document(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_document_with_format**
> file get_task_document_with_format(name, format, return_as_zip_archive=return_as_zip_archive, storage=storage, folder=folder)

Get a project document in the specified format

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
format = 'format_example' # str | The format of the resulting file.
return_as_zip_archive = false # bool | If parameter is true, HTML resources are included as separate files and returned along with the resulting html file as a zip package. (optional) (default to false)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a project document in the specified format
    api_response = api_instance.get_task_document_with_format(name, format, return_as_zip_archive=return_as_zip_archive, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_document_with_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **format** | **str**| The format of the resulting file. | 
 **return_as_zip_archive** | **bool**| If parameter is true, HTML resources are included as separate files and returned along with the resulting html file as a zip package. | [optional] [default to false]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_import_project_from_db**
> AsposeResponse put_import_project_from_db(database_type, connection_string, project_uid, filename, format=format, folder=folder, storage=storage, database_schema=database_schema)

Imports project from database with the specified connection string and saves it to specified file with the specified format.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
database_type = 'database_type_example' # str | The type of source database. The supported values are (Msp, Mpd, Primavera).
connection_string = 'connection_string_example' # str | The connection string to the source database.
project_uid = 'project_uid_example' # str | Uid of the project to import.
filename = 'filename_example' # str | The name of the resulting file.
format = 'format_example' # str | Format of the resulting file. The import to Mpp format is not supported. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)
database_schema = 'database_schema_example' # str | Schema of Microsoft project database (if applicable) (optional)

try:
    # Imports project from database with the specified connection string and saves it to specified file with the specified format.
    api_response = api_instance.put_import_project_from_db(database_type, connection_string, project_uid, filename, format=format, folder=folder, storage=storage, database_schema=database_schema)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_import_project_from_db: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_type** | **str**| The type of source database. The supported values are (Msp, Mpd, Primavera). | 
 **connection_string** | **str**| The connection string to the source database. | 
 **project_uid** | **str**| Uid of the project to import. | 
 **filename** | **str**| The name of the resulting file. | 
 **format** | **str**| Format of the resulting file. The import to Mpp format is not supported. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **database_schema** | **str**| Schema of Microsoft project database (if applicable) | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_import_project_from_file**
> AsposeResponse put_import_project_from_file(name, project_uid, filename, file_type=file_type, folder=folder, storage=storage, output_file_format=output_file_format)

Imports project from primavera db formats (Primavera SQLite .db or Primavera xml) and saves it to specified file with the specified format.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
project_uid = 'project_uid_example' # str | Uid of the project to import.
filename = 'filename_example' # str | The name of the resulting file.
file_type = 'file_type_example' # str | The type of file to import. The supported values are (PrimaveraSqliteDb, PrimaveraXml). (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)
output_file_format = 'output_file_format_example' # str | The format of the resulting file. (optional)

try:
    # Imports project from primavera db formats (Primavera SQLite .db or Primavera xml) and saves it to specified file with the specified format.
    api_response = api_instance.put_import_project_from_file(name, project_uid, filename, file_type=file_type, folder=folder, storage=storage, output_file_format=output_file_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_import_project_from_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **project_uid** | **str**| Uid of the project to import. | 
 **filename** | **str**| The name of the resulting file. | 
 **file_type** | **str**| The type of file to import. The supported values are (PrimaveraSqliteDb, PrimaveraXml). | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **output_file_format** | **str**| The format of the resulting file. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_import_project_from_project_online**
> AsposeResponse put_import_project_from_project_online(name, site_url, guid, x_project_online_token, format=format, folder=folder, storage=storage)

Imports project from Project Online and saves it to specified file.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the resulting file.
site_url = 'site_url_example' # str | The url of sharepoint site. For example, \"https://your_company_name.sharepoint.com\"
guid = 'guid_example' # str | Guid of the project to import.
x_project_online_token = 'x_project_online_token_example' # str | Authorization token for the SharePoint. For example, in c# it can be retrieved using SharePointOnlineCredentials class from Microsoft.SharePoint.Client.Runtime assembly
format = 'format_example' # str | Format of the resulting file. The import to Mpp format is not supported. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try:
    # Imports project from Project Online and saves it to specified file.
    api_response = api_instance.put_import_project_from_project_online(name, site_url, guid, x_project_online_token, format=format, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_import_project_from_project_online: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the resulting file. | 
 **site_url** | **str**| The url of sharepoint site. For example, \&quot;https://your_company_name.sharepoint.com\&quot; | 
 **guid** | **str**| Guid of the project to import. | 
 **x_project_online_token** | **str**| Authorization token for the SharePoint. For example, in c# it can be retrieved using SharePointOnlineCredentials class from Microsoft.SharePoint.Client.Runtime assembly | 
 **format** | **str**| Format of the resulting file. The import to Mpp format is not supported. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_properties**
> DocumentPropertiesResponse get_document_properties(name, storage=storage, folder=folder)

Get a collection of a project's document properties.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a collection of a project's document properties.
    api_response = api_instance.get_document_properties(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_document_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DocumentPropertiesResponse**](DocumentPropertiesResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_property**
> DocumentPropertyResponse get_document_property(name, property_name, storage=storage, folder=folder)

Get a document property by name.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a document property by name.
    api_response = api_instance.get_document_property(name, property_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| The property name. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**DocumentPropertyResponse**](DocumentPropertyResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_property**
> DocumentPropertyResponse post_document_property(name, property_name, _property, storage=storage, folder=folder, filename=filename)

Set/create document property.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
_property = asposetaskscloud.DocumentProperty() # DocumentProperty | DocumentProperty with new property value.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
filename = 'filename_example' # str | Name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document. (optional)

try:
    # Set/create document property.
    api_response = api_instance.post_document_property(name, property_name, _property, storage=storage, folder=folder, filename=filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| The property name. | 
 **_property** | [**DocumentProperty**](DocumentProperty.md)| DocumentProperty with new property value. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **filename** | **str**| Name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document. | [optional] 

### Return type

[**DocumentPropertyResponse**](DocumentPropertyResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_document_property**
> DocumentPropertyResponse put_document_property(name, property_name, _property, storage=storage, folder=folder, filename=filename)

Set/create document property.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The document name.
property_name = 'property_name_example' # str | The property name.
_property = asposetaskscloud.DocumentProperty() # DocumentProperty | DocumentProperty with new property value.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
filename = 'filename_example' # str | Name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document. (optional)

try:
    # Set/create document property.
    api_response = api_instance.put_document_property(name, property_name, _property, storage=storage, folder=folder, filename=filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_document_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The document name. | 
 **property_name** | **str**| The property name. | 
 **_property** | [**DocumentProperty**](DocumentProperty.md)| DocumentProperty with new property value. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **filename** | **str**| Name of the project document to save changes to. If this parameter is omitted then the changes will be saved to the source project document. | [optional] 

### Return type

[**DocumentPropertyResponse**](DocumentPropertyResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extended_attribute_by_index**
> AsposeResponse delete_extended_attribute_by_index(name, index, storage=storage, folder=folder)

Delete a project extended attribute.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
index = 56 # int | Index (See ExtendedAttributeItem.Index property) or FieldId of the extended attribute.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Delete a project extended attribute.
    api_response = api_instance.delete_extended_attribute_by_index(name, index, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_extended_attribute_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **index** | **int**| Index (See ExtendedAttributeItem.Index property) or FieldId of the extended attribute. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_attribute_by_index**
> ExtendedAttributeResponse get_extended_attribute_by_index(name, index, storage=storage, folder=folder)

Get a project extended attribute definition with the specified index.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
index = 56 # int | Index (See ExtendedAttributeItem.Index property) or FieldId of the extended attribute.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a project extended attribute definition with the specified index.
    api_response = api_instance.get_extended_attribute_by_index(name, index, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_extended_attribute_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **index** | **int**| Index (See ExtendedAttributeItem.Index property) or FieldId of the extended attribute. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ExtendedAttributeResponse**](ExtendedAttributeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extended_attributes**
> ExtendedAttributeItemsResponse get_extended_attributes(name, storage=storage, folder=folder)

Get a project's extended attributes.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a project's extended attributes.
    api_response = api_instance.get_extended_attributes(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_extended_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ExtendedAttributeItemsResponse**](ExtendedAttributeItemsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_extended_attribute**
> ExtendedAttributeItemResponse put_extended_attribute(extended_attribute, name, file_name=file_name, storage=storage, folder=folder)

Add a new extended attribute definition to a project or  updates existing attribute definition (with the same FieldId).

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
extended_attribute = asposetaskscloud.ExtendedAttributeDefinition() # ExtendedAttributeDefinition | Definition of the extended attribute to add.
name = 'name_example' # str | The name of the file.
file_name = 'file_name_example' # str | The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Add a new extended attribute definition to a project or  updates existing attribute definition (with the same FieldId).
    api_response = api_instance.put_extended_attribute(extended_attribute, name, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_extended_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extended_attribute** | [**ExtendedAttributeDefinition**](ExtendedAttributeDefinition.md)| Definition of the extended attribute to add. | 
 **name** | **str**| The name of the file. | 
 **file_name** | **str**| The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ExtendedAttributeItemResponse**](ExtendedAttributeItemResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outline_code_by_index**
> AsposeResponse delete_outline_code_by_index(name, index, storage=storage, folder=folder)

Deletes a project outline code

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
index = 56 # int | Index of the outline code. See OutlineCodeItem.Index property.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Deletes a project outline code
    api_response = api_instance.delete_outline_code_by_index(name, index, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_outline_code_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **index** | **int**| Index of the outline code. See OutlineCodeItem.Index property. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outline_code_by_index**
> OutlineCodeResponse get_outline_code_by_index(name, index, storage=storage, folder=folder)

Get outline code by index.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
index = 56 # int | Index of the outline code. See OutlineCodeItem.Index property.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get outline code by index.
    api_response = api_instance.get_outline_code_by_index(name, index, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_outline_code_by_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **index** | **int**| Index of the outline code. See OutlineCodeItem.Index property. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**OutlineCodeResponse**](OutlineCodeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outline_codes**
> OutlineCodeItemsResponse get_outline_codes(name, storage=storage, folder=folder)

Get a project's outline codes.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a project's outline codes.
    api_response = api_instance.get_outline_codes(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_outline_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**OutlineCodeItemsResponse**](OutlineCodeItemsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_list**
> ProjectListResponse get_project_list(site_url, x_project_online_token)

Gets the list of published projects in the current Project Online account.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
site_url = 'site_url_example' # str | The url of sharepoint site. For example, \"https://your_company_name.sharepoint.com\"
x_project_online_token = 'x_project_online_token_example' # str | Authorization token for the SharePoint. For example, in c# it can be retrieved using SharePointOnlineCredentials class from Microsoft.SharePoint.Client.Runtime assembly

try:
    # Gets the list of published projects in the current Project Online account.
    api_response = api_instance.get_project_list(site_url, x_project_online_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_project_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_url** | **str**| The url of sharepoint site. For example, \&quot;https://your_company_name.sharepoint.com\&quot; | 
 **x_project_online_token** | **str**| Authorization token for the SharePoint. For example, in c# it can be retrieved using SharePointOnlineCredentials class from Microsoft.SharePoint.Client.Runtime assembly | 

### Return type

[**ProjectListResponse**](ProjectListResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_recalculate_project**
> ProjectRecalculateResponse put_recalculate_project(name, mode=mode, validate=validate, file_name=file_name, storage=storage, folder=folder)

Reschedules all project tasks ids, outline levels, start/finish dates, sets early/late dates, calculates slacks, work and cost fields.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The filename
mode = '0' # str | Project's calculation mode (optional) (default to 0)
validate = false # bool | If true the validation of recalculation will be performed. What data is validated:     At the moment only basic validation of task and task link date ranges is implemented.     Task's date ranges (e.g. ActualStart - ActualFinish, EarlyStart - EarlyFinish, etc.) as well as Task Links dates will be checked against the date criteria that start date is less or equal than finish date. (optional) (default to false)
file_name = 'file_name_example' # str | The filename to save the changes (optional)
storage = 'storage_example' # str | The document storage (optional)
folder = 'folder_example' # str | The document folder (optional)

try:
    # Reschedules all project tasks ids, outline levels, start/finish dates, sets early/late dates, calculates slacks, work and cost fields.
    api_response = api_instance.put_recalculate_project(name, mode=mode, validate=validate, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_recalculate_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The filename | 
 **mode** | **str**| Project&#39;s calculation mode | [optional] [default to 0]
 **validate** | **bool**| If true the validation of recalculation will be performed. What data is validated:     At the moment only basic validation of task and task link date ranges is implemented.     Task&#39;s date ranges (e.g. ActualStart - ActualFinish, EarlyStart - EarlyFinish, etc.) as well as Task Links dates will be checked against the date criteria that start date is less or equal than finish date. | [optional] [default to false]
 **file_name** | **str**| The filename to save the changes | [optional] 
 **storage** | **str**| The document storage | [optional] 
 **folder** | **str**| The document folder | [optional] 

### Return type

[**ProjectRecalculateResponse**](ProjectRecalculateResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_recalculate_project_resource_fields**
> AsposeResponse put_recalculate_project_resource_fields(name, storage=storage, folder=folder, file_name=file_name)

Recalculate project resource fields

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file
storage = 'storage_example' # str | The document storage (optional)
folder = 'folder_example' # str | The document folder (optional)
file_name = 'file_name_example' # str | The document fileName (optional)

try:
    # Recalculate project resource fields
    api_response = api_instance.put_recalculate_project_resource_fields(name, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_recalculate_project_resource_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file | 
 **storage** | **str**| The document storage | [optional] 
 **folder** | **str**| The document folder | [optional] 
 **file_name** | **str**| The document fileName | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_recalculate_project_uncomplete_work_to_start_after**
> AsposeResponse put_recalculate_project_uncomplete_work_to_start_after(name, after, storage=storage, folder=folder, file_name=file_name)

Recalculate project uncomplete work

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The file name
after = '2013-10-20T19:20:30+01:00' # datetime | DateTime (from System lib)
storage = 'storage_example' # str | The document storage  (optional)
folder = 'folder_example' # str | The document folder (optional)
file_name = 'file_name_example' # str | The filename to save the changes (optional)

try:
    # Recalculate project uncomplete work
    api_response = api_instance.put_recalculate_project_uncomplete_work_to_start_after(name, after, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_recalculate_project_uncomplete_work_to_start_after: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name | 
 **after** | **datetime**| DateTime (from System lib) | 
 **storage** | **str**| The document storage  | [optional] 
 **folder** | **str**| The document folder | [optional] 
 **file_name** | **str**| The filename to save the changes | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_recalculate_project_work_as_complete**
> AsposeResponse put_recalculate_project_work_as_complete(name, complete_through, set_zero_or_hundred_percent_complete_only=set_zero_or_hundred_percent_complete_only, storage=storage, folder=folder, file_name=file_name)

Recalculate project work as complete 

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The filename
complete_through = '2013-10-20T19:20:30+01:00' # datetime | DateTime (type from System lib)
set_zero_or_hundred_percent_complete_only = true # bool | boolean value (optional) (default to true)
storage = 'storage_example' # str | The document storage (optional)
folder = 'folder_example' # str | The document folder (optional)
file_name = 'file_name_example' # str | The filename to save the changes (optional)

try:
    # Recalculate project work as complete 
    api_response = api_instance.put_recalculate_project_work_as_complete(name, complete_through, set_zero_or_hundred_percent_complete_only=set_zero_or_hundred_percent_complete_only, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_recalculate_project_work_as_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The filename | 
 **complete_through** | **datetime**| DateTime (type from System lib) | 
 **set_zero_or_hundred_percent_complete_only** | **bool**| boolean value | [optional] [default to true]
 **storage** | **str**| The document storage | [optional] 
 **folder** | **str**| The document folder | [optional] 
 **file_name** | **str**| The filename to save the changes | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_pdf**
> file get_report_pdf(name, type, storage=storage, folder=folder)

Returns created report in PDF format.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
type = 'type_example' # str | A type of the project's graphical report.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Returns created report in PDF format.
    api_response = api_instance.get_report_pdf(name, type, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_report_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **type** | **str**| A type of the project&#39;s graphical report. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource**
> AsposeResponse delete_resource(name, resource_uid, storage=storage, folder=folder, file_name=file_name)

Deletes a project resource with all references to it

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
resource_uid = 56 # int | Resource Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
file_name = 'file_name_example' # str | The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. (optional)

try:
    # Deletes a project resource with all references to it
    api_response = api_instance.delete_resource(name, resource_uid, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **resource_uid** | **int**| Resource Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **file_name** | **str**| The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource**
> ResourceResponse get_resource(name, resource_uid, storage=storage, folder=folder)

Get project resource.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
resource_uid = 56 # int | Resource Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get project resource.
    api_response = api_instance.get_resource(name, resource_uid, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **resource_uid** | **int**| Resource Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_assignments**
> AssignmentsResponse get_resource_assignments(name, resource_uid, storage=storage, folder=folder)

Get resource's assignments.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
resource_uid = 56 # int | Resource Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get resource's assignments.
    api_response = api_instance.get_resource_assignments(name, resource_uid, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_resource_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **resource_uid** | **int**| Resource Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AssignmentsResponse**](AssignmentsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_timephased_data**
> TimephasedDataResponse get_resource_timephased_data(name, resource_uid, type=type, start_date=start_date, end_date=end_date, folder=folder, storage=storage)

Get timescaled data for a resource with the specified Uid.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
resource_uid = 56 # int | Uid of resource to get timephased data for.
type = 'type_example' # str | Type of timephased data to get. (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try:
    # Get timescaled data for a resource with the specified Uid.
    api_response = api_instance.get_resource_timephased_data(name, resource_uid, type=type, start_date=start_date, end_date=end_date, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_resource_timephased_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **resource_uid** | **int**| Uid of resource to get timephased data for. | 
 **type** | **str**| Type of timephased data to get. | [optional] 
 **start_date** | **datetime**| Start date. | [optional] 
 **end_date** | **datetime**| End date. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**TimephasedDataResponse**](TimephasedDataResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resources**
> ResourceItemsResponse get_resources(name, storage=storage, folder=folder)

Get a project's resources.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a project's resources.
    api_response = api_instance.get_resources(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ResourceItemsResponse**](ResourceItemsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_resource**
> ResourceItemResponse post_resource(name, resource_name=resource_name, before_resource_id=before_resource_id, file_name=file_name, storage=storage, folder=folder)

Add a new resource to a project.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
resource_name = 'resource_name_example' # str | The name of the new resource. The default value is an empty string (optional)
before_resource_id = 56 # int | The id of the resource to insert the new resource before. The default value is the id of the last resource in a project file. (optional)
file_name = 'file_name_example' # str | The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Add a new resource to a project.
    api_response = api_instance.post_resource(name, resource_name=resource_name, before_resource_id=before_resource_id, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **resource_name** | **str**| The name of the new resource. The default value is an empty string | [optional] 
 **before_resource_id** | **int**| The id of the resource to insert the new resource before. The default value is the id of the last resource in a project file. | [optional] 
 **file_name** | **str**| The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**ResourceItemResponse**](ResourceItemResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_resource**
> ResourceResponse put_resource(name, resource_uid, resource, mode=mode, recalculate=recalculate, storage=storage, folder=folder, file_name=file_name)

Updates resource with the specified Uid

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The file name
resource_uid = 56 # int | The Uid of a resource
resource = asposetaskscloud.Resource() # Resource | The representation of the modified resource
mode = '0' # str | The calculation mode of a project (optional) (default to 0)
recalculate = true # bool | Specifies whether the project's recalculation should be performed (optional) (default to true)
storage = 'storage_example' # str | The document storage (optional)
folder = 'folder_example' # str | The document storage (optional)
file_name = 'file_name_example' # str | The filename to save Changes (optional)

try:
    # Updates resource with the specified Uid
    api_response = api_instance.put_resource(name, resource_uid, resource, mode=mode, recalculate=recalculate, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The file name | 
 **resource_uid** | **int**| The Uid of a resource | 
 **resource** | [**Resource**](Resource.md)| The representation of the modified resource | 
 **mode** | **str**| The calculation mode of a project | [optional] [default to 0]
 **recalculate** | **bool**| Specifies whether the project&#39;s recalculation should be performed | [optional] [default to true]
 **storage** | **str**| The document storage | [optional] 
 **folder** | **str**| The document storage | [optional] 
 **file_name** | **str**| The filename to save Changes | [optional] 

### Return type

[**ResourceResponse**](ResourceResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_risk_analysis_report**
> file get_risk_analysis_report(name, task_uid, distribution_type=distribution_type, optimistic=optimistic, pessimistic=pessimistic, confidence_level=confidence_level, iterations=iterations, storage=storage, folder=folder, file_name=file_name)

Performs a risk analysys using Monte Carlo simulation and creates a risk analysis report.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uid = 56 # int | The uid of the task for which this risk will be applied in Monte Carlo simulation.
distribution_type = '1' # str | Gets or sets the probability distribution used in Monte Carlo simulation. The default value is ProbabilityDistributionType.Normal. (optional) (default to 1)
optimistic = 70 # int | The percentage of the most likely task duration which can happen in the best possible project scenario. The default value is 75, which means that if the estimated specified task duration is 4 days then the optimistic duration will be 3 days. (optional) (default to 70)
pessimistic = 130 # int | The percentage of the most likely task duration which can happen in the worst possible project scenario. The default value is 125, which means that if the estimated specified task duration is 4 days then the pessimistic duration will be 5 days. (optional) (default to 130)
confidence_level = '75' # str | Gets or sets the confidence level that correspond to the percentage of the time the actual generated values will be within optimistic and pessimistic estimates. The default value is CL99. (optional) (default to 75)
iterations = 100 # int | The number of iterations to use in Monte Carlo simulation. The default value is 100. (optional) (default to 100)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The folder storage. (optional)
file_name = 'file_name_example' # str | The resulting report fileName. (optional)

try:
    # Performs a risk analysys using Monte Carlo simulation and creates a risk analysis report.
    api_response = api_instance.get_risk_analysis_report(name, task_uid, distribution_type=distribution_type, optimistic=optimistic, pessimistic=pessimistic, confidence_level=confidence_level, iterations=iterations, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_risk_analysis_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uid** | **int**| The uid of the task for which this risk will be applied in Monte Carlo simulation. | 
 **distribution_type** | **str**| Gets or sets the probability distribution used in Monte Carlo simulation. The default value is ProbabilityDistributionType.Normal. | [optional] [default to 1]
 **optimistic** | **int**| The percentage of the most likely task duration which can happen in the best possible project scenario. The default value is 75, which means that if the estimated specified task duration is 4 days then the optimistic duration will be 3 days. | [optional] [default to 70]
 **pessimistic** | **int**| The percentage of the most likely task duration which can happen in the worst possible project scenario. The default value is 125, which means that if the estimated specified task duration is 4 days then the pessimistic duration will be 5 days. | [optional] [default to 130]
 **confidence_level** | **str**| Gets or sets the confidence level that correspond to the percentage of the time the actual generated values will be within optimistic and pessimistic estimates. The default value is CL99. | [optional] [default to 75]
 **iterations** | **int**| The number of iterations to use in Monte Carlo simulation. The default value is 100. | [optional] [default to 100]
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The folder storage. | [optional] 
 **file_name** | **str**| The resulting report fileName. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> AsposeResponse delete_task(name, task_uid, storage=storage, folder=folder, file_name=file_name)

Deletes a project task with all references to it and rebuilds tasks tree.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uid = 56 # int | Task Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
file_name = 'file_name_example' # str | The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document. (optional)

try:
    # Deletes a project task with all references to it and rebuilds tasks tree.
    api_response = api_instance.delete_task(name, task_uid, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uid** | **int**| Task Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **file_name** | **str**| The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> TaskResponse get_task(name, task_uid, storage=storage, folder=folder)

Read project task.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uid = 56 # int | Task Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Read project task.
    api_response = api_instance.get_task(name, task_uid, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uid** | **int**| Task Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_assignments**
> AssignmentsResponse get_task_assignments(name, task_uid, storage=storage, folder=folder)

Get task assignments.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uid = 56 # int | Task Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get task assignments.
    api_response = api_instance.get_task_assignments(name, task_uid, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uid** | **int**| Task Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AssignmentsResponse**](AssignmentsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_recurring_info**
> RecurringInfoResponse get_task_recurring_info(name, task_uid, storage=storage, folder=folder)

Get recurring info for a task with the specified Uid

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uid = 56 # int | Task Uid
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get recurring info for a task with the specified Uid
    api_response = api_instance.get_task_recurring_info(name, task_uid, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_recurring_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uid** | **int**| Task Uid | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**RecurringInfoResponse**](RecurringInfoResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_timephased_data**
> TimephasedDataResponse get_task_timephased_data(name, task_uid, type=type, start_date=start_date, end_date=end_date, folder=folder, storage=storage)

Get timescaled data for a task with the specified Uid.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uid = 56 # int | Uid of task to get timephased data for.
type = 'type_example' # str | Type of timephased data to get. (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start date. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | End date. (optional)
folder = 'folder_example' # str | The document folder. (optional)
storage = 'storage_example' # str | The document storage. (optional)

try:
    # Get timescaled data for a task with the specified Uid.
    api_response = api_instance.get_task_timephased_data(name, task_uid, type=type, start_date=start_date, end_date=end_date, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_timephased_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uid** | **int**| Uid of task to get timephased data for. | 
 **type** | **str**| Type of timephased data to get. | [optional] 
 **start_date** | **datetime**| Start date. | [optional] 
 **end_date** | **datetime**| End date. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**TimephasedDataResponse**](TimephasedDataResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> TaskItemsResponse get_tasks(name, storage=storage, folder=folder)

Get a project's tasks.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a project's tasks.
    api_response = api_instance.get_tasks(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TaskItemsResponse**](TaskItemsResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_task**
> TaskItemResponse post_task(name, task_name=task_name, before_task_id=before_task_id, file_name=file_name, storage=storage, folder=folder)

Add a new task to a project.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_name = 'task_name_example' # str | The name of the new task. The default value is an empty string (optional)
before_task_id = 56 # int | The id of the task to insert the new task before.              The default value is the id of the last task in a project file. (optional)
file_name = 'file_name_example' # str | The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Add a new task to a project.
    api_response = api_instance.post_task(name, task_name=task_name, before_task_id=before_task_id, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_name** | **str**| The name of the new task. The default value is an empty string | [optional] 
 **before_task_id** | **int**| The id of the task to insert the new task before.              The default value is the id of the last task in a project file. | [optional] 
 **file_name** | **str**| The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TaskItemResponse**](TaskItemResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_task_recurring_info**
> TaskItemResponse post_task_recurring_info(name, parent_task_uid, task_name, recurring_info, calendar_name, file_name=file_name, storage=storage, folder=folder)

Adds a new recurring task.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
parent_task_uid = 56 # int | The Uid of parent task for the created recurring task
task_name = 'task_name_example' # str | Name of the task to create.
recurring_info = asposetaskscloud.RecurringInfo() # RecurringInfo | DTO which defines task's recurring info.
calendar_name = 'calendar_name_example' # str | Name of the project's calendar to use for recurring task's scheduling.
file_name = 'file_name_example' # str | File name to save changes to. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Adds a new recurring task.
    api_response = api_instance.post_task_recurring_info(name, parent_task_uid, task_name, recurring_info, calendar_name, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_task_recurring_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **parent_task_uid** | **int**| The Uid of parent task for the created recurring task | 
 **task_name** | **str**| Name of the task to create. | 
 **recurring_info** | [**RecurringInfo**](RecurringInfo.md)| DTO which defines task&#39;s recurring info. | 
 **calendar_name** | **str**| Name of the project&#39;s calendar to use for recurring task&#39;s scheduling. | 
 **file_name** | **str**| File name to save changes to. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TaskItemResponse**](TaskItemResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_move_task**
> AsposeResponse put_move_task(name, task_uid, parent_task_uid, file_name=file_name, storage=storage, folder=folder)

Move one task to another parent task

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uid = 56 # int | Unique id of the task to be moved.
parent_task_uid = 56 # int | Unique id of the new parent task.
file_name = 'file_name_example' # str | The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.  (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Move one task to another parent task
    api_response = api_instance.put_move_task(name, task_uid, parent_task_uid, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_move_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uid** | **int**| Unique id of the task to be moved. | 
 **parent_task_uid** | **int**| Unique id of the new parent task. | 
 **file_name** | **str**| The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document.  | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_move_task_to_sibling**
> AsposeResponse put_move_task_to_sibling(name, task_uid, before_task_uid, file_name=file_name, storage=storage, folder=folder)

Move a task to another position under the same parent and the same outline level

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uid = 56 # int | Task Unique Id.
before_task_uid = 56 # int | Unique Id of the task after which the current task will be placed.
file_name = 'file_name_example' # str | The name of the project document to save changes to.             If this parameter is omitted then the changes will be saved to the source project document. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Move a task to another position under the same parent and the same outline level
    api_response = api_instance.put_move_task_to_sibling(name, task_uid, before_task_uid, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_move_task_to_sibling: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uid** | **int**| Task Unique Id. | 
 **before_task_uid** | **int**| Unique Id of the task after which the current task will be placed. | 
 **file_name** | **str**| The name of the project document to save changes to.             If this parameter is omitted then the changes will be saved to the source project document. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task**
> TaskResponse put_task(name, task_uid, task, mode=mode, recalculate=recalculate, storage=storage, folder=folder, file_name=file_name)

Updates special task getting by task UID

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uid = 56 # int | Task UID
task = asposetaskscloud.Task() # Task | TaskDTO
mode = '0' # str | CalculationModeDTO (optional) (default to 0)
recalculate = true # bool | boolean value  (optional) (default to true)
storage = 'storage_example' # str | The document strorage (optional)
folder = 'folder_example' # str | The document folder (optional)
file_name = 'file_name_example' # str | The name of the file to save changes (optional)

try:
    # Updates special task getting by task UID
    api_response = api_instance.put_task(name, task_uid, task, mode=mode, recalculate=recalculate, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uid** | **int**| Task UID | 
 **task** | [**Task**](Task.md)| TaskDTO | 
 **mode** | **str**| CalculationModeDTO | [optional] [default to 0]
 **recalculate** | **bool**| boolean value  | [optional] [default to true]
 **storage** | **str**| The document strorage | [optional] 
 **folder** | **str**| The document folder | [optional] 
 **file_name** | **str**| The name of the file to save changes | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task_recurring_info**
> AsposeResponse put_task_recurring_info(name, task_uid, recurring_info, file_name=file_name, storage=storage, folder=folder)

Updates existing task's recurring info. Note that task should be already recurring.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uid = 56 # int | Task Uid.
recurring_info = asposetaskscloud.RecurringInfo() # RecurringInfo | A modified DTO of task's recurring info.
file_name = 'file_name_example' # str | File name to save changes to. (optional)
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Updates existing task's recurring info. Note that task should be already recurring.
    api_response = api_instance.put_task_recurring_info(name, task_uid, recurring_info, file_name=file_name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_task_recurring_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uid** | **int**| Task Uid. | 
 **recurring_info** | [**RecurringInfo**](RecurringInfo.md)| A modified DTO of task&#39;s recurring info. | 
 **file_name** | **str**| File name to save changes to. | [optional] 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task_link**
> AsposeResponse delete_task_link(name, index, storage=storage, folder=folder, file_name=file_name)

Delete task link.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
index = 56 # int | Index of the task link object. See TaskLink.Index property.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
file_name = 'file_name_example' # str | The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document. (optional)

try:
    # Delete task link.
    api_response = api_instance.delete_task_link(name, index, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_task_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **index** | **int**| Index of the task link object. See TaskLink.Index property. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **file_name** | **str**| The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_links**
> TaskLinksResponse get_task_links(name, storage=storage, folder=folder)

Get tasks' links of a project.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get tasks' links of a project.
    api_response = api_instance.get_task_links(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**TaskLinksResponse**](TaskLinksResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_task_link**
> AsposeResponse post_task_link(name, task_link, storage=storage, folder=folder, file_name=file_name)

Adds a new task link to a project.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_link = asposetaskscloud.TaskLink() # TaskLink | The TaskLink object representation that should be added.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
file_name = 'file_name_example' # str | The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document. (optional)

try:
    # Adds a new task link to a project.
    api_response = api_instance.post_task_link(name, task_link, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_task_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_link** | [**TaskLink**](TaskLink.md)| The TaskLink object representation that should be added. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **file_name** | **str**| The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task_link**
> TaskLinkResponse put_task_link(name, index, task_link, storage=storage, folder=folder, file_name=file_name)

Updates existing task link.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
index = 56 # int | Index of the task link object. See TaskLink.Index property.
task_link = asposetaskscloud.TaskLink() # TaskLink | The representation of the modified TaskLink object.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)
file_name = 'file_name_example' # str | The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document. (optional)

try:
    # Updates existing task link.
    api_response = api_instance.put_task_link(name, index, task_link, storage=storage, folder=folder, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_task_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **index** | **int**| Index of the task link object. See TaskLink.Index property. | 
 **task_link** | [**TaskLink**](TaskLink.md)| The representation of the modified TaskLink object. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 
 **file_name** | **str**| The name of the project document to save changes to.  If this parameter is omitted then the changes will be saved to the source project document. | [optional] 

### Return type

[**TaskLinkResponse**](TaskLinkResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vba_project**
> VbaProjectResponse get_vba_project(name, folder=folder, storage=storage)

Returns VBA project.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file
folder = 'folder_example' # str | The folder storage (optional)
storage = 'storage_example' # str | The document storage. (optional)

try:
    # Returns VBA project.
    api_response = api_instance.get_vba_project(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_vba_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file | 
 **folder** | **str**| The folder storage | [optional] 
 **storage** | **str**| The document storage. | [optional] 

### Return type

[**VbaProjectResponse**](VbaProjectResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wbs_definition**
> WBSDefinitionResponse get_wbs_definition(name, storage=storage, folder=folder)

Get a project's WBS Definition.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
storage = 'storage_example' # str | The document storage. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Get a project's WBS Definition.
    api_response = api_instance.get_wbs_definition(name, storage=storage, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_wbs_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **storage** | **str**| The document storage. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**WBSDefinitionResponse**](WBSDefinitionResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_renumber_wbs_code**
> AsposeResponse put_renumber_wbs_code(name, task_uids, storage=storage, file_name=file_name, folder=folder)

Renumber WBS code of passed tasks (if specified) or all project's tasks.

### Example
```python
from __future__ import print_function
import time
import asposetaskscloud
from asposetaskscloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposetaskscloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposetaskscloud.TasksApi(asposetaskscloud.ApiClient(configuration))
name = 'name_example' # str | The name of the file.
task_uids = [asposetaskscloud.list[int]()] # list[int] | Uids of task for WBS codes renumbering. If not specified, WBS codes for all tasks will be renumbered.
storage = 'storage_example' # str | The document storage. (optional)
file_name = 'file_name_example' # str | The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. (optional)
folder = 'folder_example' # str | The document folder. (optional)

try:
    # Renumber WBS code of passed tasks (if specified) or all project's tasks.
    api_response = api_instance.put_renumber_wbs_code(name, task_uids, storage=storage, file_name=file_name, folder=folder)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_renumber_wbs_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file. | 
 **task_uids** | **list[int]**| Uids of task for WBS codes renumbering. If not specified, WBS codes for all tasks will be renumbered. | 
 **storage** | **str**| The document storage. | [optional] 
 **file_name** | **str**| The name of the project document to save changes to.              If this parameter is omitted then the changes will be saved to the source project document. | [optional] 
 **folder** | **str**| The document folder. | [optional] 

### Return type

[**AsposeResponse**](AsposeResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

