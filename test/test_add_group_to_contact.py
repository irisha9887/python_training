from model.contact import Contact
from model.group import Group


def test_add_group_to_contact(app, db, json_contacts, orm):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group for adding contact"))
    contact = json_contacts
    app.contact.open_group_page_with_its_contact(orm)
    selected_group = app.contact.open_group_page_with_its_contact(orm)
    old_contacts_from_group_page = orm.get_contacts_in_group(selected_group)
    app.contact.add_group_to_contact(contact, db)
    app.contact.open_group_page_with_its_contact(orm)
    new_contacts_from_group_page = orm.get_contacts_in_group(selected_group)
    assert len(old_contacts_from_group_page) + 1 == len(new_contacts_from_group_page)





