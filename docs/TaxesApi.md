# swagger_client.TaxesApi

All URIs are relative to *https://api.facestore.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_taxes**](TaxesApi.md#add_taxes) | **POST** /taxes | 
[**delete_tax_by_id**](TaxesApi.md#delete_tax_by_id) | **DELETE** /taxes/{id}/ | 
[**get_tax_by_id**](TaxesApi.md#get_tax_by_id) | **GET** /taxes/{id}/ | 
[**get_taxes**](TaxesApi.md#get_taxes) | **GET** /taxes | 
[**update_tax_by_id**](TaxesApi.md#update_tax_by_id) | **PUT** /taxes/{id}/ | 
[**update_tax_by_id_0**](TaxesApi.md#update_tax_by_id_0) | **PATCH** /taxes/{id}/ | 


# **add_taxes**
> InlineResponse2012 add_taxes(tax)



Creates a new tax in the store.

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
api_instance = swagger_client.TaxesApi(swagger_client.ApiClient(configuration))
tax = swagger_client.Tax() # Tax | Tax to add to the store

try:
    api_response = api_instance.add_taxes(tax)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->add_taxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax** | [**Tax**](Tax.md)| Tax to add to the store | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tax_by_id**
> delete_tax_by_id(id)



deletes a single tax based on the ID supplied

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
api_instance = swagger_client.TaxesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of tax to delete

try:
    api_instance.delete_tax_by_id(id)
except ApiException as e:
    print("Exception when calling TaxesApi->delete_tax_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of tax to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_by_id**
> InlineResponse2012 get_tax_by_id(id, limit=limit)



Returns a tax based on a single ID

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
api_instance = swagger_client.TaxesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of tax to fetch
limit = 56 # int | max records to return (optional)

try:
    api_response = api_instance.get_tax_by_id(id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_tax_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of tax to fetch | 
 **limit** | **int**| max records to return | [optional] 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_taxes**
> InlineResponse2002 get_taxes(includes=includes, limit=limit, order_by=order_by)



Returns all taxes from the system that the user has access to

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
api_instance = swagger_client.TaxesApi(swagger_client.ApiClient(configuration))
includes = ['includes_example'] # list[str] | Include associated objects within response (optional)
limit = 56 # int | max records to return (optional)
order_by = ['order_by_example'] # list[str] | Specify the field to be sorted, examples:  - `?order_by=id|desc` - `?order_by=updated_at|desc,position|asc`  (optional)

try:
    api_response = api_instance.get_taxes(includes=includes, limit=limit, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->get_taxes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includes** | [**list[str]**](str.md)| Include associated objects within response | [optional] 
 **limit** | **int**| max records to return | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify the field to be sorted, examples:  - &#x60;?order_by&#x3D;id|desc&#x60; - &#x60;?order_by&#x3D;updated_at|desc,position|asc&#x60;  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_by_id**
> InlineResponse2012 update_tax_by_id(id, tax)



update a single tax based on the ID supplied

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
api_instance = swagger_client.TaxesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of tax to update
tax = swagger_client.Tax() # Tax | Tax to add to the store

try:
    api_response = api_instance.update_tax_by_id(id, tax)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->update_tax_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of tax to update | 
 **tax** | [**Tax**](Tax.md)| Tax to add to the store | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_by_id_0**
> InlineResponse2012 update_tax_by_id_0(id, tax)



update a single tax based on the ID supplied

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
api_instance = swagger_client.TaxesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of tax to update
tax = swagger_client.Tax() # Tax | Tax to add to the store

try:
    api_response = api_instance.update_tax_by_id_0(id, tax)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxesApi->update_tax_by_id_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of tax to update | 
 **tax** | [**Tax**](Tax.md)| Tax to add to the store | 

### Return type

[**InlineResponse2012**](InlineResponse2012.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

