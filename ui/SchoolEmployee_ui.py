import tkinter as tk
from tkinter import messagebox, ttk
from models.SchoolEmployee import *

shift_options = ["Morning", "Afternoon", "Evening"]
edu_options = ["High School", "Bachelor", "Master", "PhD"]


def add_employee(root=None):
    win = tk.Toplevel(root)
    win.title("Add Employee")
    win.geometry("500x900")
    win.grab_set()  # modal

    tk.Label(win, text="Add New Employee", font=("Arial", 16)).pack(pady=10)
    tk.Label(win, text="Select Employee Type").pack()
    emp_type_var = tk.StringVar(value="Teacher")
    combo_type = ttk.Combobox(win, textvariable=emp_type_var,
                              values=["SchoolManager", "AssistantPrincipal", "Teacher", "Janitor"],
                              state="readonly")
    combo_type.pack(pady=5)

    form_frame = tk.Frame(win)
    form_frame.pack(pady=10)
    fields = {}

    def build_form(emp_type):
        for widget in form_frame.winfo_children():
            widget.destroy()
        fields.clear()

        for label_text in ["Name", "Last Name", "National Code", "Age", "Phone", "Address",
                           "Salary", "Role", "Shift", "Education Level", "Major", "Work Experience"]:
            tk.Label(form_frame, text=label_text).pack()
            if label_text == "Role":
                entry = tk.Entry(form_frame)
                entry.insert(0, emp_type)
                entry.config(state="readonly")
            elif label_text == "Shift":
                entry = ttk.Combobox(form_frame, values=shift_options, state="readonly")
                entry.current(0)
            elif label_text == "Education Level":
                entry = ttk.Combobox(form_frame, values=edu_options, state="readonly")
                entry.current(0)
            else:
                entry = tk.Entry(form_frame)
            entry.pack()
            fields[label_text] = entry

        # Employee specific fields
        if emp_type == "SchoolManager":
            for label_text in ["License Number", "Room Number"]:
                tk.Label(form_frame, text=label_text).pack()
                entry = tk.Entry(form_frame)
                entry.pack()
                fields[label_text] = entry
        elif emp_type == "AssistantPrincipal":
            for label_text in ["Department", "Teaching Hours"]:
                tk.Label(form_frame, text=label_text).pack()
                entry = tk.Entry(form_frame)
                entry.pack()
                fields[label_text] = entry
        elif emp_type == "Teacher":
            for label_text in ["Subject Name", "Teaching Hours", "Teaching Days", "Overtime Hours"]:
                tk.Label(form_frame, text=label_text).pack()
                entry = tk.Entry(form_frame)
                entry.pack()
                fields[label_text] = entry
        elif emp_type == "Janitor":
            tk.Label(form_frame, text="Duties").pack()
            entry = tk.Entry(form_frame)
            entry.pack()
            fields["Duties"] = entry

    build_form(emp_type_var.get())
    combo_type.bind("<<ComboboxSelected>>", lambda e: build_form(emp_type_var.get()))

    def save_employee():
        emp_type = emp_type_var.get()
        try:
            common_args = {
                "name": fields["Name"].get(),
                "lname": fields["Last Name"].get(),
                "ncode": fields["National Code"].get(),
                "age": int(fields["Age"].get()),
                "phone": fields["Phone"].get(),
                "address": fields["Address"].get(),
                "salary": int(fields["Salary"].get()),
                "role": fields["Role"].get(),
                "shift": fields["Shift"].get(),
                "edu_level": fields["Education Level"].get(),
                "major": fields["Major"].get(),
                "work_experience": int(fields["Work Experience"].get())
            }

            if emp_type == "SchoolManager":
                SchoolManager(**common_args,
                              license_number=fields["License Number"].get(),
                              room_number=int(fields["Room Number"].get()))
            elif emp_type == "AssistantPrincipal":
                AssistantPrincipal(**common_args,
                                   department=fields["Department"].get(),
                                   teaching_hours=int(fields["Teaching Hours"].get()))
            elif emp_type == "Teacher":
                Teacher(**common_args,
                        subject_name=fields["Subject Name"].get(),
                        teaching_hours=int(fields["Teaching Hours"].get()),
                        teaching_days=int(fields["Teaching Days"].get()),
                        overtime_hours=int(fields["Overtime Hours"].get()))
            elif emp_type == "Janitor":
                Janitor(**common_args, duties=fields["Duties"].get())

            messagebox.showinfo("Success", f"{emp_type} added successfully", parent=win)
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=win)

    tk.Button(win, text="Save Employee", width=25, command=save_employee).pack(pady=5)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=5)


