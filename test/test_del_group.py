
def test_delete_first_group(app):
    app.navigation.open_home_page()
    app.session.login(login="admin", password="secret")
    app.group.open_groups_page()
    app.group.delete_first_group()
    app.session.logout()