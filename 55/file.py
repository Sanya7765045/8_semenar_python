# Функция для записи контакта в файл
def write_contact_in_the_file(myList):
    with open("notebook.txt", 'a', encoding="utf-8") as file:
        for item in myList:
            file.write(f"{item} ")  # Записываем каждый элемент контакта, разделенные пробелом
        file.write("\n")  # Завершаем запись контакта переходом на новую строку
    return "Контакт успешно добавлен!"

# Функция для чтения всех контактов из файла
def show_all_contakts():
    contaktsList = []
    with open("notebook.txt", 'r', encoding="utf-8") as file:
        for line in file:
            contact_data = line.strip().split()  # Разделяем строку контакта на элементы
            contaktsList.append(contact_data)  # Добавляем контакт в список
    return contaktsList  # Возвращаем список всех контактов из файла

def full_write_contakts(myList):
    with open("notebook.txt", 'w', encoding="utf-8") as file:
        for contact_data in myList:
            contact_str = " ".join(contact_data) + "\n"
            file.write(contact_str)


