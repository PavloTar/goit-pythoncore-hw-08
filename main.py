from address_book.address_book import AddressBook
from address_book.record import Record


def parse_input(user_input):
    command_parts = user_input.lower().split()
    if not command_parts:
        return ("Invalid command",)
    command = command_parts[0]
    args = command_parts[1:]
    return (command, args)

def main():
    
    book = AddressBook.load_from_file()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            book.save_to_file()
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(args) != 2:
                print("Invalid number of arguments for 'add' command.")
            else:
                name, phone = args
                try:
                    existing_record = book.find(name)
                    if existing_record:
                        existing_record.add_phone(phone)
                    else:
                        record = Record(name)
                        record.add_phone(phone)
                        book.add_record(record)
                        print("New contact added.")
                except ValueError as e:
                   print(f"Error: {e}")        
        elif command == "change":
            if len(args) != 3:
                print("Invalid number of arguments for 'change' command, use change <name> <old_phone> <new_phone> ")
            else:
                name, new_phone, old_phone = args
                existing_record = book.find(name)
                if existing_record:
                    try :
                        existing_record.edit_phone(new_phone, old_phone)
                    except ValueError as e:
                       print(f"Error: {e}")       
                else:
                    print("Contact not found.")
        elif command == "phone":
            if len(args) != 1:
                print("Invalid number of arguments for 'phone' command.")
            else:
                name = args[0]
                phone = book.find(name)
                if phone:
                    print(f"Phone number for {name}: {phone}")
                else:
                    print("Contact not found.")
        elif command == "all":
            book.show_all()

        elif command == "add-birthday":
            if len(args) != 2:
                print("Invalid number of arguments for 'add-birthday' command.")
            else:
                name, birthday = args
                try:
                   result = book.add_birthday([name, birthday])
                   print(result)
                except ValueError as e:
                   print(f"Error: {e}")    
        elif command == "show-birthday":
            if len(args) != 1:
                print("Invalid number of arguments for 'show-birthday' command.")
            else:
                name = args[0]
                birthday = book.show_birthday([name])
                print(f"{birthday}")
        elif command == "birthdays":
            upcoming_birthdays = book.get_upcoming_birthdays()
            for birthday in upcoming_birthdays:
                print(f"{birthday['name']}: birthday - {birthday['birthday']}, congratulation date: {birthday['congratulation_date']}")

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()