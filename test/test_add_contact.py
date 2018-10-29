# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
import random
import string
import calendar


def random_strings_for_text_fields(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_strings_for_phones(maxlen):
    symbols = string.digits + "(" + ")" + "+" + "-"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_strings_for_year_field():
    symbols = string.digits[0:2050]
    return random.choice(symbols)


def random_month():
    return random.choice(calendar.month_name)


def random_day_of_month():
    symbols = string.digits[1:31]
    return random.choice(symbols)


def random_photo_from_list():
    list_of_photo = ["/Users/i.mamutkina/Desktop/photo1.png", "/Users/i.mamutkina/Desktop/photo2.png", "/Users/i.mamutkina/Desktop/photo3.png"]
    return random.choice(list_of_photo)

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", photo=random_photo_from_list(),
    title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="",
    email3="", homepage="", bday="", bmonth="May", byear="", aday="", amonth="June", ayear="",
    address2="", phone2="",notes="")] + [Contact(firstname=random_strings_for_text_fields("name", 7),
    middlename=random_strings_for_text_fields("middlename", 7), lastname=random_strings_for_text_fields("lastname", 7),
    nickname=random_strings_for_text_fields("nick", 10), photo=random_photo_from_list(),
    title=random_strings_for_text_fields("title", 10), company=random_strings_for_text_fields("company", 10),
    address=random_strings_for_text_fields("address", 20), home=random_strings_for_phones(20),
    mobile=random_strings_for_phones(15), work=random_strings_for_phones(15),
    fax=random_strings_for_phones(15), email=random_strings_for_text_fields("email", 12),
    email2=random_strings_for_text_fields("email2", 12), email3=random_strings_for_text_fields("email3", 12),
    homepage=random_strings_for_text_fields("Homepage", 10),bday=random_day_of_month(), bmonth=random_month(),
    byear=random_strings_for_year_field(), aday=random_day_of_month(), amonth=random_month(),
    ayear=random_strings_for_year_field(), address2=random_strings_for_text_fields("address2", 15),
    phone2=random_strings_for_phones(20), notes=random_strings_for_text_fields("notes", 50))
    for name in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    app.navigation.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.navigation.open_edit_page()
    app.contact.create(contact)
    app.navigation.open_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


