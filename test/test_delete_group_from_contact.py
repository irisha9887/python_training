from model.contact import Contact
from model.group import Group
import random


def test_delete_group_from_contact(app, orm):
    # If group list is empty, then add new group
    if len(orm.get_group_list()) == 0:
        app.group.open_groups_page()
        app.group.create(Group(name="Group for adding contact"))
    # Get again group list because it could be changed after if conditions
    group_list = orm.get_group_list()
    # Get contact list from random selected group
    selected_group = random.choice(group_list)
    if len(orm.get_contacts_in_group(selected_group)) == 0:
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
    contact_list = orm.get_contacts_in_group(selected_group)
    if len(contact_list) == 0:
        app.navigation.open_home_page()
        selected_contact = random.choice(orm.get_contact_list())
        app.contact.select_contact_by_id(selected_contact.id)
        app.contact.add_group_to_contact(selected_contact.id)
    # Get count of contacts which are inside selected group
    count_contacts_in_group_before_deleting_contact = len(contact_list)
    # Choose one random contact from this list
    selected_contact = random.choice(contact_list)
    app.contact.open_group_page_with_contacts(selected_group.name, selected_group.id)
    app.contact.delete_group_from_contact(selected_contact.id, selected_group.id)





