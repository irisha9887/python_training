from model.group import Group


def test_modify_group(app):
    app.navigation.open_home_page()
    app.session.login(login="admin", password="secret")
    app.group.open_groups_page()
    app.group.modify_first_group(Group(name="Changed group name", header="Changed header", footer="Changed footer"))
    app.session.logout()
