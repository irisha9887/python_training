import pytest
from model.contact import Contact
import random
import string
import calendar
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_strings_for_text_fields(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_strings_for_phones(maxlen):
    symbols = string.digits + "(" + ")" + "+" + "-"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_strings_for_year_field():
    symbols = range(1980, 2050)
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
    email3="", homepage="", bday="6", bmonth="May", byear="", aday="5", amonth="June", ayear="",
    address2="", phone2="",notes="")] + [Contact(firstname=random_strings_for_text_fields("name", 20),
    middlename=random_strings_for_text_fields("middlename", 20), lastname=random_strings_for_text_fields("lastname", 20),
    nickname=random_strings_for_text_fields("nick", 30), photo=random_photo_from_list(),
    title=random_strings_for_text_fields("title", 30), company=random_strings_for_text_fields("company", 30),
    address=random_strings_for_text_fields("address", 50), home=random_strings_for_phones(30),
    mobile=random_strings_for_phones(30), work=random_strings_for_phones(30),
    fax=random_strings_for_phones(30), email=random_strings_for_text_fields("email", 35),
    email2=random_strings_for_text_fields("email2", 35), email3=random_strings_for_text_fields("email3", 35),
    homepage=random_strings_for_text_fields("Homepage", 40),bday=random_day_of_month(), bmonth=random_month(),
    byear=random_strings_for_year_field(), aday=random_day_of_month(), amonth=random_month(),
    ayear=random_strings_for_year_field(), address2=random_strings_for_text_fields("address2", 35),
    phone2=random_strings_for_phones(30), notes=random_strings_for_text_fields("notes", 70))
    for name in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
