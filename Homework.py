import json
import os

FILENAME = "students.json"

def load_students():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_students(students):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False,
                  indent=4)
    print("Данные сохранены.")

def add_student(students):
    if len(students) >= 10:
        print("Максимум 10 студентов в списке!")
        return students
    name = input(
        "Введите имя студента: ").strip().capitalize()
    if len(name) == 0:
        print("Имя не может быть пустым!")
    elif len(name) > 15:
        print("Имя слишком длинное (максимум 15 символов)!")
    elif name in students:
        print("Такой студент уже есть в списке!")
    else:
        students.append(name)
        print(f"Студент {name} успешно добавлен!")
    return students

def change_student(students, name: str, index: int):
    processed_name = name.strip().capitalize()
    students[index] = processed_name

def change(students):
    indexName = int(input("Номер студента:"))
    name = input("Новое имя:")
    change_student(students, name, indexName)

def delete_student_name(students):
    ind_student = input("Введите имя студента для удаления:")
    if ind_student in students:
        students.remove(ind_student)
        save_students(students)
    else:
        print("Такого имени не существует!")

def delete_student_index(students):
    ind_student = int(input("Введите индекс студента для удаления:"))
    students.pop(ind_student)
    print("Студент удален успешно!")

def show_students(students):
    if not students:
        print("Список студентов пуст.")
    else:
        print("Текущий список студентов:")
        for i, s in enumerate(students, start=1):
            print(f"{i}. {s}")

def main():
    students = load_students()

    while True:
        print("\nМеню:")
        print("1) Добавить студента")
        print("2) Изменить имя студента")
        print("3) Удалить студента по имени")
        print("4) Удалить студента по индексу")
        print("5) Показывать всех студентов")
        print("0) Выход")

        command = input("\nВыберите команду: ").strip()

        if command == "1":
            students = add_student(students)
        elif command == "2":
            change(students)
        elif command == "3":
            delete_student_name(students)
        elif command == "4":
            delete_student_index(students)
        elif command == "5":
            show_students(students)
        elif command == "0":
            save_students(students)
            print("Программа завершена.")
            break
        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()