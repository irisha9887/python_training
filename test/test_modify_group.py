from model.group import Group
from random import randrange
import random


#def test_modify_group_name(app):
    #app.group.open_groups_page()
    #if app.group.count() == 0:
    #app.group.create(Group(name="Test group for modifying"))
    #old_groups = app.group.get_group_list()
    #index = randrange(len(old_groups))
    #group = Group(name="New group name")
    #group.id = old_groups[index].id
    #app.group.modify_group_by_index(index, group)
    #assert len(old_groups) == app.group.count()
    #new_groups = app.group.get_group_list()
    #old_groups[index] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_name(app, db, check_ui):
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Test group for modifying"))
    old_groups = db.get_group_list()
    #id = random.choice(old_groups)
    index = randrange(len(old_groups))
    group = Group(name="New group name")
    group.id = old_groups[index].id
    app.group.modify_group_by_id(id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    new_groups = db.get_group_list()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)














