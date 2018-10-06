class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

    def open_edit_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/edit.php")