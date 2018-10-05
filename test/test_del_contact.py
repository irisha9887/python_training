
def test_delete_first_contact(app):
    app.navigation.open_home_page()
    #app.sessoin.login(login="admin", password="secret")
    app.contact.delete_first_contact()
    app.sessoin.logout()

