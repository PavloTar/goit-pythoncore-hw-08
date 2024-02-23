from .name import Name
from .phone import Phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday=None

    def add_phone(self, phone):
        if phone not in [p.value for p in self.phones]:
            self.phones.append(Phone(phone))
            print("Phone number added to contact.")
        else:
            print("Phone number already exists for this contact.")

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"