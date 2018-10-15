from model.group import Group


def test_modify_first_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.open_groups_page()
    if app.group.count == 0:
        app.group.create(Group(name="Test group for modifying"))
    app.group.modify_first_group(Group(name="New group name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_first_group_header(app):
    old_groups = app.group.get_group_list()
    app.group.open_groups_page()
    if app.group.count == 0:
        app.group.create(Group(name="Test group for modifying"))
    app.group.modify_first_group(Group(header="New header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

