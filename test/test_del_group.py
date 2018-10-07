from model.group import Group

def test_delete_first_group(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="Test group for deleting"))
    app.group.delete_first_group()