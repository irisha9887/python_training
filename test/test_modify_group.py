from model.group import Group


def test_modify_first_group_name(app):
    app.navigation.open_home_page()
    #app.session.login(login="admin", password="secret")
    app.group.modify_first_group(Group(name="New group name"))
    app.session.logout()

def test_modify_first_group_header(app):
    app.navigation.open_home_page()
    #app.session.login(login="admin", password="secret")
    app.group.modify_first_group(Group(header="New header"))
    app.session.logout()