def edit_employee(root=None):
    win = tk.Toplevel(root)
    win.title("Edit Employee")
    win.geometry("500x700")
    win.grab_set()  # Makes the window modal

    tk.Label(win, text="Edit Employee", font=("Arial", 16)).pack(pady=10)
    tk.Label(win, text="Employee ID").pack()
    entry_id = tk.Entry(win)
    entry_id.pack(pady=5)

    form_frame = tk.Frame(win)
    form_frame.pack(pady=10)
    fields = {}

    # نگاشت label به نام واقعی attribute ها
    field_map = {
        "Name": "name",
        "Last Name": "lname",
        "National Code": "ncode",
        "Age": "age",
        "Phone": "phone",
        "Address": "address",
        "Salary": "salary",
        "Role": "role",
        "Shift": "shift",
        "Education Level": "edu_level",
        "Major": "major",
        "Work Experience": "work_experience"
    }

    def search_and_edit():
        try:
            emp_id = int(entry_id.get())
            emp = SchoolEmployee.search_by_id(emp_id)
            if not emp:
                messagebox.showerror("Error", f"Employee with ID {emp_id} not found", parent=win)
                return

            # پاک کردن فرم قبلی
            for widget in form_frame.winfo_children():
                widget.destroy()
            fields.clear()
            win.geometry("500x900")

            # ساخت فیلدهای مشترک
            for label_text in field_map.keys():
                tk.Label(form_frame, text=label_text).pack()
                if label_text == "Role":
                    entry = tk.Entry(form_frame)
                    entry.insert(0, emp.role)
                    entry.config(state="readonly")
                elif label_text == "Shift":
                    entry = ttk.Combobox(form_frame, values=shift_options, state="readonly")
                    entry.set(emp.shift)
                elif label_text == "Education Level":
                    entry = ttk.Combobox(form_frame, values=edu_options, state="readonly")
                    entry.set(emp.edu_level)
                else:
                    entry = tk.Entry(form_frame)
                    attr_name = field_map[label_text]
                    value = getattr(emp, attr_name, "")
                    entry.insert(0, str(value))
                entry.pack()
                fields[label_text] = entry

            # فیلدهای اختصاصی کارمندان
            if isinstance(emp, SchoolManager):
                for label_text in ["License Number", "Room Number"]:
                    tk.Label(form_frame, text=label_text).pack()
                    entry = tk.Entry(form_frame)
                    entry.insert(0, getattr(emp, label_text.lower().replace(" ", "_"), ""))
                    entry.pack()
                    fields[label_text] = entry
            elif isinstance(emp, AssistantPrincipal):
                for label_text in ["Department", "Teaching Hours"]:
                    tk.Label(form_frame, text=label_text).pack()
                    entry = tk.Entry(form_frame)
                    entry.insert(0, getattr(emp, label_text.lower().replace(" ", "_"), ""))
                    entry.pack()
                    fields[label_text] = entry
            elif isinstance(emp, Teacher):
                for label_text in ["Subject Name", "Teaching Hours", "Teaching Days", "Overtime Hours"]:
                    tk.Label(form_frame, text=label_text).pack()
                    entry = tk.Entry(form_frame)
                    entry.insert(0, getattr(emp, label_text.lower().replace(" ", "_"), ""))
                    entry.pack()
                    fields[label_text] = entry
            elif isinstance(emp, Janitor):
                tk.Label(form_frame, text="Duties").pack()
                entry = tk.Entry(form_frame)
                entry.insert(0, getattr(emp, "duties", ""))
                entry.pack()
                fields["Duties"] = entry

            def do_edit():
                try:
                    common_args = {
                        "n_name": fields["Name"].get(),
                        "n_lname": fields["Last Name"].get(),
                        "n_ncode": fields["National Code"].get(),
                        "n_age": int(fields["Age"].get()),
                        "n_phone": fields["Phone"].get(),
                        "n_address": fields["Address"].get(),
                        "n_salary": int(fields["Salary"].get()),
                        "n_role": fields["Role"].get(),
                        "n_shift": fields["Shift"].get(),
                        "n_edu_level": fields["Education Level"].get(),
                        "n_major": fields["Major"].get(),
                        "n_work_experience": int(fields["Work Experience"].get())
                    }

                    if isinstance(emp, SchoolManager):
                        emp.edit(**common_args,
                                 n_license_number=fields["License Number"].get(),
                                 n_room_number=int(fields["Room Number"].get()))
                    elif isinstance(emp, AssistantPrincipal):
                        emp.edit(**common_args,
                                 n_department=fields["Department"].get(),
                                 n_teaching_hours=int(fields["Teaching Hours"].get()))
                    elif isinstance(emp, Teacher):
                        emp.edit(**common_args,
                                 n_subject_name=fields["Subject Name"].get(),
                                 n_teaching_hours=int(fields["Teaching Hours"].get()),
                                 n_teaching_days=int(fields["Teaching Days"].get()),
                                 n_overtime_hours=int(fields["Overtime Hours"].get()))
                    elif isinstance(emp, Janitor):
                        emp.edit(**common_args,
                                 n_duties=fields["Duties"].get())

                    messagebox.showinfo("Success", f"Employee (ID: {emp.em_id}) edited successfully", parent=win)
                    win.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e), parent=win)

            tk.Button(form_frame, text="Save Edit", width=25, command=do_edit).pack(pady=5)

        except ValueError:
            messagebox.showerror("Error", "Employee ID must be a number", parent=win)

    tk.Button(win, text="Search", width=25, command=search_and_edit).pack(pady=5)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=5)


