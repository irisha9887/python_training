from model.group import Group


def test_modify_first_group_name(app):
    app.group.open_groups_page()
    if app.group.count == 0:
        app.group.create(Group(name="Test group for modifying"))
    app.group.modify_first_group(Group(name="New group name"))


def test_modify_first_group_header(app):
    app.group.open_groups_page()
    if app.group.count == 0:
        app.group.create(Group(name="Test group for modifying"))
    app.group.modify_first_group(Group(header="New header"))

