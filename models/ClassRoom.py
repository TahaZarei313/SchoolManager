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

class ClassRoom:
    ClassRoom_list = []
    id_counter = 2025

    def __init__(self, class_name, class_grade, capacity=30):
        self.class_id = ClassRoom._id_generator()
        self.class_name = class_name
        self.class_grade = class_grade
        self.capacity = capacity
        self.add()

    @classmethod
    def _id_generator(cls):
        current_id = cls.id_counter
        cls.id_counter += 3
        return current_id

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if 1 <= value <= 30:
            self.__capacity = value
        else:
            raise ValueError("Invalid capacity")

    @property
    def class_grade(self):
        return self.__class_grade

    @class_grade.setter
    def class_grade(self, value):
        if 7 <= value <= 9:
            self.__class_grade = value
        else:
            raise ValueError("Invalid class grade")

    @classmethod
    def classroom_count(cls):
        print(f"Class Room Count is : {len(ClassRoom.ClassRoom_list)}")
        write_log(f"ClassRoom ===> Count requested (total : {len(ClassRoom.ClassRoom_list)})")

    def add(self):
        ClassRoom.ClassRoom_list.append(self)
        print("Class Room Added")
        write_log(f"ClassRoom ===> Added (id : {self.class_id})")

    def remove(self):
        ClassRoom.ClassRoom_list.remove(self)
        print("Class Room Deleted")
        write_log(f"ClassRoom ===> Removed (id : {self.class_id})")

    def show(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- Class Room Info -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print(f"Class Room ID: {self.class_id}")
        print(f"Class Room Name: {self.class_name}")
        print(f"Class Room Grade: {self.class_grade}")
        print(f"Class Room Capacity: {self.capacity}\n")
        write_log(f"ClassRoom ===> Info requested (id : {self.class_id})")

    def edit(self, class_name=None, n_class_grade=None, n_capacity=None):
        if class_name is not None:
            self.class_name = class_name
        if n_class_grade is not None:
            self.class_grade = n_class_grade
        if n_capacity is not None:
            self.capacity = n_capacity
        print("Class Room Updated")
        write_log(f"ClassRoom ===> Edited (id : {self.class_id})")

    @classmethod
    def search_by_id(cls, id):
        for i in cls.ClassRoom_list:
            if i.class_id == id:
                s =f"Found ==> ID: {i.class_id} - Name: {i.class_name} - Grade: {i.class_grade} - Capacity: {i.capacity}"
                write_log(f"ClassRoom ===> Search success (id : {i.class_id})")
                print(s)
                return i
        print("Not found")
        write_log(f"ClassRoom ===> Search failed (id : {id})")
        return None

    @classmethod
    def show_all(cls):
        ClassRoom_info = []
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- All Class Rooms -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        write_log("ClassRoom ===> Show all requested")
        for i in cls.ClassRoom_list:
            info = f"ID: {i.class_id} - Name: {i.class_name} - Grade: {i.class_grade} - Capacity: {i.capacity}"
            ClassRoom_info.append(info)
            print(info)
        return ClassRoom_info


# ================== TEST CASES ==================
if __name__ == "__main__":
    print("\n============== Test Case: ClassRoom ==============\n")

    print("--- 1) Creating Class Rooms (Valid Inputs) ---")
    c1 = ClassRoom("A5", 9, 30)
    c2 = ClassRoom("D5", 8, 26)

    print("\n--- 2) Testing Invalid Capacity (Should Raise Error) ---")
    try:
        c_invalid = ClassRoom("ZZ", 9, 90)
    except ValueError as e:
        print("Error Caught:", e)

    print("\n--- 3) Testing Invalid Grade (Should Raise Error) ---")
    try:
        c_invalid2 = ClassRoom("AA", 5, 20)
    except ValueError as e:
        print("Error Caught:", e)

    print("\n--- 4) Show Class Rooms Individually ---")
    c1.show()
    c2.show()

    print("\n--- 5) Show All Class Rooms ---")
    ClassRoom.show_all()

    print("\n--- 6) Search by ID (Existing) ---")
    ClassRoom.search_by_id(c1.class_id)

    print("\n--- 7) Search by ID (Not Existing) ---")
    ClassRoom.search_by_id(9999)

    print("\n--- 8) Edit Class Room ---")
    c1.edit(class_name="A6", n_class_grade=8, n_capacity=28)
    c1.show()

    print("\n--- 9) Test Invalid Edit (Invalid Capacity) ---")
    try:
        c1.edit(n_capacity=100)
    except ValueError as e:
        print("Error Caught:", e)

    print("\n--- 10) Remove a Class Room ---")
    c2.remove()

    print("\n--- 11) Show All After Removal ---")
    ClassRoom.show_all()

    print("\n--- 12) Total Class Rooms ---")
    ClassRoom.classroom_count()

    print("\n============== End of Test Case ==============\n")
