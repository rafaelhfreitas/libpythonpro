from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/21064382?v=4'
    resp_mock.json.return_value = {
        'login': 'rafaelhfreitas',
        'id': 21064382,
        'avatar_url': url
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value=resp_mock
    return url


def test_get_avatar(avatar_url):
    url = github_api.get_avatar('rafaelhfreitas')
    assert avatar_url == url


def test_get_avatar_integration():
    url = github_api.get_avatar('rafaelhfreitas')
    assert 'https://avatars3.githubusercontent.com/u/21064382?v=4' == url
