# coding: utf-8

"""
    UrlShortener API

    Description  # noqa: E501

    OpenAPI spec version: v1
    Contact: gagarinovdaniil@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.manage_api import ManageApi  # noqa: E501
from swagger_client.api.detail_api import DetailApi
from swagger_client.rest import ApiException


class TestManageApi(unittest.TestCase):
    """ManageApi unit test stubs"""

    def setUp(self):
        configuration = swagger_client.Configuration()
        configuration.username = 'yaishenka'
        configuration.password = 'root'
        self.api = swagger_client.api.manage_api.ManageApi(swagger_client.ApiClient(configuration))  # noqa: E501
        self.detail_api = swagger_client.api.detail_api.DetailApi(swagger_client.ApiClient(configuration))  # noqa: E501

    def tearDown(self):
        self.detail_api.detail_delete(short_url='test')

    def test_manage_create(self):
        data = {'full_url': 'full_test', 'short_url': 'test'}
        self.api.manage_create(data)

    def test_manage_list(self):
        data = {'full_url': 'full_test', 'short_url': 'test'}
        self.api.manage_create(data)
        url_list = self.api.manage_list()
        url = url_list[0]
        self.assertTrue(url.short_url == 'test')


if __name__ == '__main__':
    unittest.main()