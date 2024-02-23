# === Вимоги технічого завдання ===
# Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).


from .field import Field

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, str) or len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be a 10-digit string.")
        super().__init__(value)
      
        
