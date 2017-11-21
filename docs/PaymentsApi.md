# swagger_client.PaymentsApi

All URIs are relative to *https://api.facestore.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_by_id**](PaymentsApi.md#get_payment_by_id) | **GET** /payments/{id}/ | 
[**get_payments**](PaymentsApi.md#get_payments) | **GET** /payments | 


# **get_payment_by_id**
> InlineResponse2005 get_payment_by_id(id)



Returns all payments from the system that the user has access to 

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of payment

try:
    api_response = api_instance.get_payment_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of payment | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments**
> InlineResponse2004 get_payments(includes=includes, limit=limit, order_by=order_by)



Returns all payments from the system that the user has access to 

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
includes = ['includes_example'] # list[str] | Include associated objects within response (optional)
limit = 56 # int | max records to return (optional)
order_by = ['order_by_example'] # list[str] | Specify the field to be sorted, examples:  - `?order_by=id|desc` - `?order_by=updated_at|desc,position|asc`  (optional)

try:
    api_response = api_instance.get_payments(includes=includes, limit=limit, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includes** | [**list[str]**](str.md)| Include associated objects within response | [optional] 
 **limit** | **int**| max records to return | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify the field to be sorted, examples:  - &#x60;?order_by&#x3D;id|desc&#x60; - &#x60;?order_by&#x3D;updated_at|desc,position|asc&#x60;  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

