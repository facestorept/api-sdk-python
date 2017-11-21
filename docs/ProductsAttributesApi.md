# swagger_client.ProductsAttributesApi

All URIs are relative to *https://api.facestore.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_products_attributes**](ProductsAttributesApi.md#add_products_attributes) | **POST** /attributes | 
[**delete_product_attribute_by_id**](ProductsAttributesApi.md#delete_product_attribute_by_id) | **DELETE** /attributes/{id}/ | 
[**get_product_attribute_by_id**](ProductsAttributesApi.md#get_product_attribute_by_id) | **GET** /attributes/{id}/ | 
[**get_products_attributes**](ProductsAttributesApi.md#get_products_attributes) | **GET** /attributes | 
[**update_product_attribute_by_id**](ProductsAttributesApi.md#update_product_attribute_by_id) | **PUT** /attributes/{id}/ | 


# **add_products_attributes**
> list[Attribute] add_products_attributes(attribute)



Creates a new attribute of products in the store.

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
api_instance = swagger_client.ProductsAttributesApi(swagger_client.ApiClient(configuration))
attribute = swagger_client.Attribute() # Attribute | Attribute to add to the store

try:
    api_response = api_instance.add_products_attributes(attribute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsAttributesApi->add_products_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute** | [**Attribute**](Attribute.md)| Attribute to add to the store | 

### Return type

[**list[Attribute]**](Attribute.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_product_attribute_by_id**
> delete_product_attribute_by_id(id)



deletes a single attribute of products based on the ID supplied

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
api_instance = swagger_client.ProductsAttributesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of attribute to delete

try:
    api_instance.delete_product_attribute_by_id(id)
except ApiException as e:
    print("Exception when calling ProductsAttributesApi->delete_product_attribute_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of attribute to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_attribute_by_id**
> Attribute get_product_attribute_by_id(id, includes=includes)



Returns a attribute of products based on a single ID  ### Includes You can give the following values on includes parameter: `options` 

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
api_instance = swagger_client.ProductsAttributesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of attribute to fetch
includes = ['includes_example'] # list[str] | Include associated objects within response (optional)

try:
    api_response = api_instance.get_product_attribute_by_id(id, includes=includes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsAttributesApi->get_product_attribute_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of attribute to fetch | 
 **includes** | [**list[str]**](str.md)| Include associated objects within response | [optional] 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_products_attributes**
> list[Attribute] get_products_attributes(includes=includes, limit=limit, order_by=order_by)



Returns all attributes of products from the system that the user has access to  ### Includes You can give the following values on includes parameter: `options` 

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
api_instance = swagger_client.ProductsAttributesApi(swagger_client.ApiClient(configuration))
includes = ['includes_example'] # list[str] | Include associated objects within response (optional)
limit = 56 # int | max records to return (optional)
order_by = ['order_by_example'] # list[str] | Specify the field to be sorted, examples:  - `?order_by=id|desc` - `?order_by=updated_at|desc,position|asc`  (optional)

try:
    api_response = api_instance.get_products_attributes(includes=includes, limit=limit, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsAttributesApi->get_products_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includes** | [**list[str]**](str.md)| Include associated objects within response | [optional] 
 **limit** | **int**| max records to return | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify the field to be sorted, examples:  - &#x60;?order_by&#x3D;id|desc&#x60; - &#x60;?order_by&#x3D;updated_at|desc,position|asc&#x60;  | [optional] 

### Return type

[**list[Attribute]**](Attribute.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product_attribute_by_id**
> Attribute update_product_attribute_by_id(id, product_attribute)



update a single attribute of products based on the ID supplied

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
api_instance = swagger_client.ProductsAttributesApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of attribute to update
product_attribute = swagger_client.Attribute() # Attribute | Attribute to add to the store

try:
    api_response = api_instance.update_product_attribute_by_id(id, product_attribute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsAttributesApi->update_product_attribute_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of attribute to update | 
 **product_attribute** | [**Attribute**](Attribute.md)| Attribute to add to the store | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

