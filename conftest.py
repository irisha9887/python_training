import pytest
from fixture.application import Application

fixture =  None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.navigation.open_home_page()
        fixture.session.login(login="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.navigation.open_home_page()
            fixture.session.login(login="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture