from model.contact import Contact
from model.group import Group
import random


def test_delete_group_from_contact(app, orm):
    app.navigation.open_home_page()
    # Get group list from DB
    group_list = orm.get_group_list()
    # If group list is empty, then add new group
    if len(group_list) == 0:
        app.group.open_groups_page()
        app.group.create(Group(name="Group for adding contact"))
    # Get again group list because it could be changed after if conditions
    new_group_list = orm.get_group_list()
    # Get contact list from random selected group
    selected_group = random.choice(new_group_list)
    contacts_in_group = orm.get_contacts_in_group(selected_group)
    # Get count of contacts which are inside selected group
    count_contacts_in_group_before_deleting_contact = len(contacts_in_group)
    if len(contacts_in_group) == 0:
        app.navigation.open_edit_page()
        app.contact.create(
            Contact(firstname="Ekaterina", middlename="E.Smithes", lastname="Smithes", nickname="Cat",
                    photo="/Users/i.mamutkina/Desktop/photo.png", title="Manager",
                    company="Facebook", address="13 Main str, 9 apr, SF", home="1122334455", mobile="33221166554",
                    work="99887744556",
                    fax="fax-745-126-789", email="cat_1@gmail.com", email2="cat_2@gmail.com",
                    email3="cat_3@gmail.com", homepage="Changed homepage",
                    bday="10", bmonth="April", byear="1998", aday="19", amonth="December", ayear="1999",
                    address2="123 Main str, 40 apr, San Carlos",
                    phone2="385263354", notes="New changed notes!"))
    new_contact_list = orm.get_contacts_in_group(selected_group)
    # Choose one random contact from this list
    #app.navigation.open_home_page(?group=selected_group id)
    selected_contact = random.choice(new_contact_list)
    #app.navigation.open_home_page( http: // localhost / addressbook / index.php?group = 306
    #wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
    app.contact.delete_group_from_contact(selected_contact.id)





#def test_delete_group_from_contact(app, db, json_contacts, orm):
    #app.navigation.open_home_page()
    #app.contact.open_group_page_with_its_contact(orm)
    #selected_group = app.contact.open_group_page_with_its_contact(orm)
    #old_contacts_from_group_page = orm.get_contacts_in_group(selected_group)
    #contact = Contact(firstname="Ekaterina", middlename="E.Smithes", lastname="Smithes", nickname="Cat", photo="/Users/i.mamutkina/Desktop/photo.png", title="Manager",
            #company="Facebook", address="13 Main str, 9 apr, SF", home="1122334455", mobile="33221166554", work="99887744556",
            #fax="fax-745-126-789", email="cat_1@gmail.com", email2="cat_2@gmail.com", email3="cat_3@gmail.com", homepage="Changed homepage",
            #bday="10", bmonth="April", byear="1998", aday="19", amonth="December", ayear="1999", address2="123 Main str, 40 apr, San Carlos",
            #phone2="385263354", notes="New changed notes!")
    #if len(old_contacts_from_group_page) == 0:
        #app.contact.add_group_to_contact(contact, db)
    #app.contact.delete_group_from_contact(orm)
    #app.contact.open_group_page_with_its_contact(orm)
    #new_contacts_from_group_page = orm.get_contacts_in_group(selected_group)
    #assert len(old_contacts_from_group_page) - 1 == len(new_contacts_from_group_page)