def remove_employee(root=None):
    win = tk.Toplevel(root)
    win.title("Remove Employee")
    win.geometry("400x250")
    win.grab_set()

    tk.Label(win, text="Remove Employee", font=("Arial", 16)).pack(pady=10)
    tk.Label(win, text="Employee Type").pack()
    emp_type_var = tk.StringVar(value="Teacher")
    combo_type = ttk.Combobox(win, textvariable=emp_type_var,
                              values=["SchoolManager", "AssistantPrincipal", "Teacher", "Janitor"],
                              state="readonly")
    combo_type.pack(pady=5)

    tk.Label(win, text="Employee ID").pack()
    entry_id = tk.Entry(win)
    entry_id.pack(pady=5)

    def do_remove():
        try:
            emp_id = int(entry_id.get())
            emp_type = emp_type_var.get()
            role_map = {
                "SchoolManager": "manager",
                "AssistantPrincipal": "assistant principal",
                "Teacher": "Teacher",
                "Janitor": "Janitor"
            }
            real_role = role_map.get(emp_type)

            emp = None
            for e in SchoolEmployee._employees_list:
                if e.em_id == emp_id and e.role == real_role:
                    emp = e
                    break

            if emp is None:
                messagebox.showerror("Error", f"{emp_type} with ID {emp_id} not found", parent=win)
                return

            emp.remove()
            messagebox.showinfo("Success", f"{emp_type} removed successfully", parent=win)
            win.destroy()
        except ValueError:
            messagebox.showerror("Error", "Employee ID must be a number", parent=win)
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=win)

    tk.Button(win, text="Remove", width=25, command=do_remove).pack(pady=10)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=5)


def show_all_employees(root=None):
    win = tk.Toplevel(root)
    win.title("All Employees")
    win.geometry("700x400")
    win.grab_set()

    tk.Label(win, text="All Employees", font=("Arial", 16)).pack(pady=10)
    listbox = tk.Listbox(win, width=120)
    listbox.pack(padx=10, pady=10, fill="both", expand=True)

    all_employees_info = SchoolEmployee.show_all()
    for info in all_employees_info:
        listbox.insert(tk.END, info)

    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=10)


def search_employee(root=None):
    win = tk.Toplevel(root)
    win.title("Search Employee")
    win.geometry("500x600")
    win.grab_set()

    tk.Label(win, text="Search Employee", font=("Arial", 16)).pack(pady=10)
    tk.Label(win, text="Employee ID").pack()
    entry_id = tk.Entry(win)
    entry_id.pack(pady=5)

    result_label = tk.Label(win, text="", justify="left")
    result_label.pack(pady=10)

    def do_search():
        try:
            emp_id = int(entry_id.get())
            emp = SchoolEmployee.search_by_id(emp_id)
            if emp is None:
                result_label.config(text="")
                messagebox.showerror("Error", f"Employee with ID {emp_id} not found", parent=win)
                return

            info = f"ID: {emp.em_id}\nName: {emp.name} {emp.lname}\nRole: {emp.role}\nSalary: {emp.salary}\nShift: {emp.shift}\nEducation: {emp.edu_level} in {emp.major}\nWork Experience: {emp.work_experience} years\n"

            if isinstance(emp, SchoolManager):
                info += f"License Number: {emp.license_number}\nRoom Number: {emp.room_number}"
            elif isinstance(emp, AssistantPrincipal):
                info += f"Department: {emp.department}\nTeaching Hours: {emp.teaching_hours}"
            elif isinstance(emp, Teacher):
                info += f"Subject: {emp.subject_name}\nTeaching Hours: {emp.teaching_hours}\nTeaching Days: {emp.teaching_days}\nOvertime Hours: {emp.overtime_hours}"
            elif isinstance(emp, Janitor):
                info += f"Duties: {emp.duties}"

            result_label.config(text=info)

        except ValueError:
            messagebox.showerror("Error", "Employee ID must be a number", parent=win)
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=win)

    tk.Button(win, text="Search", width=25, command=do_search).pack(pady=5)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=5)
