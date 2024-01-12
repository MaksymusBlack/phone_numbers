
from re import findall
phone_numbers = {}


# Декоратор
def logged_func(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print('erroe')
            return 'Enter user name'
        except ValueError:
            print('erroe')
            return 'Give me phone please'
        except IndexError:
            print('erroe')
            return 'Give me name and phone please'
    return inner



## Функція для додавання номеру в список
@logged_func
def add(name, number):
    
    new_contact = {name:number}
    phone_numbers.update(new_contact)
    return f'Contact {name} has been added'
 


## Функція для зміни номеру для контакту
@logged_func
def change(name, new_number):
    
    if name.capitalize() in phone_numbers:
        phone_numbers[name.capitalize()] = new_number
        return f'Number of {name} has been changed to {new_number}'
    # На випадок, якщо нема такого імені в словнику
    else:
        return f'Number {name} not in the list. Give me name and phone please'
    


## Функція для пошуку номера з ігноруванням регістру
@logged_func
def phone(name):

    for key, value in phone_numbers.items():
        if key.lower() == name.lower():
            reply = f"Name: {key}, number: {value}"
            return reply


# Функція обробки команд
def command_processing(input_command):

    if input_command.lower() == 'hello':
        return 'How can I help you? '
            
    elif input_command.lower() == "good bye" or \
         input_command.lower() == "close" or \
        input_command.lower() == "exit" or \
        input_command.lower() == ".":
        return False

    elif input_command.lower() == 'show all':
        return phone_numbers
    
    else:
    # розділяємо на окремі слова
        command = findall(r'[\w]{1,}', input_command)
        #виконуємо відповідні команди
        if command[0].lower() == 'add':
            return add(command[1], command[2])

        if command[0].lower() == 'change':
            return change(command[1], command[2])

        if command[0].lower() == 'phone':
            return phone(command[1])
        

# Основна функція
def main():
    
    while True:
        input_command = input()
        if command_processing(input_command) == False:
            break
        else:
            print(command_processing(input_command))
            continue

      
        

if __name__ == "__main__":
    main()

    
