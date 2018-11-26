Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename>, <lastname>, <nickname>, <photo>, <title>, <company>, <address>, <home>, <mobile>, <work>, <fax>, <email>, <email2>, <email3>, <homepage>, <bday>, <bmonth>, <byear>, <aday>, <amonth>, <ayear>, <address2>, <phone2> and <notes>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  |firstname|middlename|lastname|nickname|photo                                |title|company|address               |home      |mobile     |work       |fax            |email           |email2          |email3          |homepage|bday|bmonth|byear|aday|amonth|ayear|address2                  |phone2     |notes         |
  |Inna     |I.M       |Kruz    |Ikruz   |/Users/i.mamutkina/Desktop/photo.png |BA   |Apple  |90 Main str, 1 apr, SF|1122334400|33221160911|33221161232|fax-567-111-767|inna_1@gmail.com|inna_2@gmail.com|inna_3@gmail.com|al.com  |1   |May   |1997 |1   |May   |2003 |12 Grog str, 57 apr, Brest|90761164090|Good person   |
  |Nik      |N.B       |Bronx   |BroN    |/Users/i.mamutkina/Desktop/photo1.png|Dev  |A1QA   |88 Toms str, 3 apr, SF|1189764455|23349066554|90761166554|fax-898-232-878|n1@gmail.com    |n2@gmail.com    |n3@gmail.com    |1k.by   |8   |April |1987 |12  |May   |1995 |3 Grog str, 4 apr, Minsk  |21331166554|My best friend|


#Scenario: Modify a contact
  #Given a non-empty contact list
  #Given a random contact from the list
  #When I modify the contact from the list
  #Then the new contact list is equal to the old contact list

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact