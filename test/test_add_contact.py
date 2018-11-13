# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    app.navigation.open_home_page()
    old_contacts = db.get_contact_list()
    app.navigation.open_edit_page()
    app.contact.create(contact)
    app.navigation.open_home_page()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    if check_ui:
        contact_list = db.get_contact_list_with_merged_emails_and_phones()
        assert sorted(contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)






