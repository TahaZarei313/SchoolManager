import tkinter as tk
from tkinter import messagebox
from models.member import *

def add_member(root=None):
    win = tk.Toplevel(root)
    win.title("Add Member")
    win.geometry("420x600")
    win.grab_set()

    tk.Label(win, text="Add New Member", font=("Arial", 16)).pack(pady=10)
    form = tk.Frame(win)
    form.pack(pady=10)

    def field(label):
        tk.Label(form, text=label).pack()
        e = tk.Entry(form)
        e.pack()
        return e

    entry_name = field("Name")
    entry_lname = field("Last Name")
    entry_ncode = field("National Code")
    entry_age = field("Age")
    entry_phone = field("Phone")
    entry_address = field("Address")
    entry_membership = field("Membership Number")
    entry_username = field("Username")
    entry_password = field("Password")

    def save_member():
        try:
            Member(
                name=entry_name.get(),
                lname=entry_lname.get(),
                ncode=entry_ncode.get(),
                age=int(entry_age.get()),
                phone=entry_phone.get(),
                address=entry_address.get(),
                membership_num=entry_membership.get(),
                username=entry_username.get(),
                password=entry_password.get()
            )
            messagebox.showinfo("Success", "Member added successfully")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save Member", width=25, command=save_member).pack(pady=5)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=5)


def show_all_members(root=None):
    win = tk.Toplevel(root)
    win.title("All Members")
    win.geometry("600x400")
    win.grab_set()

    tk.Label(win, text="All Members", font=("Arial", 16)).pack(pady=10)
    listbox = tk.Listbox(win, width=100)
    listbox.pack(padx=10, pady=10, fill="both", expand=True)

    for m in Member.show_all():
        listbox.insert(tk.END, m)

    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=10)


def search_member(root=None):
    win = tk.Toplevel(root)
    win.title("Search Member")
    win.geometry("400x350")
    win.grab_set()

    tk.Label(win, text="Search Member", font=("Arial", 16)).pack(pady=10)
    tk.Label(win, text="Membership Number").pack()
    entry_id = tk.Entry(win)
    entry_id.pack()
    result = tk.Label(win, justify="left")
    result.pack(pady=10)

    def do_search():
        member = Member.search_by_membership_num(entry_id.get())
        if member is None:
            messagebox.showerror("Error", "Member not found")
            result.config(text="")
        else:
            result.config(
                text=(
                    f"Name: {member.name}\n"
                    f"Last Name: {member.lname}\n"
                    f"National Code: {member.ncode}\n"
                    f"Age: {member.age}\n"
                    f"Phone: {member.phone}\n"
                    f"Address: {member.address}\n"
                    f"Membership: {member.membership_num}"
                )
            )

    tk.Button(win, text="Search", width=25, command=do_search).pack(pady=5)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=5)


def remove_member(root=None):
    win = tk.Toplevel(root)
    win.title("Remove Member")
    win.geometry("400x250")
    win.grab_set()

    tk.Label(win, text="Remove Member", font=("Arial", 16)).pack(pady=10)
    tk.Label(win, text="Membership Number").pack()
    entry_id = tk.Entry(win)
    entry_id.pack()

    def do_remove():
        member = Member.search_by_membership_num(entry_id.get())
        if member is None:
            messagebox.showerror("Error", "Member not found")
        else:
            member.remove()
            messagebox.showinfo("Success", "Member removed")
            win.destroy()

    tk.Button(win, text="Remove", width=25, command=do_remove).pack(pady=5)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=5)


def edit_member(root=None):
    win = tk.Toplevel(root)
    win.title("Edit Member")
    win.geometry("400x300")
    win.grab_set()

    tk.Label(win, text="Edit Member", font=("Arial", 16)).pack(pady=10)
    tk.Label(win, text="Membership Number").pack()
    entry_id = tk.Entry(win)
    entry_id.pack()

    form_frame = tk.Frame(win)
    form_frame.pack(pady=10)

    def search_and_edit():
        # پاک کردن فرم قبلی
        for widget in form_frame.winfo_children():
            widget.destroy()

        member = Member.search_by_membership_num(entry_id.get())
        if member is None:
            messagebox.showerror("Error", "Member not found")
            return

        win.geometry("400x650")

        def field(label, value=""):
            tk.Label(form_frame, text=label).pack()
            e = tk.Entry(form_frame)
            e.pack()
            e.insert(0, value)
            return e

        entry_name = field("Name", member.name)
        entry_lname = field("Last Name", member.lname)
        entry_phone = field("Phone", member.phone)
        entry_address = field("Address", member.address)
        entry_membership = field("Membership Number", member.membership_num)
        entry_username = field("Username", getattr(member, "username", ""))
        entry_password = field("Password", "")

        def do_edit():
            try:
                member.edit(
                    n_name=entry_name.get(),
                    n_lname=entry_lname.get(),
                    n_phone=entry_phone.get(),
                    n_address=entry_address.get(),
                    n_membership_num=entry_membership.get(),
                    n_username=entry_username.get(),
                    n_password=entry_password.get()
                )
                messagebox.showinfo("Success", "Member edited successfully")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(form_frame, text="Save Edit", width=25, command=do_edit).pack(pady=5)

    tk.Button(win, text="Search", width=25, command=search_and_edit).pack(pady=5)
    tk.Button(win, text="Close", width=25, command=win.destroy).pack(pady=5)
