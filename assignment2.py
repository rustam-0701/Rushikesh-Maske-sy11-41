def decorator(func):
    def wrapper(self):
        print("***" * 10)
        func(self)
        print("***" * 10)
    return wrapper


class report:
    template = "Default"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    def __str__(self):
        return f"template:{self.template}\nTitle:{self.title}\nContent:{self.content}"

    @decorator
    def show_report(self):
        print(self)


report.change_template("student Report")

r1 = report(
    "python project",
    "Dynamic Report Generated Using OOP"
)

r1.show_report()