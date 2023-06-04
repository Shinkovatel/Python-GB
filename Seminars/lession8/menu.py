import task

choice = ""

while True:
    print("1) Добавить запись")
    print("2) Удалить запись")
    print("3) Просмотр записей")
    print("4) Выход")

    choice = input("Выберите пункт от 1 до 4:  ")

    choice = choice.strip()

    if (choice == "1"):
        new_list = input("Введите Фамилию Имя Отчество через (,)")
        task.open_file_write("phones.txt", new_list)
    elif (choice == "2"):
        text_delite = input("введите фамилию коротую хотите удалить: ")
        task.file_delite('phones.txt',text_delite)
    elif (choice == "3"):
        print(task.open_file_read('phones.txt'))
    elif (choice == "4"):
        break
    else:
        print("вы набрали число отличное от 1-4, попробуйте снова")