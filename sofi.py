import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from datetime import datetime

# Database Setup
def initialize_db():
    conn = sqlite3.connect("school_supplies.db")
    cursor = conn.cursor()

    # Creating tables if they don't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        grade TEXT NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        id INTEGER PRIMARY KEY,
                        item_name TEXT NOT NULL,
                        quantity INTEGER NOT NULL
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS distribution (
                        id INTEGER PRIMARY KEY,
                        student_id INTEGER,
                        item_id INTEGER,
                        quantity INTEGER,
                        date TEXT,
                        FOREIGN KEY(student_id) REFERENCES students(id),
                        FOREIGN KEY(item_id) REFERENCES inventory(id)
                    )''')
    conn.commit()
    conn.close()

# Functionality
class SchoolSupplySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Tools for Tomorrow: School Supplies System")

        # Create Tabs
        tabControl = ttk.Notebook(self.root)
        self.student_tab = ttk.Frame(tabControl)
        self.inventory_tab = ttk.Frame(tabControl)
        self.distribution_tab = ttk.Frame(tabControl)

        tabControl.add(self.student_tab, text='Student Management')
        tabControl.add(self.inventory_tab, text='Inventory Management')
        tabControl.add(self.distribution_tab, text='Distribution Management')
        tabControl.pack(expand=1, fill="both")

        # Initialize Components
        self.student_management()
        self.inventory_management()
        self.distribution_management()

    # Student Management Tab
    def student_management(self):
        # Add student
        self.student_name = tk.StringVar()
        self.student_grade = tk.StringVar()

        tk.Label(self.student_tab, text="Student Name:").grid(row=0, column=0)
        tk.Entry(self.student_tab, textvariable=self.student_name).grid(row=0, column=1)

        tk.Label(self.student_tab, text="Grade:").grid(row=1, column=0)
        tk.Entry(self.student_tab, textvariable=self.student_grade).grid(row=1, column=1)

        tk.Button(self.student_tab, text="Add Student", command=self.add_student).grid(row=2, column=0, columnspan=2)

        # Student List
        self.student_tree = ttk.Treeview(self.student_tab, columns=('ID', 'Name', 'Grade'), show='headings')
        self.student_tree.heading('ID', text='ID')
        self.student_tree.heading('Name', text='Name')
        self.student_tree.heading('Grade', text='Grade')
        self.student_tree.grid(row=3, column=0, columnspan=2)
        self.load_students()

    def add_student(self):
        name = self.student_name.get()
        grade = self.student_grade.get()
        if name and grade:
            conn = sqlite3.connect("school_supplies.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
            conn.commit()
            conn.close()
            self.load_students()
        else:
            messagebox.showerror("Input Error", "Please enter both name and grade.")

    def load_students(self):
        self.student_tree.delete(*self.student_tree.get_children())
        conn = sqlite3.connect("school_supplies.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            self.student_tree.insert('', tk.END, values=row)
        conn.close()

    # Inventory Management Tab
    def inventory_management(self):
        # Add inventory
        self.item_name = tk.StringVar()
        self.item_quantity = tk.IntVar()

        tk.Label(self.inventory_tab, text="Item Name:").grid(row=0, column=0)
        tk.Entry(self.inventory_tab, textvariable=self.item_name).grid(row=0, column=1)

        tk.Label(self.inventory_tab, text="Quantity:").grid(row=1, column=0)
        tk.Entry(self.inventory_tab, textvariable=self.item_quantity).grid(row=1, column=1)

        tk.Button(self.inventory_tab, text="Add Item", command=self.add_inventory).grid(row=2, column=0, columnspan=2)

        # Inventory List
        self.inventory_tree = ttk.Treeview(self.inventory_tab, columns=('ID', 'Item', 'Quantity'), show='headings')
        self.inventory_tree.heading('ID', text='ID')
        self.inventory_tree.heading('Item', text='Item Name')
        self.inventory_tree.heading('Quantity', text='Quantity')
        self.inventory_tree.grid(row=3, column=0, columnspan=2)
        self.load_inventory()

    def add_inventory(self):
        item_name = self.item_name.get()
        quantity = self.item_quantity.get()
        if item_name and quantity:
            conn = sqlite3.connect("school_supplies.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO inventory (item_name, quantity) VALUES (?, ?)", (item_name, quantity))
            conn.commit()
            conn.close()
            self.load_inventory()
        else:
            messagebox.showerror("Input Error", "Please enter both item name and quantity.")

    def load_inventory(self):
        self.inventory_tree.delete(*self.inventory_tree.get_children())
        conn = sqlite3.connect("school_supplies.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory")
        for row in cursor.fetchall():
            self.inventory_tree.insert('', tk.END, values=row)
        conn.close()

    # Distribution Management Tab
    def distribution_management(self):
        self.student_id = tk.StringVar()
        self.item_id = tk.StringVar()
        self.distribute_quantity = tk.IntVar()

        tk.Label(self.distribution_tab, text="Student ID:").grid(row=0, column=0)
        tk.Entry(self.distribution_tab, textvariable=self.student_id).grid(row=0, column=1)

        tk.Label(self.distribution_tab, text="Item ID:").grid(row=1, column=0)
        tk.Entry(self.distribution_tab, textvariable=self.item_id).grid(row=1, column=1)

        tk.Label(self.distribution_tab, text="Quantity:").grid(row=2, column=0)
        tk.Entry(self.distribution_tab, textvariable=self.distribute_quantity).grid(row=2, column=1)

        tk.Button(self.distribution_tab, text="Distribute", command=self.distribute_items).grid(row=3, column=0, columnspan=2)

    def distribute_items(self):
        student_id = self.student_id.get()
        item_id = self.item_id.get()
        quantity = self.distribute_quantity.get()
        date = datetime.now().strftime("%Y-%m-%d")

        if student_id and item_id and quantity > 0:
            # Check if student_id and item_id exist in database
            conn = sqlite3.connect("school_supplies.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
            if cursor.fetchone() is None:
                messagebox.showerror("Student Not Found", "The student ID does not exist.")
                conn.close()
                return

            cursor.execute("SELECT * FROM inventory WHERE id=?", (item_id,))
            item = cursor.fetchone()
            if item is None:
                messagebox.showerror("Item Not Found", "The item ID does not exist.")
                conn.close()
                return

            # Check if enough quantity is available
            available_quantity = item[2]  # Inventory quantity is the 3rd column
            if available_quantity < quantity:
                messagebox.showerror("Insufficient Inventory", "Not enough items in inventory.")
                conn.close()
                return

            # Insert distribution record
            cursor.execute("INSERT INTO distribution (student_id, item_id, quantity, date) VALUES (?, ?, ?, ?)",
                           (student_id, item_id, quantity, date))
            cursor.execute("UPDATE inventory SET quantity = quantity - ? WHERE id=?", (quantity, item_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Item distributed successfully!")
        else:
            messagebox.showerror("Input Error", "Please fill all fields with valid data.")

# Main Application
if __name__ == "__main__":
    initialize_db()  # Initialize the database
    root = tk.Tk()
    app = SchoolSupplySystem(root)  # Create the app instance
    root.mainloop()  # Start the Tkinter main loop


    