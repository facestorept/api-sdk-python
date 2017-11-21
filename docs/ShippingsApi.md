# swagger_client.ShippingsApi

All URIs are relative to *https://api.facestore.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_shipping**](ShippingsApi.md#add_shipping) | **POST** /shippings | 
[**delete_shipping_by_id**](ShippingsApi.md#delete_shipping_by_id) | **DELETE** /shippings/{id}/ | 
[**get_shipping_by_id**](ShippingsApi.md#get_shipping_by_id) | **GET** /shippings/{id}/ | 
[**get_shippings**](ShippingsApi.md#get_shippings) | **GET** /shippings | 
[**update_shipping_by_id**](ShippingsApi.md#update_shipping_by_id) | **PUT** /shippings/{id}/ | 
[**update_shipping_by_id_0**](ShippingsApi.md#update_shipping_by_id_0) | **PATCH** /shippings/{id}/ | 


# **add_shipping**
> InlineResponse2013 add_shipping(shipping)



Creates a new shipping in the store.

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
api_instance = swagger_client.ShippingsApi(swagger_client.ApiClient(configuration))
shipping = swagger_client.Shipping() # Shipping | Shipping to add to the store

try:
    api_response = api_instance.add_shipping(shipping)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingsApi->add_shipping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping** | [**Shipping**](Shipping.md)| Shipping to add to the store | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shipping_by_id**
> delete_shipping_by_id(id)



deletes a single shipping based on the ID supplied

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
api_instance = swagger_client.ShippingsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of shipping to delete

try:
    api_instance.delete_shipping_by_id(id)
except ApiException as e:
    print("Exception when calling ShippingsApi->delete_shipping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of shipping to delete | 

### Return type

void (empty response body)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipping_by_id**
> InlineResponse2013 get_shipping_by_id(id, limit=limit)



Returns a shipping based on a single ID

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
api_instance = swagger_client.ShippingsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of shipping to fetch
limit = 56 # int | max records to return (optional)

try:
    api_response = api_instance.get_shipping_by_id(id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingsApi->get_shipping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of shipping to fetch | 
 **limit** | **int**| max records to return | [optional] 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shippings**
> InlineResponse2003 get_shippings(includes=includes, limit=limit, order_by=order_by)



Returns all shippings from the system that the user has access to

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
api_instance = swagger_client.ShippingsApi(swagger_client.ApiClient(configuration))
includes = ['includes_example'] # list[str] | Include associated objects within response (optional)
limit = 56 # int | max records to return (optional)
order_by = ['order_by_example'] # list[str] | Specify the field to be sorted, examples:  - `?order_by=id|desc` - `?order_by=updated_at|desc,position|asc`  (optional)

try:
    api_response = api_instance.get_shippings(includes=includes, limit=limit, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingsApi->get_shippings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includes** | [**list[str]**](str.md)| Include associated objects within response | [optional] 
 **limit** | **int**| max records to return | [optional] 
 **order_by** | [**list[str]**](str.md)| Specify the field to be sorted, examples:  - &#x60;?order_by&#x3D;id|desc&#x60; - &#x60;?order_by&#x3D;updated_at|desc,position|asc&#x60;  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipping_by_id**
> InlineResponse2013 update_shipping_by_id(id, tax)



update a single shipping based on the ID supplied

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
api_instance = swagger_client.ShippingsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of shipping to update
tax = swagger_client.Shipping() # Shipping | Shipping to update in store

try:
    api_response = api_instance.update_shipping_by_id(id, tax)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingsApi->update_shipping_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of shipping to update | 
 **tax** | [**Shipping**](Shipping.md)| Shipping to update in store | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipping_by_id_0**
> InlineResponse2013 update_shipping_by_id_0(id, tax)



update a single shipping based on the ID supplied

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
api_instance = swagger_client.ShippingsApi(swagger_client.ApiClient(configuration))
id = 789 # int | ID of shipping to update
tax = swagger_client.Shipping() # Shipping | Shipping to update in store

try:
    api_response = api_instance.update_shipping_by_id_0(id, tax)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShippingsApi->update_shipping_by_id_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of shipping to update | 
 **tax** | [**Shipping**](Shipping.md)| Shipping to update in store | 

### Return type

[**InlineResponse2013**](InlineResponse2013.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

