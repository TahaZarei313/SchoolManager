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

class SchoolEmployee(Person):
    _employees_list = []
    _id_counter = 1000

    def __init__(self, name, lname, ncode, age, phone, address,
                 salary, role, shift, edu_level, major, work_experience):
        super().__init__(name, lname, ncode, age, phone, address)

        self.__em_id = SchoolEmployee._id_generator()
        self.__salary = salary
        self.role = role
        self.shift = shift
        self.edu_level = edu_level
        self.major = major
        self.work_experience = work_experience

        self.add()

    @classmethod
    def _id_generator(cls):
        current_id = cls._id_counter
        cls._id_counter += 1
        return current_id

    def add(self):
        SchoolEmployee._employees_list.append(self)
        print(f"Employee added")
        write_log(f"SchoolEmployee ===> Added Employee (ID: {self.__em_id})")

    def remove(self):
        if self in SchoolEmployee._employees_list:
            SchoolEmployee._employees_list.remove(self)
            print(f"Employee deleted")
            write_log(f"SchoolEmployee ===> Employee Removed (ID: {self.__em_id})")

    @classmethod
    def Employee_count(cls):
        print(f"Employee count is : {len(SchoolEmployee._employees_list)}")
        write_log(f"SchoolEmployee ===> Employee count : {len(SchoolEmployee._employees_list)}")

    @classmethod
    def search_by_id(cls, emp_id):
        for i in cls._employees_list:
            if i.em_id == emp_id:
                s = f"Found ==> {i.em_id} - {i.role} - {i.name} {i.lname}"
                write_log(f"SchoolEmployee ===> Search success (id : {i.em_id})")
                print(s)
                return i

        print(f"Employee with ID {emp_id} not found")
        write_log(f"SchoolEmployee ===> Search failed (id : {emp_id})")
        return None

    def edit(self, n_name=None, n_lname=None, n_ncode=None, n_age=None,
             n_phone=None, n_address=None, n_salary=None, n_role=None,
             n_shift=None, n_edu_level=None, n_major=None, n_work_experience=None):

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

        if n_salary is not None:
            if n_salary > 0:
                self.salary = n_salary
            else:
                print("invalid salary value")

        if n_role is not None:
            self.role = n_role

        if n_shift is not None:
            self.shift = n_shift

        if n_edu_level is not None:
            self.edu_level = n_edu_level

        if n_major is not None:
            self.major = n_major

        if n_work_experience is not None:
            self.work_experience = n_work_experience



    # Property
    @property
    def em_id(self):
        return self.__em_id

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            raise ValueError("invalid salary value")
        self.__salary = value


    @classmethod
    def show_all(cls):
        SchoolEmployee_info = []
        write_log("SchoolEmployee ===> Show all requested")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- All Employees -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        for i in cls._employees_list:
            info = f"{i.em_id} - {i.role} - {i.name} {i.lname} - salary: {i.salary}"
            SchoolEmployee_info.append(info)
            print(info)
        return SchoolEmployee_info





