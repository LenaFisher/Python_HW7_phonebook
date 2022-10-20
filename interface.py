import model

step_back = 0
add = 1
upload = 2
CSV = 1
TXT = 2

def  format_mode(): 
    print(f"Выберите формат для работы с данными:\n1 - CSV\n2 - TXT")
    num = int(input("введите номер варианта: "))
    return num


def choice_actoin():
    print("Выберите действие:\n0 - вернуться к выбору формата данных\n1 - добавить данные\n2 - выгрузить данные")
    num2 = int(input("введите номер варианта: "))
    return num2


def get_surname():
    surname = input("введите фамилию: ")
    return surname

def get_name():
    name = input("введите имя: ")
    return name

def get_phone():
    phone = input("введите номер телефона: ")
    return phone

def get_description():
    description = input("введите описание: ")
    return description