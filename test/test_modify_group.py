from model.group import Group


def test_modify_group(app):
    app.navigation.open_home_page()
    # app.sessoin.login(login="admin", password="secret")
    app.group.open_groups_page()
    app.group.modify_first_group(Group(name="Changed group name", header="Changed header", footer="Changed footer"))
    app.sessoin.logout()


def test_modify_name(app):
    app.navigation.open_home_page()
    # app.sessoin.login(login="admin", password="secret")
    app.group.open_groups_page()
    app.group.modify_first_group(Group(name="New group name"))
    app.sessoin.logout()


def test_modify_header(app):
    app.navigation.open_home_page()
    # app.sessoin.login(login="admin", password="secret")
    app.group.open_groups_page()
    app.group.modify_first_group(Group(header="New header"))
    app.sessoin.logout()
