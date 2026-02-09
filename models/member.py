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


class Member(Person):
    Member_list = []

    def __init__(self, name, lname, ncode, age, phone, address, membership_num, username=None, password=None):
        super().__init__(name, lname, ncode, age, phone, address)
        self.membership_num = membership_num
        self.__username = username
        self.__password = password
        self.add()

    def add(self):
        Member.Member_list.append(self)
        print("Member added")
        write_log(f"Member ===> Added (membership_num : {self.membership_num})")

    def remove(self):
        Member.Member_list.remove(self)
        print("Member removed")
        write_log(f"Member ===> Removed (membership_num : {self.membership_num})")

    @classmethod
    def member_count(cls):
        print(f"Member count is: {len(cls.Member_list)}")
        write_log(f"Member ===> Count requested (total : {len(cls.Member_list)})")

    def show(self):
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- Member Info -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        print("Member name:", self.name)
        print("Member last name:", self.lname)
        print("Member National code:", self.ncode)
        print("Member Age:", self.age)
        print("Member Phone:", self.phone)
        print("Member Address:", self.address)
        print("Membership number:", self.membership_num)
        print("Username:", self.__username)
        print("Password:", self.__password)
        write_log(f"Member ===> Info requested (membership_num : {self.membership_num})")

    def edit(self, n_name=None, n_lname=None, n_phone=None, n_address=None, n_membership_num=None, n_username=None, n_password=None):
        if n_name is not None:
            self.name = n_name
        if n_lname is not None:
            self.lname = n_lname
        if n_phone is not None:
            self.phone = n_phone
        if n_address is not None:
            self.address = n_address
        if n_membership_num is not None:
            self.membership_num = n_membership_num
        if n_username is not None:
            self.__username = n_username
        if n_password is not None:
            self.__password = n_password
        print("Member edited")
        write_log(f"Member ===> Edited (membership_num : {self.membership_num})")

    @classmethod
    def search_by_membership_num(cls, membership_num):
        for i in cls.Member_list:
            if i.membership_num == membership_num:
                s = f"Found ==> membership number: {i.membership_num} - name: {i.name} - last name: {i.lname} - national code: {i.ncode}"
                write_log(f"Member ===> Search success (membership_num : {membership_num})")
                print(s)
                return i
        print("Not found")
        write_log(f"Member ===> Search failed (membership_num : {membership_num})")
        return None

    @classmethod
    def show_all(cls):
        member_info = []
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+- All Member -+-+-+-+-+-+-+-+-+-+-+-+-+-")
        write_log("Library Member ===> Show all items requested")
        for i in cls.Member_list:
            info = f"Found ==> membership number: {i.membership_num} - name: {i.name} - last name: {i.lname} - national code: {i.ncode}"
            member_info.append(info)
            print(info)
        return member_info

# ================== TEST CASES ==================
if __name__ == "__main__":
    print("\n--- Test 1: Create Members ---")
    m1 = Member("Ali", "Zarei", "1234567890", 30, "09120000001", "Tehran", "ali123", "pass1")
    m2 = Member("Sara", "Moradi", "1234567891", 25, "09120000002", "Tehran", "sara_m", "pass2")
    m3 = Member("Reza", "Ahmadi", "1234567892", 28, "09120000003", "Tehran", "reza_a", "pass3")

    print("\n--- Test 2: Show Individual Members ---")
    m1.show()
    m2.show()
    m3.show()

    print("\n--- Test 3: Total Members ---")
    Member.member_count()

    print("\n--- Test 4: Edit Member Information ---")
    m2.edit(n_name="Sarina", n_phone="09121111111", n_username="sarina_m", n_password="newpass")
    m2.show()

    print("\n--- Test 5: Search by Membership Number ---")
    Member.search_by_membership_num(m2.membership_num)
    Member.search_by_membership_num("9999")  # شماره موجود نیست

    print("\n--- Test 6: Remove a Member ---")
    m3.remove()
    Member.member_count()
