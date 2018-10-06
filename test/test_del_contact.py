
def test_delete_first_contact(app):
    app.navigation.open_home_page()
    app.session.login(login="admin", password="secret")
    app.navigation.open_home_page()
    app.contact.delete_first_contact()
    app.session.logout()

