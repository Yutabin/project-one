class SimpleClass:
    def __init__(self, name):
        self.name = name

# Приклад класу
if __name__ == "__main__":
    # Створення обєкту класу SimpleClass з аргументом "Yulian"
    obj = SimpleClass("Yulian")

    # Виведення значення змінної name
    print("Name:", obj.name)
