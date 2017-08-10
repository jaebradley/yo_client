from unittest import TestCase

from yo_client.request_parameters import RequestBodyBuilder, RequestQueryParametersBuilder


class MockCoordinate:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


class TestRequestBodyBuilder(TestCase):
    def test_build_send_yo_body_without_coordinate(self):
        username = "foo"
        api_token = "bar"
        expected = {
            "username": username,
            "api_token": api_token,
            "text": None,
            "link": None
        }
        self.assertEqual(expected, RequestBodyBuilder.build_send_yo_body(username=username, api_token=api_token))

    def test_build_send_yo_body_with_coordinate(self):
        username = "foo"
        api_token = "bar"
        latitude = "fizz"
        longitude = "buzz"
        coordinate = MockCoordinate(latitude=latitude, longitude=longitude)
        expected = {
            "username": username,
            "api_token": api_token,
            "text": None,
            "link": None,
            "location": "fizz,buzz"
        }
        self.assertEqual(expected, RequestBodyBuilder.build_send_yo_body(username=username, api_token=api_token, coordinate=coordinate))

    def test_build_send_yo_to_all_subscribers_body(self):
        api_token = "foo"
        expected = {
            "api_token": api_token,
            "link": None
        }
        self.assertEqual(expected, RequestBodyBuilder.build_send_yo_to_all_subscribers_body(api_token=api_token))

    def test_build_account_creation_body(self):
        api_token = "foo"
        username = "bar"
        expected = {
            "username": username,
            "api_token": api_token,
            "password": None,
            "callback_url": None,
            "email": None,
            "description": None,
            "needs_location": False,
            "welcome_link": None
        }
        self.assertEqual(expected, RequestBodyBuilder.build_account_creation_body(username=username, api_token=api_token))


class TestRequestQueryParameterBuilder(TestCase):
    def test_build_username_exists_query_parameters(self):
        api_token = "foo"
        username = "bar"
        expected = {
            "api_token": api_token,
            "username": username
        }
        self.assertEqual(expected, RequestQueryParametersBuilder.build_username_exists_query_parameters(username=username, api_token=api_token))