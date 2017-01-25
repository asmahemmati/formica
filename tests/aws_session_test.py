import unittest
from unittest.mock import patch, Mock

from formica.aws_session import AWSSession
from tests.test_constants import REGION, PROFILE


@patch('boto3.session.Session')
class AWSClientTest(unittest.TestCase):
    def test_init_with_region(self, session):
        AWSSession()
        session.assert_called_with()

    def test_init_with_region(self, session):
        AWSSession(region=REGION)
        session.assert_called_with(region_name=REGION)

    def test_init_with_profile(self, session):
        AWSSession(profile=PROFILE)
        session.assert_called_with(profile_name=PROFILE)

    def test_init_with_profile_and_region(self, session):
        AWSSession(profile=PROFILE, region=REGION)
        session.assert_called_with(profile_name=PROFILE, region_name=REGION)

    def test_client_for_returns_client(self, session):
        aws_session = AWSSession()
        client_mock = Mock()

        session.return_value.client.return_value = client_mock
        client = aws_session.client_for('s3')

        session.return_value.client.assert_called_with('s3')
        self.assertEquals(client_mock, client)
