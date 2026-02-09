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


class Subject:
    subject_list = []
    _id_counter = 456

    def __init__(self, subject_name, subject_teacher, subject_grade, subject_category):
        self.__subject_id = Subject._id_generator()
        self.subject_name = subject_name
        self.subject_teacher = subject_teacher
        self.subject_grade = subject_grade
        self.subject_category = subject_category
        self.add()

    @classmethod
    def _id_generator(cls):
        current_id = cls._id_counter
        cls._id_counter += 4
        return current_id

    @property
    def subject_id(self):
        return self.__subject_id

    def add(self):
        Subject.subject_list.append(self)
        print("Subject Added")
        write_log(f"Subject ===> Added (id : {self.subject_id})")

    def remove(self):
        Subject.subject_list.remove(self)
        print("Subject Removed")
        write_log(f"Subject ===> Removed (id : {self.subject_id})")

    @classmethod
    def subject_count(cls):
        print(f"Subject Count is: {len(cls.subject_list)}")
        write_log(f"Subject ===> Count requested (total : {len(cls.subject_list)})")

    def show(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- Subject Info -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print(f"Subject ID: {self.__subject_id}")
        print(f"Subject Name: {self.subject_name}")
        print(f"Subject Teacher: {self.subject_teacher}")
        print(f"Subject Grade: {self.subject_grade}")
        print(f"Subject Category: {self.subject_category}")
        write_log(f"Subject ===> Info requested (id : {self.subject_id})")

    @classmethod
    def search_by_id(cls, subject_id):
        for i in cls.subject_list:
            if i.subject_id == subject_id:
                s = f"Found ==> ID: {i.subject_id} - Name: {i.subject_name} - Teacher: {i.subject_teacher} - Grade: {i.subject_grade} - Category: {i.subject_category}"
                write_log(f"Subject ===> Search success (id : {subject_id})")
                print(s)
                return i
        print("Not found")
        write_log(f"Subject ===> Search failed (id : {subject_id})")
        return None

    def edit(self, n_subject_name=None, n_subject_teacher=None, n_subject_grade=None, n_subject_category=None):
        if n_subject_name is not None:
            self.subject_name = n_subject_name
        if n_subject_teacher is not None:
            self.subject_teacher = n_subject_teacher
        if n_subject_grade is not None:
            self.subject_grade = n_subject_grade
        if n_subject_category is not None:
            self.subject_category = n_subject_category
        print("Subject Edited")
        write_log(f"Subject ===> Edited (id : {self.subject_id})")

    @classmethod
    def show_all(cls):
        subject_info = []
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- All Subjects -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        write_log("Subject ===> Show all requested")
        for i in cls.subject_list:
            info = f"ID: {i.subject_id} - Name: {i.subject_name} - Teacher: {i.subject_teacher} - Grade: {i.subject_grade} - Category: {i.subject_category}"
            subject_info.append(info)
            print(info)
        return subject_info

# ================== TEST CASES ==================
if __name__ == "__main__":
    print("\n--- Adding Subjects ---")
    s1 = Subject("Math", "Mr. Ali", 9, "Science")
    s2 = Subject("History", "Ms. Sara", 10, "Social")
    s3 = Subject("Biology", "Dr. Reza", 9, "Science")

    print("\n--- Show All Subjects ---")
    Subject.show_all()

    print("\n--- Search by ID ---")
    Subject.search_by_id(s2.subject_id)
    Subject.search_by_id(9999)
    Subject.search_by_id(456)

    print("\n--- Edit Subject ---")
    s1.edit("Math", "Mr. Reza", 9, "Science")

    print("\n--- Remove a Subject ---")
    s3.remove()

    print("\n--- Show All After Removal ---")
    Subject.show_all()

    print("\n--- Total Subjects ---")
    Subject.subject_count()
