"""
    Bloopy

    The Bloopy server API documentation  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import whsaas.openapi_client
from whsaas.openapi_client.api.health_api import HealthApi  # noqa: E501


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_api_v1_health_get(self):
        """Test case for health_api_v1_health_get

        Health  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
