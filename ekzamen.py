class SimpleClass:
    def __init__(self, name):
        self.name = name

# Приклад використання класу
if __name__ == "__main__":
    # Створення об'єкту класу SimpleClass з аргументом "Alice"
    obj = SimpleClass("Yulian")

    # Виведення значення змінної name об'єкта
    print("Name:", obj.name)
