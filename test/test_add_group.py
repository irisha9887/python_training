# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.navigation.open_home_page()
    app.session.login(login="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="New group", header="Header", footer="Footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.navigation.open_home_page()
    app.session.login(login="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()



