from file import *  # Импортируем функции из файла file.py

# Функция для добавления нового контакта
def adding_a_contact():
    contactList = []
    contactList.append(str(input("Введите фамилию контакта: ")))
    contactList.append(str(input("Введите имя контакта: ")))
    contactList.append(str(input("Введите отчество контакта: ")))
    contactList.append(str(input("Введите номер телефона контакта: ")))
    print(write_contact_in_the_file(contactList))  # Вызываем функцию для записи контакта в файл

# Функция для вывода всех контактов
def showing_contakts():
    myList = show_all_contakts()
    print("Фамилия | Имя | Отчество | Номер телефона")
    for contact_data in myList:
        for i in range(0, len(contact_data), 4):
            contact = contact_data[i:i+4]
            if len(contact) == 4:
                print(f"{contact[0]} | {contact[1]} | {contact[2]} | {contact[3]}")

# Функция для поиска контактов по фамилии
def search_contacts_by_lastname(lastname):
    myList = show_all_contakts()  # Получаем список всех контактов из файла
    print("Результаты поиска по фамилии:")
    
    found_contacts = []  # Здесь будем хранить найденные контакты
    
    # Итерируемся по каждому контакту в списке
    for contact_data in myList:
        for i in range(0, len(contact_data), 4):
            contact = contact_data[i:i+4]
            if len(contact) == 4:
                if contact[0] == lastname:  # Если фамилия совпадает с заданной
                    found_contacts.append(contact)  # Добавляем контакт в список найденных
    
    if len(found_contacts) == 0:
        print("Контакты с такой фамилией не найдены.")
    else:
        print("Фамилия | Имя | Отчество | Номер телефона")
        for contact in found_contacts:
            print(f"{contact[0]} | {contact[1]} | {contact[2]} | {contact[3]}")

# Функция для изменения контакта по фамилии
def change_a_contact(lastname):
    myList = show_all_contakts()

    found_contacts = []

    for i, contact_data in enumerate(myList):
        for j in range(0, len(contact_data), 4):
            contact = contact_data[j:j+4]
            if len(contact) == 4 and contact[0] == lastname:
                found_contacts.append(i)

    if len(found_contacts) == 0:
        print("Контакты с такой фамилией не найдены.")
    else:
        for index in found_contacts:
            new_lastname = input("Введите новую фамилию контакта: ")
            new_firstname = input("Введите новое имя контакта: ")
            new_patronymic = input("Введите новое отчество контакта: ")
            new_phone = input("Введите новый номер телефона контакта: ")

            myList[index][0] = new_lastname
            myList[index][1] = new_firstname
            myList[index][2] = new_patronymic
            myList[index][3] = new_phone

        full_write_contakts(myList)

# Функция для удаления контакта по фамилии
def delete_a_contact(lastname):
    myList = show_all_contakts()
    print("Результаты поиска по фамилии:")

    found_contacts = []

    for contact_data in myList:
        for i in range(0, len(contact_data), 4):
            contact = contact_data[i:i+4]
            if len(contact) == 4:
                if contact[0] == lastname:
                    found_contacts.append(contact)

    if len(found_contacts) == 0:
        print("Контакты с такой фамилией не найдены.")
    else:
        new_list = [contact_data for contact_data in myList if contact_data not in found_contacts]
        full_write_contakts(new_list)

# Функция для выбора действия и его выполнения
def choise(choise):
    if choise == 1:
        print("Добавление нового контакта:")
        adding_a_contact()  # Вызываем функцию для добавления контакта
        return 0
    elif choise == 2:
        print("Вывод всех контактов:")
        showing_contakts()  # Вызываем функцию для вывода контактов
        return 0
    elif choise == 3:
        print("Поиск контакта по фамилии:")
        search_contacts_by_lastname(str(input("Введите Фамилию контакта: ")))  # Вызываем функцию для поиска по фамилии
        return 0
    elif choise == 4:
        print("Поиск контакта по фамилии и его изменение:")
        change_a_contact(str(input("Введите Фамилию контакта: ")))  # Вызываем функцию для изменения контакта
        return 0
    elif choise == 5:
        print("Поиск контакта по фамилии и его удаление:")
        delete_a_contact(str(input("Введите Фамилию контакта: ")))  # Вызываем функцию для удаления контакта
        return 0
    elif choise == 6:
        print("Всего доброго!")  # Завершаем программу
        return 1
