import tkinter as tk
from tkinter import messagebox, ttk
from models.Student import Student

def Add_s():
    win = tk.Toplevel()
    win.title("Add Student")
    win.geometry("420x500")
    win.grab_set()  # Modal

    tk.Label(win, text="Add New Student", font=("Arial", 16)).pack(pady=10)

    form = tk.Frame(win)
    form.pack(pady=10)

    tk.Label(form, text="Name").pack()
    entry_name = tk.Entry(form)
    entry_name.pack()

    tk.Label(form, text="Last Name").pack()
    entry_lname = tk.Entry(form)
    entry_lname.pack()

    tk.Label(form, text="National Code").pack()
    entry_ncode = tk.Entry(form)
    entry_ncode.pack()

    tk.Label(form, text="Age").pack()
    entry_age = tk.Entry(form)
    entry_age.pack()

    tk.Label(form, text="Phone").pack()
    entry_phone = tk.Entry(form)
    entry_phone.pack()

    tk.Label(form, text="Address").pack()
    entry_address = tk.Entry(form)
    entry_address.pack()

    tk.Label(form, text="Grade").pack()
    grade_var = tk.StringVar(value="7")
    combo_grade = ttk.Combobox(form, textvariable=grade_var, values=["7", "8", "9"], state="readonly")
    combo_grade.pack()

    def save_student():
        try:
            Student(
                classroom_id="Unknown",
                name=entry_name.get(),
                lname=entry_lname.get(),
                ncode=entry_ncode.get(),
                age=int(entry_age.get()),
                phone=entry_phone.get(),
                address=entry_address.get(),
                grade=int(grade_var.get())
            )
            messagebox.showinfo("Success", "Student added successfully", parent=win)
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e), parent=win)

    tk.Button(win, text="Save Student", width=25, command=save_student).pack(pady=5)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=5)


def Show_all_students():
    win = tk.Toplevel()
    win.title("All Students")
    win.geometry("600x400")
    win.grab_set()

    tk.Label(win, text="All Students", font=("Arial", 16)).pack(pady=10)

    listbox = tk.Listbox(win, width=100)
    listbox.pack(padx=10, pady=10, fill="both", expand=True)

    all_students = Student.show_all()
    for s in all_students:
        listbox.insert(tk.END, s)

    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=10)


def search_student():
    win = tk.Toplevel()
    win.title("Search Student")
    win.geometry("400x350")
    win.grab_set()

    tk.Label(win, text="Search Student", font=("Arial", 16)).pack(pady=10)

    tk.Label(win, text="Student ID").pack()
    entry_id = tk.Entry(win)
    entry_id.pack()

    result_label = tk.Label(win, text="", justify="left")
    result_label.pack(pady=10)

    def do_search():
        try:
            student_id = int(entry_id.get())
            student = Student.search_by_id(student_id)
            if student is None:
                messagebox.showerror("Error", "Student not found", parent=win)
                result_label.configure(text="")
            else:
                result_label.config(
                    text=
                    f"ID: {student.student_id}\n"
                    f"Name: {student.name}\n"
                    f"Last Name: {student.lname}\n"
                    f"Grade: {student.grade}\n"
                    f"Age: {student.age}\n"
                    f"Phone: {student.phone}\n"
                    f"Address: {student.address}"
                )
        except ValueError:
            messagebox.showerror("Error", "Student ID must be a number", parent=win)

    tk.Button(win, text="Search", width=25, command=do_search).pack(pady=5)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=5)


def remove_student():
    win = tk.Toplevel()
    win.title("Remove Student")
    win.geometry("400x250")
    win.grab_set()

    tk.Label(win, text="Remove Student", font=("Arial", 16)).pack(pady=10)

    tk.Label(win, text="Student ID").pack()
    entry_id = tk.Entry(win)
    entry_id.pack()

    def do_remove():
        try:
            student_id = int(entry_id.get())
            student = Student.search_by_id(student_id)
            if student is None:
                messagebox.showerror("Error", "Student not found", parent=win)
            else:
                student.remove()
                messagebox.showinfo("Success", "Student removed successfully", parent=win)
                win.destroy()
        except ValueError:
            messagebox.showerror("Error", "Student ID must be a number", parent=win)

    tk.Button(win, text="Remove", width=25, command=do_remove).pack(pady=5)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack()


def edit_student():
    win = tk.Toplevel()
    win.title('Edit Student')
    win.geometry("400x250")
    win.grab_set()

    tk.Label(win, text="Edit Student", font=("Arial", 16)).pack(pady=10)
    tk.Label(win, text="Student ID").pack()
    entry_id = tk.Entry(win)
    entry_id.pack()

    result_label = tk.Label(win, text="")
    result_label.pack(pady=10)

    def search_and_edit():
        try:
            student_id = int(entry_id.get())
            student = Student.search_by_id(student_id)
            if student is None:
                messagebox.showerror("Error", "Student not found", parent=win)
                return

            win.geometry("400x600")
            form = tk.Frame(win)
            form.pack(pady=10)

            tk.Label(form, text="Name").pack()
            entry_name = tk.Entry(form)
            entry_name.pack()
            entry_name.insert(0, student.name)

            tk.Label(form, text="Last Name").pack()
            entry_lname = tk.Entry(form)
            entry_lname.pack()
            entry_lname.insert(0, student.lname)

            tk.Label(form, text="National Code").pack()
            entry_ncode = tk.Entry(form)
            entry_ncode.pack()
            entry_ncode.insert(0, student.ncode)

            tk.Label(form, text="Age").pack()
            entry_age = tk.Entry(form)
            entry_age.pack()
            entry_age.insert(0, str(student.age))

            tk.Label(form, text="Phone").pack()
            entry_phone = tk.Entry(form)
            entry_phone.pack()
            entry_phone.insert(0, student.phone)

            tk.Label(form, text="Address").pack()
            entry_address = tk.Entry(form)
            entry_address.pack()
            entry_address.insert(0, student.address)

            tk.Label(form, text="Grade").pack()
            grade_var = tk.StringVar(value=str(student.grade))
            combo_grade = ttk.Combobox(form, textvariable=grade_var, values=["7", "8", "9"], state="readonly")
            combo_grade.pack()

            def do_edit():
                try:
                    student.edit(
                        n_name=entry_name.get(),
                        n_lname=entry_lname.get(),
                        n_ncode=entry_ncode.get(),
                        n_age=int(entry_age.get()),
                        n_phone=entry_phone.get(),
                        n_address=entry_address.get(),
                        n_grade=int(grade_var.get())
                    )
                    messagebox.showinfo("Success", "Student edited successfully", parent=win)
                    win.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e), parent=win)

            tk.Button(form, text="Edit", width=25, command=do_edit).pack(pady=5)

        except ValueError:
            messagebox.showerror("Error", "Student ID must be a number", parent=win)

    tk.Button(win, text="Search", width=25, command=search_and_edit).pack(pady=5)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=5)
