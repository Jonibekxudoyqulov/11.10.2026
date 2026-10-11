class Student:
    """Talaba haqidagi ma'lumotlarni boshqaruvchi klass."""
    
    def __init__(self, name: str, age: int, major: str):
        self.name = name
        self.age = age
        self.major = major
        self.grades = []

    def add_grade(self, grade: float):
        """Talabaga baho qo'shish."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"{self.name} ga {grade} baho qo'shildi.")
        else:
            print("Baho 0 va 100 oralig'ida bo'lishi kerak!")

    def get_average_grade(self) -> float:
        """O'rtacha bahoni hisoblash."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """Talaba haqida to'liq ma'lumotni chiqarish."""
        avg = self.get_average_grade()
        print("\n--- Talaba Ma'lumoti ---")
        print(f"Ism: {self.name}")
        print(f"Yosh: {self.age}")
        print(f"Yo'nalish: {self.major}")
        print(f"Baholar: {self.grades}")
        print(f"O'rtacha baho: {avg:.2f}")
        print("------------------------\n")


# Kodni tekshirib ko'rish uchun test qismi:
if __name__ == "__main__":
    # Yangi talaba obyektini yaratamiz
    student1 = Student("Jonibek Xudoyqulov", 17, "Kompyuter Injiniringi,Backend,Suniy Intellekt")
    
    # Baholar qo'shamiz
    student1.add_grade(85)
    student1.add_grade(90)
    student1.add_grade(95)
    
    # Ma'lumotlarni ko'rsatamiz
    student1.display_info()