import pytest
from fixture.application import Application


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.navigation.open_home_page()
    fixture.session.login(login="admin", password="secret")
    request.addfinalizer(fixture.destroy)
    return fixture