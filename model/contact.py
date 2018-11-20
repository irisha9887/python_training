from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo=None, title=None, company=None, address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None,
                 email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, new_group=None, address2=None, phone2=None, notes=None, id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.new_group = new_group
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s%s:%s:%s:%s%s:%s:%s:%s%s:%s:%s:%s%s:%s:%s:%s%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.middlename, self.firstname,
                                                                                          self.nickname, self.title, self.company, self.address, self.photo,
                                                                                          self.home, self.mobile, self.work, self.fax, self.email,
                                                                                          self.email2, self.email3, self.homepage, self.bday,
                                                                                          self.bmonth, self.byear, self.aday, self.amonth,
                                                                                          self.ayear, self.address2, self.phone2, self.notes)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and\
                self.firstname == other.firstname and self.middlename == other.middlename and self.address == other.address and\
                self.nickname == other.nickname and self.title == other.title and self.company == other.company and\
                self.photo == other.photo, self.home == other.home and self.mobile == other.mobile and\
                self.work == other.work and self.fax == other.fax and self.email == other.email and self.email2 == other.email2 and\
                self.email3 == other.email3 and self.homepage == other.homepage and self.bday == other.bday and\
                self.bmonth == other.bmonth and self.byear == other.byear  and\
                self.address2 == other.address2 and self.phone2 == other.phone2 and self.notes == other.notes

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize




