from collections import UserDict
from datetime import datetime, timedelta
from .birthday import Birthday
import pickle


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Input error"
    return wrapper


class AddressBook(UserDict):
    
    @input_error
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def show_all(self):
        if self.data:
            print("\n".join(f"{name}: {phone}" for name, phone in self.data.items()))
        else:
            print("No contacts available.")


    def add_birthday(self, args):
        name, birthday = args[0], args[1]
        record = self.find(name)
        if record:
            record.birthday = Birthday(birthday)
            return f"Birthday added to {name}."
        return f"Contact with name {name} not found."

    @input_error
    def show_birthday(self, args):
        name = args[0]
        record = self.find(name)
        if record and record.birthday:
            return f"Birthday of {name}: {record.birthday.value}"
        return f"The contact named {name} does not have a specified birthday."

    @input_error
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                days_until_birthday = (birthday_this_year - today).days

                if 0 <= days_until_birthday <= 7:
                    if birthday_this_year.weekday() in [5, 6]:
                        days_until_birthday += (7 - birthday_this_year.weekday())

                    congratulation_date = today + timedelta(days=days_until_birthday)
                    congratulation_date_str = congratulation_date.strftime("%d.%m.%Y")

                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "birthday": record.birthday,
                        "congratulation_date": congratulation_date_str
                    })

        return upcoming_birthdays

    def save_to_file(book, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(book, f)


    def load_from_file(filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return AddressBook()  # Return a new address book if file not found
    
  
