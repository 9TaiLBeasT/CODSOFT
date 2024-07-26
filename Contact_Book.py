import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ContactManager:
    def __init__(self, root):
        self.contacts = {}
        self.root = root
        self.root.title("Contact Manager")
        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)
        
        self.label = tk.Label(self.frame, text="Contact Manager", font=("Arial", 18))
        self.label.pack(pady=10)
        
        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)
        
        self.view_button = tk.Button(self.frame, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)
        
        self.search_button = tk.Button(self.frame, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)
        
        self.update_button = tk.Button(self.frame, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)
        
        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)
    
    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        phone = simpledialog.askstring("Input", "Enter contact phone number:")
        email = simpledialog.askstring("Input", "Enter contact email:")
        address = simpledialog.askstring("Input", "Enter contact address:")
        
        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required.")
    
    def view_contacts(self):
        contact_list = ""
        for name, details in self.contacts.items():
            contact_list += f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n\n"
        
        if contact_list:
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "No contacts available.")
    
    def search_contact(self):
        search_name = simpledialog.askstring("Input", "Enter contact name to search:")
        
        if search_name in self.contacts:
            details = self.contacts[search_name]
            contact_info = f"Name: {search_name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}"
            messagebox.showinfo("Contact Details", contact_info)
        else:
            messagebox.showwarning("Not Found", "Contact not found.")
    
    def update_contact(self):
        update_name = simpledialog.askstring("Input", "Enter contact name to update:")
        
        if update_name in self.contacts:
            phone = simpledialog.askstring("Input", "Enter new phone number:", initialvalue=self.contacts[update_name]['phone'])
            email = simpledialog.askstring("Input", "Enter new email:", initialvalue=self.contacts[update_name]['email'])
            address = simpledialog.askstring("Input", "Enter new address:", initialvalue=self.contacts[update_name]['address'])
            
            self.contacts[update_name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")
    
    def delete_contact(self):
        delete_name = simpledialog.askstring("Input", "Enter contact name to delete:")
        
        if delete_name in self.contacts:
            del self.contacts[delete_name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
