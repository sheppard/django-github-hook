from django.test import TestCase
from github_hook.models import Hook
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
        self.bitbucket_payload = json.load(open('tests/bitbucket.json'))

    def test_plain_post(self):
        response = self.client.post('/')
        # Post without payload or name is invalid
        self.assertFalse(status.is_success(response.status_code))

    def test_named_post(self):
        self.reset_log()
        # Named post should work
        response = self.client.post('/test')
        self.assertTrue(status.is_success(response.status_code))
        self.check_log()

    def test_github_post(self):
        self.reset_log()
        # Payload post should work
        data = {"payload": json.dumps(self.github_payload)}
        response = self.client.post('/', data)
        self.assertTrue(status.is_success(response.status_code))
        self.check_log()

    def test_bitbucket_post(self):
        self.reset_log()
        # Payload post should work
        data = {"payload": json.dumps(self.bitbucket_payload)}
        response = self.client.post('/', data)
        self.assertTrue(status.is_success(response.status_code))
        self.check_log()

    def test_get(self):
        response = self.client.get('/')
        # GET is not valid
        self.assertFalse(status.is_success(response.status_code))

    def reset_log(self):
        f = open('tests/test.log', 'w')
        f.write("")
        f.close()

    def check_log(self):
        data = open('tests/test.log').read()
        self.assertEqual(data, "Hello")
