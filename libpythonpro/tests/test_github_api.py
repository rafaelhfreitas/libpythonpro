from unittest import TestCase
from libpythonpro import github_api



def test_get_avatar():
    url = github_api.get_avatar('rafaelhfreitas')
    assert 'https://avatars3.githubusercontent.com/u/21064382?v=4' == url


# class TestGitHubApi(TestCase):
#     def test_get_avatar(self):
#         user = 'rafaelhfreitas'
#
#         url_received = github_api.get_avatar(user)
#         url_expected = "https://avatars3.githubusercontent.com/u/21064382?v=4"
#
#         self.assertEqual(url_expected, url_received)
#
#     def test_init(self):
#         assert 1 == 1
