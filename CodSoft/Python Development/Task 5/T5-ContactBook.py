import tkinter as tk
import sqlite3

conn = sqlite3.connect('contacts.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Contacts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT
            )''')
conn.commit()

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    
    c.execute("INSERT INTO Contacts (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    clear_entries()
    display_contacts()

def display_contacts():
    contacts_listbox.delete(0, tk.END)
    c.execute("SELECT name, phone FROM Contacts")
    contacts = c.fetchall()
    for contact in contacts:
        contacts_listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")

def search_contact():
    search_term = search_entry.get()
    c.execute("SELECT name, phone FROM Contacts WHERE name LIKE ? OR phone LIKE ?", (f"%{search_term}%", f"%{search_term}%"))
    results = c.fetchall()
    contacts_listbox.delete(0, tk.END)
    for contact in results:
        contacts_listbox.insert(tk.END, f"{contact[0]} - {contact[1]}")

def update_contact():
    selected_contact = contacts_listbox.get(tk.ACTIVE)
    selected_name, selected_phone = selected_contact.split(" - ")
    updated_name = name_entry.get()
    updated_phone = phone_entry.get()
    
    c.execute("UPDATE Contacts SET name=?, phone=? WHERE name=? AND phone=?", (updated_name, updated_phone, selected_name, selected_phone))
    conn.commit()
    clear_entries()
    display_contacts()

def delete_contact():
    selected_contact = contacts_listbox.get(tk.ACTIVE)
    selected_name, selected_phone = selected_contact.split(" - ")
    c.execute("DELETE FROM Contacts WHERE name=? AND phone=?", (selected_name, selected_phone))
    conn.commit()
    clear_entries()
    display_contacts()

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book")

tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone:").grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=2, column=0, columnspan=2, pady=5)

tk.Label(root, text="Search:").grid(row=3, column=0)
search_entry = tk.Entry(root)
search_entry.grid(row=3, column=1)
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=4, column=0, columnspan=2, pady=5)

contacts_listbox = tk.Listbox(root, width=40)
contacts_listbox.grid(row=5, column=0, columnspan=2)
display_contacts()

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=6, column=0, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=6, column=1, pady=5)

root.mainloop()
