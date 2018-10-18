# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

def test_add_contact(app):
    app.navigation.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.navigation.open_edit_page()
    contact = Contact(firstname="Kate", middlename="K.Smith", lastname="Smith", nickname="Katty", photo="/Users/i.mamutkina/Desktop/photo.png", title="Dev",
                               company="Google", address="12 Main str, 5 apr, Menlo park", home="123456789", mobile="123456788", work="12346777",
                               fax="fax-123-456-789", email="kate1@gmail.com", email2="kate2@gmail.com", email3="kate3@gmail.com", homepage="Test homepage",
                               bday="12", bmonth="May", byear="1990", aday="17", amonth="June", ayear="1995", address2="10 Main str, 8 apr, Fremont",
                               phone2="987654321", notes="Have a good day! Well done!")
    app.contact.create(contact)
    app.navigation.open_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    app.navigation.open_home_page()
#    old_contacts = app.contact.get_contact_list()
#    app.navigation.open_edit_page()
#    contact = Contact(firstname="", middlename="", lastname="", nickname="", photo="/Users/i.mamutkina/Desktop/photo.png", title="", company="", address="", home="", mobile="", work="",
#                               fax="", email="", email2="", email3="", homepage="", bday="", bmonth="May", byear="", aday="", amonth="June", ayear="", address2="", phone2="", notes="")
#    app.contact.create(contact)
#    app.navigation.open_home_page()
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == app.contact.count()
#    old_contacts.append(contact)
#   assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