class SchoolManager(SchoolEmployee):
    def __init__(self, name, lname, ncode, age, phone, address,
                 salary, role, shift, edu_level, major, work_experience,
                 license_number, room_number):
        super().__init__(name, lname, ncode, age, phone, address,
                         salary, role, shift, edu_level, major, work_experience)
        self.role = "manager"
        self.__license_number = license_number
        self.room_number = room_number

    @property
    def license_number(self):
        return self.__license_number


    def show(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- School Manager Info -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print(f"ID: {self.em_id}")
        print(f"Name: {self.name} {self.lname}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary}")
        print(f"Shift: {self.shift}")
        print(f"Education: {self.edu_level} in {self.major}")
        print(f"Work Experience: {self.work_experience} years")
        print(f"License Number: {self.license_number}")
        print(f"Room Number: {self.room_number}")
        print("")
        write_log(f"SchoolEmployee ===> School Manager info requested (id : {self.em_id})")


    def edit(self, n_license_number=None, n_room_number=None, **kwargs):
        super().edit(**kwargs)

        if n_license_number is not None:
            self.__license_number = n_license_number

        if n_room_number is not None:
            self.room_number = n_room_number

        print("Employee updated")
        write_log(f"SchoolEmployee ===> School Manager edited (id : {self.em_id})")
        return None





class AssistantPrincipal(SchoolEmployee):
    def __init__(self, name, lname, ncode, age, phone, address,
                 salary, role, shift, edu_level, major, work_experience,
                 department, teaching_hours):
        super().__init__(name, lname, ncode, age, phone, address,
                         salary, role, shift, edu_level, major, work_experience)
        self.role = "assistant principal"
        self.department = department
        self.teaching_hours = teaching_hours

    def show(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- Assistant Principal Info -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print(f"ID: {self.em_id}")
        print(f"Name: {self.name} {self.lname}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary}")
        print(f"Shift: {self.shift}")
        print(f"Education: {self.edu_level} in {self.major}")
        print(f"Work Experience: {self.work_experience} years")
        print(f"Department: {self.department}")
        print(f"Teaching Hours: {self.teaching_hours}")
        print("")
        write_log(f"SchoolEmployee ===> Assistant Principal info requested (id : {self.em_id})")

    def edit(self, n_department=None, n_teaching_hours=None, **kwargs):
        super().edit(**kwargs)

        if n_department is not None:
            self.department = n_department

        if n_teaching_hours is not None:
            self.teaching_hours = n_teaching_hours
        print("Employee updated")
        write_log(f"SchoolEmployee ===> Assistant Principal edited (id : {self.em_id})")
        return None




class Teacher(SchoolEmployee):
    def __init__(self, name, lname, ncode, age, phone, address,
                 salary, role, shift, edu_level, major, work_experience,
                 subject_name, teaching_hours, teaching_days, overtime_hours):
        super().__init__(name, lname, ncode, age, phone, address,
                         salary, role, shift, edu_level, major, work_experience)
        self.role = "Teacher"
        self.subject_name = subject_name
        self.teaching_hours = teaching_hours
        self.teaching_days = teaching_days
        self.overtime_hours = overtime_hours

    def show(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- Teacher Info -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print(f"ID: {self.em_id}")
        print(f"Name: {self.name} {self.lname}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary}")
        print(f"Shift: {self.shift}")
        print(f"Education: {self.edu_level} in {self.major}")
        print(f"Work Experience: {self.work_experience} years")
        print(f"Subject: {self.subject_name}")
        print(f"Teaching Hours: {self.teaching_hours}")
        print(f"Teaching Days: {self.teaching_days}")
        print(f"Overtime Hours: {self.overtime_hours}")
        print("")
        write_log(f"SchoolEmployee ===> Teacher info requested (id : {self.em_id})")

    def edit(self, n_subject_name=None, n_teaching_hours=None, n_teaching_days=None, n_overtime_hours=None, **kwargs):
        super().edit(**kwargs)

        if n_subject_name is not None:
            self.subject_name = n_subject_name

        if n_teaching_hours is not None:
            self.teaching_hours = n_teaching_hours

        if n_teaching_days is not None:
            self.teaching_days = n_teaching_days

        if n_overtime_hours is not None:
            self.overtime_hours = n_overtime_hours
        print("Employee updated")
        write_log(f"SchoolEmployee ===> Teacher edited (id : {self.em_id})")
        return None




class Janitor(SchoolEmployee):
    def __init__(self, name, lname, ncode, age, phone, address,
                 salary, role, shift, edu_level, major, work_experience, duties):
        super().__init__(name, lname, ncode, age, phone, address,
                         salary, role, shift, edu_level, major, work_experience)
        self.role = "Janitor"
        self.duties = duties


    def show(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- Janitor Info -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print(f"ID: {self.em_id}")
        print(f"Name: {self.name} {self.lname}")
        print(f"Role: {self.role}")
        print(f"Salary: {self.salary}")
        print(f"Shift: {self.shift}")
        print(f"Education: {self.edu_level} in {self.major}")
        print(f"Work Experience: {self.work_experience} years")
        print(f"Duties: {self.duties}")
        print("")
        write_log(f"SchoolEmployee ===> Janitor info requested (id : {self.em_id})")

    def edit(self, n_duties=None, **kwargs):
        super().edit(**kwargs)

        if n_duties is not None:
            self.duties = n_duties

        print("Employee updated")
        write_log(f"SchoolEmployee ===> Janitor edited (id : {self.em_id})")
        return None



if __name__ == "__main__":

    print("\n===== TEST 1: Creating Employees =====")

    manager = SchoolManager(
        name="Ali", lname="Zarei", ncode="111", age=40,
        phone="091200000", address="Tehran", salary=50000000, role="Manager",
        shift="Morning", edu_level="PhD", major="Education", work_experience=15,
        license_number="MGR111", room_number=101
    )

    teacher = Teacher(
        name="Sara", lname="Moradi", ncode="222", age=29,
        phone="091200001", address="Tehran", salary=25000000, role="Teacher",
        shift="Morning", edu_level="Master", major="Math", work_experience=5,
        subject_name="Math", teaching_hours=20, teaching_days=5, overtime_hours=3
    )

    janitor = Janitor(
        name="Reza", lname="Karimi", ncode="333", age=45,
        phone="091200002", address="Tehran", salary=12000000, role="Janitor",
        shift="Evening", edu_level="Diploma", major="Services", work_experience=10,
        duties="Cleaning"
    )

    SchoolEmployee.show_all()

    # ===== TEST 2 =====
    print("\n===== TEST 2: Employee Count =====")
    manager.Employee_count()

    # ===== TEST 3 =====
    print("\n===== TEST 3: Search by ID =====")
    manager.search_by_id(manager.em_id)  # Should find manager
    manager.search_by_id(9999)  # Should not find

    # ===== TEST 4 =====
    print("\n===== TEST 4: Edit SchoolEmployee Base =====")
    teacher.edit(n_name="Taher", n_salary=26000000, n_shift="Evening")
    teacher.show()

    # ===== TEST 5 =====
    print("\n===== TEST 5: Edit SchoolManager =====")
    manager.edit(n_license_number="NEW999", n_room_number=202)
    manager.show()

    # ===== TEST 6 =====
    print("\n===== TEST 6: Edit AssistantPrincipal =====")
    assistant = AssistantPrincipal(
        name="Mohammad", lname="Ahmadi", ncode="444", age=38,
        phone="091212345", address="Tehran", salary=30000000, role="Assistant",
        shift="Morning", edu_level="Master", major="Education", work_experience=8,
        department="Science", teaching_hours=10
    )

    assistant.edit(n_department="Math Dept", n_teaching_hours=12)
    assistant.show()

    # ===== TEST 7 =====
    print("\n===== TEST 7: Edit Janitor =====")
    janitor.edit(n_duties="Full Maintenance")
    janitor.show()

    # ===== TEST 8 =====
    print("\n===== TEST 8: Remove Employee =====")
    janitor.remove()
    SchoolEmployee.show_all()

    print("\n===== ALL TESTS COMPLETED SUCCESSFULLY =====")



