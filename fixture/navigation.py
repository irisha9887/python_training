import conftest

class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def open_edit_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("./edit.php")):
            wd.find_element_by_link_text("add new").click()

