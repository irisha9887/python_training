# -*- coding: utf-8 -*-
from model.group import Group
import pytest


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('When I add a group %s to the list' % group):
        app.group.open_groups_page()
        app.group.create(group)
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert old_groups == new_groups
        if check_ui:
            groups_name_from_db = db.get_list_of_groups_names_and_ids()
            assert sorted(groups_name_from_db, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

















