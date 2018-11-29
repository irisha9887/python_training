from model.group import Group
import random
import allure


def test_delete_some_group(app, db, check_ui):
    with allure.step('Given Home page is opened'):
        app.group.open_groups_page()
    with allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="Test group for deleting"))
    old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I delete the group %s from the list' % group.id):
        app.group.delete_group_by_id(group.id)
    with allure.step('Then the new group list is equal to the old list group without the deleted group'):
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == len(new_groups)
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            groups_name_from_db = db.get_list_of_groups_names_and_ids()
            assert sorted(groups_name_from_db, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



