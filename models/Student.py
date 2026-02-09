from models.Person import *
from datetime import datetime
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "log")


os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "School_Manager_System_log.txt")
def write_log(message: str):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time}] {message}\n")

class Student(Person):
    _students_list = []
    _id_counter = 1000

    def __init__(self, classroom_id, name, lname, ncode, age, phone, address, grade):
        super().__init__(name, lname, ncode, age, phone, address)
        self.__student_id = Student._id_generator()
        self.classroom_id = classroom_id
        self.grade = grade
        self.add()

    @property
    def student_id(self):
        return self.__student_id

    @classmethod
    def _id_generator(cls):
        current_id = cls._id_counter
        cls._id_counter += 2
        return current_id

    def add(self):
        Student._students_list.append(self)
        print(f"Student added")
        write_log(f"Student ===> Added (id : {self.student_id})")

    def remove(self):
        if self in Student._students_list:
            Student._students_list.remove(self)
            print(f"Student deleted")
            write_log(f"Student ===> Removed (id : {self.student_id})")

    @classmethod
    def student_count(cls):
        print(f"Total students: {len(cls._students_list)}")
        write_log(f"Student ===> Count requested (total : {len(cls._students_list)})")

    @classmethod
    def search_by_id(cls, student_id):
        for i in cls._students_list:
            if i.student_id == student_id:
                s = f"Found ==> {i.student_id} - {i.name} {i.lname}  - Grade: {i.grade} - Age: {i.age}"
                write_log(f"Student ===> Search success (id : {student_id})")
                print(s)
                return i
        print("Not found")
        write_log(f"Student ===> Search failed (id : {student_id})")
        return None

    def edit(self, n_name=None, n_lname=None, n_ncode=None, n_age=None, n_phone=None,
             n_address=None, n_classroom_id=None, n_grade=None):
        if n_name is not None:
            self.name = n_name
        if n_lname is not None:
            self.lname = n_lname
        if n_ncode is not None:
            self.ncode = n_ncode
        if n_age is not None:
            self.age = n_age
        if n_phone is not None:
            self.phone = n_phone
        if n_address is not None:
            self.address = n_address
        if n_classroom_id is not None:
            self.classroom_id = n_classroom_id
        if n_grade is not None:
            self.grade = n_grade
        print("Student updated")
        write_log(f"Student ===> Edited (id : {self.student_id})")

    def show(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- Student Info -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print(f"Student ID: {self.student_id}")
        print(f"Student name: {self.name}")
        print(f"Student last name: {self.lname}")
        print(f"Student ncode: {self.ncode}")
        print(f"Student age: {self.age}")
        print(f"Student phone: {self.phone}")
        print(f"Student address: {self.address}")
        print(f"Student classroom id: {self.classroom_id}")
        print(f"Student grade: {self.grade}")
        write_log(f"Student ===> Info requested (id : {self.student_id})")

    @classmethod
    def show_all(cls):
        students_info = []
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- All Students -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        write_log("Student ===> Show all requested")
        for i in cls._students_list:
            info = f"Found ==> {i.student_id} - {i.name} {i.lname}  - Grade: {i.grade} - Age: {i.age}"
            students_info.append(info)
            print(info)
        return students_info




# ================== TEST CASES ==================
if __name__ == "__main__":
    print("\n--- Test 1: Create Students ---")
    s1 = Student("9A", "Ali", "Zarei", "1234567890", 14, "09120000001", "Tehran", 9)
    s2 = Student("10B", "Sara", "Moradi", "1234567891", 15, "09120000002", "Tehran", 10)
    s3 = Student("8C", "Reza", "Ahmadi", "1234567892", 13, "09120000003", "Tehran", 8)

    print("\n--- Test 2: Show Individual Students ---")
    s1.show()
    s2.show()
    s3.show()

    print("\n--- Test 3: Show All Students ---")
    Student.show_all()

    print("\n--- Test 4: Search by ID ---")
    Student.search_by_id(s2.student_id)
    Student.search_by_id(9999)

    print("\n--- Test 5: Edit Student Information ---")
    s1.edit(n_name="Alireza", n_classroom_id="9B", n_grade=10)
    s1.show()

    print("\n--- Test 6: Remove a Student ---")
    s3.remove()
    Student.show_all()

    print("\n--- Test 7: Total Students ---")
    Student.student_count()

    print("\n--- Test 8: Multiple Edits ---")
    s2.edit(n_name="Sara", n_lname="Mohammadi", n_age=16, n_phone="09121111111")
    s2.show()

    print("\n--- Test 9: Inheritance Check ---")
    print(isinstance(s1, Student))  # True
