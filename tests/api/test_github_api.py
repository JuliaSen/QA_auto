import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user ['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 25
    assert r['total_count'] == r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_status_code200(github_api):
    r = github_api.check_status_code()
    assert r.status_code == 200

   
@pytest.mark.api
def test_list_emojis_not_empty(github_api):
    r = github_api.check_empty_list_emojis()
    assert len(r) > 2

@pytest.mark.api
def test_search_emoji_wolf(github_api):
    r = github_api.check_empty_list_emojis()
    assert "wolf" in r
    if "wolf" in r:
        print(True)
    else:
        print(False)