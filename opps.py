class Course:
    def __init__(self, title, hours, price):
        self.title = title
        self.hours = hours
        self.price = price

    def summary(self):
        return f"{self.title}: {self.hours} hours for Rs {self.price}"
    def price_per_hour(self):
        return round(self.price / self.hours, 2)

py = Course("Python Basics", 40, 4999)
web = Course("Web Design", 60, 6499)
print(py.summary())
print(web.summary())
print(py.price_per_hour(), web.price_per_hour())