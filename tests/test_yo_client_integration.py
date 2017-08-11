from unittest import TestCase

import os
from dotenv import load_dotenv, find_dotenv
from yo_client import YoClient, Coordinate

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

    def test_sending_yo_with_link(self):
        client = YoClient(api_key=API_KEY)
        result = client.send_yo(username=TEST_USERNAME, link="http://example.com")
        self.assertIsNotNone(result)
        self.assertIn("success", result)
        self.assertIn("yo_id", result)
        self.assertTrue(result["success"])
        self.assertIsNotNone(result["yo_id"])

    def test_sending_yo_with_location(self):
        coordinate = Coordinate(latitude=0, longitude=0)
        client = YoClient(api_key=API_KEY)
        result = client.send_yo(username=TEST_USERNAME, coordinate=coordinate)
        self.assertIsNotNone(result)
        self.assertIn("success", result)
        self.assertIn("yo_id", result)
        self.assertTrue(result["success"])
        self.assertIsNotNone(result["yo_id"])


class GetSubscribersCountIntegrationTest(TestCase):
    def test_getting_subscribers_count(self):
        client = YoClient(api_key=API_KEY)
        count = client.get_subscribers_count()
        self.assertIsNotNone(count)
        self.assertTrue(count["count"] > 0)


class UsernameExistsIntegrationTest(TestCase):
    def test_username_exists(self):
        client = YoClient(api_key=API_KEY)
        self.assertTrue(client.username_exists(username=TEST_USERNAME))
