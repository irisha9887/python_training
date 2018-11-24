from model.contact import Contact
from model.group import Group
import random
from random import randrange


def test_add_group_to_contact(app, orm):
    app.navigation.open_home_page()
    #Get group list from DB
    group_list = orm.get_group_list()
    if len(group_list) == 0:
        app.group.open_groups_page()
        app.group.create(Group(name="Group for adding contact"))
    new_group_list = orm.get_group_list()
    #Choose one random group from list
    selected_group = random.choice(new_group_list)
    #Get contact list where contacts aren't inside a group
    old_contacts = orm.get_contacts_not_in_group(selected_group)
    #Get a count of contacts before adding contact to group
    contacts_in_group = orm.get_contacts_in_group(selected_group)
    count_contacts_in_group_before_adding_contact = len(contacts_in_group)
    if len(old_contacts) == 0:
        app.navigation.open_edit_page()
        app.contact.create(Contact(firstname="Ekaterina", middlename="E.Smithes", lastname="Smithes", nickname="Cat", photo="/Users/i.mamutkina/Desktop/photo.png", title="Manager",
                               company="Facebook", address="13 Main str, 9 apr, SF", home="1122334455", mobile="33221166554", work="99887744556",
                               fax="fax-745-126-789", email="cat_1@gmail.com", email2="cat_2@gmail.com", email3="cat_3@gmail.com", homepage="Changed homepage",
                               bday="10", bmonth="April", byear="1998", aday="19", amonth="December", ayear="1999", address2="123 Main str, 40 apr, San Carlos",
                               phone2="385263354", notes="New changed notes!"))
    new_contact_list = orm.get_contacts_not_in_group(selected_group)
    #Choose one random contact from this list
    app.navigation.open_home_page()
    selected_contact = random.choice(new_contact_list)
    #Choose a group from list to add the selected contact
    app.group.select_group_from_group_list_on_home_page(selected_group.id)
    #Add the random selected contact to random group using contact id
    app.contact.add_group_to_contact(selected_contact.id)
    #Get a count of contacts after adding contact to group
    new_contacts = orm.get_contacts_in_group(selected_group)
    count_contacts_in_group_after_adding_contact = len(new_contacts)
    assert count_contacts_in_group_before_adding_contact + 1 == count_contacts_in_group_after_adding_contact


#def test_add_group_to_contact(app, db, json_contacts, orm):
    #app.group.open_groups_page()
    #if len(db.get_group_list()) == 0:
        #app.group.create(Group(name="Group for adding contact"))
    #contact = json_contacts
    #app.contact.open_group_page_with_its_contact(orm)
    #selected_group = app.contact.open_group_page_with_its_contact(orm)
    #old_contacts_from_group_page = orm.get_contacts_in_group(selected_group)
    #app.contact.add_group_to_contact(contact, db)
    #app.contact.open_group_page_with_its_contact(orm)
    #new_contacts_from_group_page = orm.get_contacts_in_group(selected_group)
    #assert len(old_contacts_from_group_page) + 1 == len(new_contacts_from_group_page)





