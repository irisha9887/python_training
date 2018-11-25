#Сценарий превращается в шаблон со словом Outline
Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
  |name       |header      |footer|
  |Work group |Work header |Work footer|
  |Dance group|Dance header|Dance footer|

Scenario: Delete a group
  Given a non-empty group list
  Given a random group from the list
  When I delete the group from the list
  Then the new group list is equal to the old list group without the deleted group

