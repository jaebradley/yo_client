from unittest import TestCase

import os
from dotenv import load_dotenv, find_dotenv
from yo_client.yo_client import YoClient

load_dotenv(find_dotenv())

API_KEY=os.environ.get("API_KEY")
TEST_USERNAME=os.environ.get("TEST_USERNAME")


class SendYoIntegrationTest(TestCase):
    def test_sending_yo_without_arguments(self):
        client = YoClient(api_key=API_KEY)
        result = client.send_yo(username=TEST_USERNAME)
        self.assertIsNotNone(result)
        self.assertIn("success", result)
        self.assertIn("yo_id", result)
        self.assertTrue(result["success"])
        self.assertIsNotNone(result["yo_id"])
