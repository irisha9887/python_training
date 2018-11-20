from model.contact import Contact


def test_delete_group_from_contact(app, db, json_contacts, orm):
    app.navigation.open_home_page()
    app.contact.open_group_page_with_its_contact(orm)
    selected_group = app.contact.open_group_page_with_its_contact(orm)
    old_contacts_from_group_page = orm.get_contacts_in_group(selected_group)
    contact = Contact(firstname="Ekaterina", middlename="E.Smithes", lastname="Smithes", nickname="Cat", photo="/Users/i.mamutkina/Desktop/photo.png", title="Manager",
            company="Facebook", address="13 Main str, 9 apr, SF", home="1122334455", mobile="33221166554", work="99887744556",
            fax="fax-745-126-789", email="cat_1@gmail.com", email2="cat_2@gmail.com", email3="cat_3@gmail.com", homepage="Changed homepage",
            bday="10", bmonth="April", byear="1998", aday="19", amonth="December", ayear="1999", address2="123 Main str, 40 apr, San Carlos",
            phone2="385263354", notes="New changed notes!")
    if len(old_contacts_from_group_page) == 0:
        app.contact.add_group_to_contact(contact, db)
    app.contact.delete_group_from_contact(orm)
    app.contact.open_group_page_with_its_contact(orm)
    new_contacts_from_group_page = orm.get_contacts_in_group(selected_group)
    assert len(old_contacts_from_group_page) - 1 == len(new_contacts_from_group_page)

