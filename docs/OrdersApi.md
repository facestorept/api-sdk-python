# swagger_client.OrdersApi

All URIs are relative to *https://api.facestore.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_by_id**](OrdersApi.md#get_order_by_id) | **GET** /orders/{id}/ | 
[**get_orders**](OrdersApi.md#get_orders) | **GET** /orders | 


# **get_order_by_id**
> list[Order] get_order_by_id(id, includes=includes)



Returns all orders from the system that the user has access to  ### Includes You can give the following values on includes parameter: `products, customers` 

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of customer
includes = ['includes_example'] # list[str] | Include associated objects within response (optional)

try:
    api_response = api_instance.get_order_by_id(id, includes=includes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_order_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of customer | 
 **includes** | [**list[str]**](str.md)| Include associated objects within response | [optional] 

### Return type

[**list[Order]**](Order.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders**
> list[Order] get_orders(includes=includes, limit=limit, order_by=order_by)



Returns all orders from the system that the user has access to  ### Includes You can give the following values on includes parameter: `products, customers` 

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
includes = ['includes_example'] # list[str] | Include associated objects within response (optional)
limit = 56 # int | max records to return (optional)
order_by = ['order_by_example'] # list[str] | Specify the field to be sorted, examples:  - `?order_by=id|desc` - `?order_by=updated_at|desc,position|asc`  (optional)

try:
    api_response = api_instance.get_orders(includes=includes, limit=limit, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->get_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includes** | [**list[str]**](str.md)| Include associated objects within response | [optional] 
 **limit** | **int**| max records to return | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify the field to be sorted, examples:  - &#x60;?order_by&#x3D;id|desc&#x60; - &#x60;?order_by&#x3D;updated_at|desc,position|asc&#x60;  | [optional] 

### Return type

[**list[Order]**](Order.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

