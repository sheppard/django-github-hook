from django.test import TestCase
from github_hook.models import Hook, hook_signal
from rest_framework import status
import json


class GithubHookTestCase(TestCase):
    def setUp(self):
        Hook.objects.create(
            name='test',
            user='user',
            repo='test',
            path='tests/test.sh',
        )
        self.github_payload = json.load(open('tests/github.json'))
        self.github_payload2 = json.load(open('tests/github2.json'))
        self.bitbucket_payload = json.load(open('tests/bitbucket.json'))

    def test_plain_post(self):
        """
        POST without payload or name is invalid
        """
        response = self.client.post('/')
        self.assertFalse(status.is_success(response.status_code))

    def test_named_post(self):
        """
        POST with valid name (url slug) should work.
        """
        self.reset_log()
        response = self.client.post('/test')
        self.assertTrue(status.is_success(response.status_code))
        self.check_log()

    def test_github_post(self):
        """
        POST with valid Github-style form payload should work.
        """
        self.reset_log()
        data = {"payload": json.dumps(self.github_payload)}
        response = self.client.post('/', data)
        self.assertTrue(status.is_success(response.status_code))
        self.check_log()

    def test_github_json(self):
        """
        POST with valid Github-style JSON payload should work.
        """
        self.reset_log()
        data = json.dumps(self.github_payload)
        response = self.client.post('/', data, content_type="application/json")
        self.assertTrue(status.is_success(response.status_code))
        self.check_log()

    def test_github_signal(self):
        """
        POST with valid payload but unknown user/repo should trigger signal.
        """
        def test_fn(sender, **kwargs):
            self.write_log()
        hook_signal.connect(test_fn)

        self.reset_log()
        data = json.dumps(self.github_payload2)
        response = self.client.post('/', data, content_type="application/json")
        self.assertTrue(status.is_success(response.status_code))
        self.check_log()

    def test_bitbucket_post(self):
        """
        POST with valid Bitbucket-style form payload should work.
        """
        self.reset_log()
        data = {"payload": json.dumps(self.bitbucket_payload)}
        response = self.client.post('/', data)
        self.assertTrue(status.is_success(response.status_code))
        self.check_log()

    def test_get(self):
        """
        GET should not work.
        """
        response = self.client.get('/')
        self.assertFalse(status.is_success(response.status_code))
        response = self.client.get('/test')
        self.assertFalse(status.is_success(response.status_code))

    def reset_log(self):
        self.write_log("")

    def write_log(self, value="Hello"):
        f = open('tests/test.log', 'w')
        f.write(value)
        f.close()

    def check_log(self, value="Hello"):
        f = open('tests/test.log')
        data = f.read()
        f.close()
        self.assertEqual(data, value)
