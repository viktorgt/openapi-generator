# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.model.order import Order


class TestOrder(unittest.TestCase):
    """Order unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrder(self):
        """Test Order"""
        order = Order()
        order.status = "placed"
        self.assertEqual("placed", order.status)
        with self.assertRaises(petstore_api.ApiValueError):
            order.status = "invalid"



if __name__ == '__main__':
    unittest.main()
