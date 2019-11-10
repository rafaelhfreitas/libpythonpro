from libpythonpro import github_api


def test_get_avatar():
    url = github_api.get_avatar('rafaelhfreitas')
    assert 'https://avatars3.githubusercontent.com/u/21064382?v=4' == url
