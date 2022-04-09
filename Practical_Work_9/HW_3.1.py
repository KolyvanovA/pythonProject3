from Practical_Work_9.HW_3 import Position

if __name__ == "__main__":
    position = Position("Max", "Pain", "Programmer",
                        {"wage": 110, "bonus": 1.3})

    position.name = "Alexandr"
    position.position += "|Engineer"

    position.income["bonus"] = 1.0

    print(position.get_full_name.__name__, position.get_full_name())
    print(position.position)
    print(position.get_total_income.__name__, position.get_total_income())
