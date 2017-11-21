# swagger_client.CategoriesApi

All URIs are relative to *https://api.facestore.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_categories**](CategoriesApi.md#add_categories) | **POST** /categories | 
[**delete_category_by_id**](CategoriesApi.md#delete_category_by_id) | **DELETE** /categories/{id}/ | 
[**get_categories**](CategoriesApi.md#get_categories) | **GET** /categories | 
[**get_category_by_id**](CategoriesApi.md#get_category_by_id) | **GET** /categories/{id}/ | 
[**update_category_by_id**](CategoriesApi.md#update_category_by_id) | **PUT** /categories/{id}/ | 


# **add_categories**
> InlineResponse2011 add_categories(category)



Creates a new category in the store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['APIToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIToken'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
category = swagger_client.Category() # Category | Category to add to the store

try:
    api_response = api_instance.add_categories(category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->add_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | [**Category**](Category.md)| Category to add to the store | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_category_by_id**
> delete_category_by_id(id)



deletes a single category based on the ID supplied

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['APIToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIToken'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of category to delete

try:
    api_instance.delete_category_by_id(id)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of category to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> InlineResponse2001 get_categories(includes=includes, limit=limit, order_by=order_by)



Returns all categories from the system that the user has access to  ### Includes You can give the following values on includes parameter: `routes, products` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['APIToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIToken'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
includes = ['includes_example'] # list[str] | Include associated objects within response (optional)
limit = 56 # int | max records to return (optional)
order_by = ['order_by_example'] # list[str] | Specify the field to be sorted, examples:  - `?order_by=id|desc` - `?order_by=updated_at|desc,position|asc`  (optional)

try:
    api_response = api_instance.get_categories(includes=includes, limit=limit, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includes** | [**list[str]**](str.md)| Include associated objects within response | [optional] 
 **limit** | **int**| max records to return | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify the field to be sorted, examples:  - &#x60;?order_by&#x3D;id|desc&#x60; - &#x60;?order_by&#x3D;updated_at|desc,position|asc&#x60;  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category_by_id**
> InlineResponse2011 get_category_by_id(id, includes=includes, limit=limit)



Returns a category based on a single ID  ### Includes You can give the following values on includes parameter: `routes, products` 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['APIToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIToken'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of category to fetch
includes = ['includes_example'] # list[str] | Include associated objects within response (optional)
limit = 56 # int | max records to return (optional)

try:
    api_response = api_instance.get_category_by_id(id, includes=includes, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of category to fetch | 
 **includes** | [**list[str]**](str.md)| Include associated objects within response | [optional] 
 **limit** | **int**| max records to return | [optional] 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_category_by_id**
> update_category_by_id(id, category)



update a single category based on the ID supplied

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['APIToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIToken'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of category to update
category = NULL # object | Category to update in store

try:
    api_instance.update_category_by_id(id, category)
except ApiException as e:
    print("Exception when calling CategoriesApi->update_category_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of category to update | 
 **category** | **object**| Category to update in store | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

