# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.login(login="admin", password="secret")
    app.create_group(Group(name="New group", header="Header", footer="Footer"))
    app.logout()


def test_add_empty_group(app):
    app.open_home_page()
    app.login(login="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()


