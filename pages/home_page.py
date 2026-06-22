class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://example.com")

    def get_title(self):
        return self.page.title()
