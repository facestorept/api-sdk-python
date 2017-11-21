# swagger-client
This is a reference to Facestore API.  # Introduction This API is documented in **OpenAPI format** and provided by [facestore.pt](http://facestore.pt) team.  # About the API Through the Facestore API your applications can retrieve and manage Facestore platform content in your store. The base address of the API is `https://api.facestore.pt`. There are several endpoints at that address, each with its own unique path. All endpoints are private and you need the permissions to access them. To get an API Token you have to be client of Facestore and access your personal account to request it (see the next topic).  # Get API Token To consume the Facestore API is take the unique token to identify your requests. You can do that accessing the store manager admin and doing the following steps: 1. Go to ``configurations > API`` section. 2. Copy the unique token.  # Requests The API is based on REST principles: data resources are accessed via standard HTTPS requests in UTF-8 format to an API endpoint. Where possible, the API strives to use appropriate HTTP verbs for each action: | VERB     | DESCRIPTION                                            | | -------- |:-------------:                                         | | GET      | Used for retrieving resources.                         | | POST     | Used for creating resources.                           | | PUT      | Used for changing/replacing resources or collections.  | | PATCH    | Used for changing/replacing partial resources.         | | DELETE   | Used for deleting resources.                           |  # Responses Response Status Codes The API uses the following response status codes, as defined in the RFC 2616 and RFC 6585:  | STATUS CODE | DESCRIPTION                                                                                                                                                                                                                       | |:-----------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | 200         | OK - The request has succeeded. The client can read the result of the request in the body and the headers of the response.                                                                                                        | | 201         | Created - The request has been fulfilled and resulted in a new resource being created.                                                                                                                                            | | 202         | Accepted - The request has been accepted for processing, but the processing has not been completed.                                                                                                                               | | 204         | No Content - The request has succeeded but returns no message body.                                                                                                                                                               | | 304         | Not Modified. See Conditional requests.                                                                                                                                                                                           | | 400         | Bad Request - The request could not be understood by the server due to malformed syntax. The message body will contain more information; see Error Details.                                                                       | | 401         | Unauthorized - The request requires user authentication or, if the request included authorization credentials, authorization has been refused for those credentials.                                                              | | 403         | Forbidden - The server understood the request, but is refusing to fulfill it.                                                                                                                                                     | | 404         | Not Found - The requested resource could not be found. This error can be due to a temporary or permanent condition.                                                                                                               | | 429         | Too Many Requests - Rate limiting has been applied.                                                                                                                                                                               | | 500         | Internal Server Error. You should never receive this error because our clever coders catch them all ... but if you are unlucky enough to get one, please report it to us through a comment at the bottom of this page.            | | 502         | Bad Gateway - The server was acting as a gateway or proxy and received an invalid response from the upstream server.                                                                                                              | | 503         | Service Unavailable - The server is currently unable to handle the request due to a temporary condition which will be alleviated after some delay. You can choose to resend the request again.                                    |  # Rate limiting To make the API fast for everybody, rate limits apply.  Rate limiting is applied on an application basis (based on client id), regardless of how many users are using it.  If you get status code 429, it means that you have sent too many requests. If this happens, have a look in the Retry-After header, where you will see a number displayed. This is the amount of seconds that you need to wait, before you can retry sending your requests.  You can check the returned HTTP headers of any API request to see your current rate limit status:  ``` curl -i https://api.facestore.pt/v1/sample HTTP/1.1 200 OK Date: Mon, 01 Dec 2016 17:27:06 GMT Status: 200 OK X-RateLimit-Limit: 60 X-RateLimit-Remaining: 56 X-RateLimit-Reset: 1372700873 ```  The headers tell you everything you need to know about your current rate limit status:  | HEADER NAME           | DESCRIPTION                                                                     | |:---------------------:|:-------------------------------------------------------------------------------:| | X-RateLimit-Limit   | The maximum number of requests that the consumer is permitted to make per hour. | | X-RateLimit-Remaining | The number of requests remaining in the current rate limit window.              | | X-RateLimit-Reset   | The time at which the current rate limit window resets in UTC epoch seconds.    |  # Timestamps Timestamps are returned in ISO 8601 format as Coordinated Universal Time (UTC) with zero offset: YYYY-MM-DDTHH:MM:SSZ. If the time is imprecise (for example, the date/time of an product is created), an additional field will show the precision; see for example, created_at in an product object.  # Error Details The API uses the following format to describe unsuccessful responses, return information about the error as an error JSON object containing the following information::  | KEY         | VALUE TYPE   | VALUE DESCRIPTION | |:-----------:|:------------:|:-----------------:| | status_code | integer    | The HTTP status code (also returned in the response header; see Response Status Codes for more information). | | message     | string     | A short description of the cause of the error. | 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1.4
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [http://facestore.pt](http://facestore.pt)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/facestorept/api-sdk-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/facestorept/api-sdk-python.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
swagger_client.configuration.api_key['APIToken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['APIToken'] = 'Bearer'
# create an instance of the API class
api_instance = swagger_client.BrandsApi()
brand = swagger_client.Brand() # Brand | Brand to add to the store

try:
    api_response = api_instance.add_brands(brand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BrandsApi->add_brands: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.facestore.local/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrandsApi* | [**add_brands**](docs/BrandsApi.md#add_brands) | **POST** /brands | 
*BrandsApi* | [**delete_brand_by_id**](docs/BrandsApi.md#delete_brand_by_id) | **DELETE** /brands/{id}/ | 
*BrandsApi* | [**get_brand_by_id**](docs/BrandsApi.md#get_brand_by_id) | **GET** /brands/{id}/ | 
*BrandsApi* | [**get_brands**](docs/BrandsApi.md#get_brands) | **GET** /brands | 
*BrandsApi* | [**update_category_by_id**](docs/BrandsApi.md#update_category_by_id) | **PUT** /brands/{id}/ | 
*BrandsApi* | [**update_category_by_id_0**](docs/BrandsApi.md#update_category_by_id_0) | **PATCH** /brands/{id}/ | 
*CategoriesApi* | [**add_categories**](docs/CategoriesApi.md#add_categories) | **POST** /categories | 
*CategoriesApi* | [**delete_category_by_id**](docs/CategoriesApi.md#delete_category_by_id) | **DELETE** /categories/{id}/ | 
*CategoriesApi* | [**get_categories**](docs/CategoriesApi.md#get_categories) | **GET** /categories | 
*CategoriesApi* | [**get_category_by_id**](docs/CategoriesApi.md#get_category_by_id) | **GET** /categories/{id}/ | 
*CategoriesApi* | [**update_category_by_id**](docs/CategoriesApi.md#update_category_by_id) | **PUT** /categories/{id}/ | 
*CustomersApi* | [**get_customer_by_id**](docs/CustomersApi.md#get_customer_by_id) | **GET** /customers/{id}/ | 
*CustomersApi* | [**get_customers**](docs/CustomersApi.md#get_customers) | **GET** /customers | 
*OrdersApi* | [**get_order_by_id**](docs/OrdersApi.md#get_order_by_id) | **GET** /orders/{id}/ | 
*OrdersApi* | [**get_orders**](docs/OrdersApi.md#get_orders) | **GET** /orders | 
*PaymentsApi* | [**get_payment_by_id**](docs/PaymentsApi.md#get_payment_by_id) | **GET** /payments/{id}/ | 
*PaymentsApi* | [**get_payments**](docs/PaymentsApi.md#get_payments) | **GET** /payments | 
*ProductsApi* | [**add_product**](docs/ProductsApi.md#add_product) | **POST** /products | 
*ProductsApi* | [**delete_product_by_id**](docs/ProductsApi.md#delete_product_by_id) | **DELETE** /products/{id}/ | 
*ProductsApi* | [**get_product_by_id**](docs/ProductsApi.md#get_product_by_id) | **GET** /products/{id}/ | 
*ProductsApi* | [**get_products**](docs/ProductsApi.md#get_products) | **GET** /products | 
*ProductsApi* | [**update_product_by_id**](docs/ProductsApi.md#update_product_by_id) | **PUT** /products/{id}/ | 
*ProductsApi* | [**update_product_by_id_0**](docs/ProductsApi.md#update_product_by_id_0) | **PATCH** /products/{id}/ | 
*ProductsAttributesApi* | [**add_products_attributes**](docs/ProductsAttributesApi.md#add_products_attributes) | **POST** /attributes | 
*ProductsAttributesApi* | [**delete_product_attribute_by_id**](docs/ProductsAttributesApi.md#delete_product_attribute_by_id) | **DELETE** /attributes/{id}/ | 
*ProductsAttributesApi* | [**get_product_attribute_by_id**](docs/ProductsAttributesApi.md#get_product_attribute_by_id) | **GET** /attributes/{id}/ | 
*ProductsAttributesApi* | [**get_products_attributes**](docs/ProductsAttributesApi.md#get_products_attributes) | **GET** /attributes | 
*ProductsAttributesApi* | [**update_product_attribute_by_id**](docs/ProductsAttributesApi.md#update_product_attribute_by_id) | **PUT** /attributes/{id}/ | 
*ShippingsApi* | [**add_shipping**](docs/ShippingsApi.md#add_shipping) | **POST** /shippings | 
*ShippingsApi* | [**delete_shipping_by_id**](docs/ShippingsApi.md#delete_shipping_by_id) | **DELETE** /shippings/{id}/ | 
*ShippingsApi* | [**get_shipping_by_id**](docs/ShippingsApi.md#get_shipping_by_id) | **GET** /shippings/{id}/ | 
*ShippingsApi* | [**get_shippings**](docs/ShippingsApi.md#get_shippings) | **GET** /shippings | 
*ShippingsApi* | [**update_shipping_by_id**](docs/ShippingsApi.md#update_shipping_by_id) | **PUT** /shippings/{id}/ | 
*ShippingsApi* | [**update_shipping_by_id_0**](docs/ShippingsApi.md#update_shipping_by_id_0) | **PATCH** /shippings/{id}/ | 
*TaxesApi* | [**add_taxes**](docs/TaxesApi.md#add_taxes) | **POST** /taxes | 
*TaxesApi* | [**delete_tax_by_id**](docs/TaxesApi.md#delete_tax_by_id) | **DELETE** /taxes/{id}/ | 
*TaxesApi* | [**get_tax_by_id**](docs/TaxesApi.md#get_tax_by_id) | **GET** /taxes/{id}/ | 
*TaxesApi* | [**get_taxes**](docs/TaxesApi.md#get_taxes) | **GET** /taxes | 
*TaxesApi* | [**update_tax_by_id**](docs/TaxesApi.md#update_tax_by_id) | **PUT** /taxes/{id}/ | 
*TaxesApi* | [**update_tax_by_id_0**](docs/TaxesApi.md#update_tax_by_id_0) | **PATCH** /taxes/{id}/ | 


## Documentation For Models

 - [Attribute](docs/Attribute.md)
 - [AttributeOptions](docs/AttributeOptions.md)
 - [Brand](docs/Brand.md)
 - [Category](docs/Category.md)
 - [Customer](docs/Customer.md)
 - [DefaultResponse](docs/DefaultResponse.md)
 - [I18n](docs/I18n.md)
 - [I18nProduct](docs/I18nProduct.md)
 - [I18nProductSeo](docs/I18nProductSeo.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2001Meta](docs/InlineResponse2001Meta.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse2012](docs/InlineResponse2012.md)
 - [InlineResponse2013](docs/InlineResponse2013.md)
 - [InlineResponse2014](docs/InlineResponse2014.md)
 - [MetaPartialResponse](docs/MetaPartialResponse.md)
 - [NotFoundResponse](docs/NotFoundResponse.md)
 - [Options](docs/Options.md)
 - [Order](docs/Order.md)
 - [Payment](docs/Payment.md)
 - [Product](docs/Product.md)
 - [Shipping](docs/Shipping.md)
 - [Tax](docs/Tax.md)


## Documentation For Authorization


## APIKeyHeader

- **Type**: API key
- **API key parameter name**: APIToken
- **Location**: HTTP header


## Author

apihelp@facestore.pt

