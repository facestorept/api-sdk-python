# coding: utf-8

"""
    Facestore API

    This is a reference to Facestore API.  # Introduction This API is documented in **OpenAPI format** and provided by [facestore.pt](http://facestore.pt) team.  # About the API Through the Facestore API your applications can retrieve and manage Facestore platform content in your store. The base address of the API is `https://api.facestore.pt`. There are several endpoints at that address, each with its own unique path. All endpoints are private and you need the permissions to access them. To get an API Token you have to be client of Facestore and access your personal account to request it (see the next topic).  # Get API Token To consume the Facestore API is take the unique token to identify your requests. You can do that accessing the store manager admin and doing the following steps: 1. Go to ``configurations > API`` section. 2. Copy the unique token.  # Requests The API is based on REST principles: data resources are accessed via standard HTTPS requests in UTF-8 format to an API endpoint. Where possible, the API strives to use appropriate HTTP verbs for each action: | VERB     | DESCRIPTION                                            | | -------- |:-------------:                                         | | GET      | Used for retrieving resources.                         | | POST     | Used for creating resources.                           | | PUT      | Used for changing/replacing resources or collections.  | | PATCH    | Used for changing/replacing partial resources.         | | DELETE   | Used for deleting resources.                           |  # Responses Response Status Codes The API uses the following response status codes, as defined in the RFC 2616 and RFC 6585:  | STATUS CODE | DESCRIPTION                                                                                                                                                                                                                       | |:-----------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | 200         | OK - The request has succeeded. The client can read the result of the request in the body and the headers of the response.                                                                                                        | | 201         | Created - The request has been fulfilled and resulted in a new resource being created.                                                                                                                                            | | 202         | Accepted - The request has been accepted for processing, but the processing has not been completed.                                                                                                                               | | 204         | No Content - The request has succeeded but returns no message body.                                                                                                                                                               | | 304         | Not Modified. See Conditional requests.                                                                                                                                                                                           | | 400         | Bad Request - The request could not be understood by the server due to malformed syntax. The message body will contain more information; see Error Details.                                                                       | | 401         | Unauthorized - The request requires user authentication or, if the request included authorization credentials, authorization has been refused for those credentials.                                                              | | 403         | Forbidden - The server understood the request, but is refusing to fulfill it.                                                                                                                                                     | | 404         | Not Found - The requested resource could not be found. This error can be due to a temporary or permanent condition.                                                                                                               | | 429         | Too Many Requests - Rate limiting has been applied.                                                                                                                                                                               | | 500         | Internal Server Error. You should never receive this error because our clever coders catch them all ... but if you are unlucky enough to get one, please report it to us through a comment at the bottom of this page.            | | 502         | Bad Gateway - The server was acting as a gateway or proxy and received an invalid response from the upstream server.                                                                                                              | | 503         | Service Unavailable - The server is currently unable to handle the request due to a temporary condition which will be alleviated after some delay. You can choose to resend the request again.                                    |  # Rate limiting To make the API fast for everybody, rate limits apply.  Rate limiting is applied on an application basis (based on client id), regardless of how many users are using it.  If you get status code 429, it means that you have sent too many requests. If this happens, have a look in the Retry-After header, where you will see a number displayed. This is the amount of seconds that you need to wait, before you can retry sending your requests.  You can check the returned HTTP headers of any API request to see your current rate limit status:  ``` curl -i https://api.facestore.pt/v1/sample HTTP/1.1 200 OK Date: Mon, 01 Dec 2016 17:27:06 GMT Status: 200 OK X-RateLimit-Limit: 60 X-RateLimit-Remaining: 56 X-RateLimit-Reset: 1372700873 ```  The headers tell you everything you need to know about your current rate limit status:  | HEADER NAME           | DESCRIPTION                                                                     | |:---------------------:|:-------------------------------------------------------------------------------:| | X-RateLimit-Limit   | The maximum number of requests that the consumer is permitted to make per hour. | | X-RateLimit-Remaining | The number of requests remaining in the current rate limit window.              | | X-RateLimit-Reset   | The time at which the current rate limit window resets in UTC epoch seconds.    |  # Timestamps Timestamps are returned in ISO 8601 format as Coordinated Universal Time (UTC) with zero offset: YYYY-MM-DDTHH:MM:SSZ. If the time is imprecise (for example, the date/time of an product is created), an additional field will show the precision; see for example, created_at in an product object.  # Error Details The API uses the following format to describe unsuccessful responses, return information about the error as an error JSON object containing the following information::  | KEY         | VALUE TYPE   | VALUE DESCRIPTION | |:-----------:|:------------:|:-----------------:| | status_code | integer    | The HTTP status code (also returned in the response header; see Response Status Codes for more information). | | message     | string     | A short description of the cause of the error. |   # noqa: E501

    OpenAPI spec version: 0.1.4
    Contact: apihelp@facestore.pt
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.i18n import I18n  # noqa: F401,E501


class Brand(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'position': 'int',
        'image_small': 'str',
        'image_larger': 'str',
        'active': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'visibility': 'list[str]',
        'i18n': 'list[I18n]'
    }

    attribute_map = {
        'id': 'id',
        'position': 'position',
        'image_small': 'image_small',
        'image_larger': 'image_larger',
        'active': 'active',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'visibility': 'visibility',
        'i18n': 'i18n'
    }

    def __init__(self, id=None, position=None, image_small=None, image_larger=None, active=None, created_at=None, updated_at=None, visibility=None, i18n=None):  # noqa: E501
        """Brand - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._position = None
        self._image_small = None
        self._image_larger = None
        self._active = None
        self._created_at = None
        self._updated_at = None
        self._visibility = None
        self._i18n = None
        self.discriminator = None

        self.id = id
        if position is not None:
            self.position = position
        if image_small is not None:
            self.image_small = image_small
        if image_larger is not None:
            self.image_larger = image_larger
        if active is not None:
            self.active = active
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if visibility is not None:
            self.visibility = visibility
        if i18n is not None:
            self.i18n = i18n

    @property
    def id(self):
        """Gets the id of this Brand.  # noqa: E501


        :return: The id of this Brand.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Brand.


        :param id: The id of this Brand.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def position(self):
        """Gets the position of this Brand.  # noqa: E501


        :return: The position of this Brand.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Brand.


        :param position: The position of this Brand.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def image_small(self):
        """Gets the image_small of this Brand.  # noqa: E501


        :return: The image_small of this Brand.  # noqa: E501
        :rtype: str
        """
        return self._image_small

    @image_small.setter
    def image_small(self, image_small):
        """Sets the image_small of this Brand.


        :param image_small: The image_small of this Brand.  # noqa: E501
        :type: str
        """

        self._image_small = image_small

    @property
    def image_larger(self):
        """Gets the image_larger of this Brand.  # noqa: E501


        :return: The image_larger of this Brand.  # noqa: E501
        :rtype: str
        """
        return self._image_larger

    @image_larger.setter
    def image_larger(self, image_larger):
        """Sets the image_larger of this Brand.


        :param image_larger: The image_larger of this Brand.  # noqa: E501
        :type: str
        """

        self._image_larger = image_larger

    @property
    def active(self):
        """Gets the active of this Brand.  # noqa: E501


        :return: The active of this Brand.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Brand.


        :param active: The active of this Brand.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def created_at(self):
        """Gets the created_at of this Brand.  # noqa: E501


        :return: The created_at of this Brand.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Brand.


        :param created_at: The created_at of this Brand.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Brand.  # noqa: E501


        :return: The updated_at of this Brand.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Brand.


        :param updated_at: The updated_at of this Brand.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def visibility(self):
        """Gets the visibility of this Brand.  # noqa: E501

        channels that resource are showed  # noqa: E501

        :return: The visibility of this Brand.  # noqa: E501
        :rtype: list[str]
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this Brand.

        channels that resource are showed  # noqa: E501

        :param visibility: The visibility of this Brand.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["facebook", "mobile", "webstore", "none", "all"]  # noqa: E501
        if not set(visibility).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `visibility` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(visibility) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._visibility = visibility

    @property
    def i18n(self):
        """Gets the i18n of this Brand.  # noqa: E501

        I18n fields to brands  # noqa: E501

        :return: The i18n of this Brand.  # noqa: E501
        :rtype: list[I18n]
        """
        return self._i18n

    @i18n.setter
    def i18n(self, i18n):
        """Sets the i18n of this Brand.

        I18n fields to brands  # noqa: E501

        :param i18n: The i18n of this Brand.  # noqa: E501
        :type: list[I18n]
        """

        self._i18n = i18n

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Brand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
