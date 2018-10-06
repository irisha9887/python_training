from model.contact import Contact


def test_modify_group(app):
    app.navigation.open_home_page()
    app.sessoin.login(login="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Ekaterina", middlename="E.Smithes", lastname="Smithes", nickname="Cat", photo="/Users/i.mamutkina/Desktop/photo.png", title="Manager",
                               company="Facebook", address="13 Main str, 9 apr, SF", home="1122334455", mobile="33221166554", work="99887744556",
                               fax="fax-745-126-789", email="cat_1@gmail.com", email2="cat_2@gmail.com", email3="cat_3@gmail.com", homepage="Changed homepage",
                               bday="10", bmonth="April", byear="1998", aday="19", amonth="December", ayear="1999", address2="123 Main str, 40 apr, San Carlos",
                               phone2="385263354", notes="New changed notes!"))
    app.navigation.open_home_page()
    app.sessoin.logout()

