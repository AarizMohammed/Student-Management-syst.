import tkinter as tk
from tkinter import StringVar

class Student:
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year

class StudentApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Students - Aariz")
        self.master.geometry("500x400")

        self.selected_year = StringVar()  # Added this line

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.age_label = tk.Label(master, text="Age:")
        self.age_label.grid(row=1, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(master)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        self.year_label = tk.Label(master, text="Year:")
        self.year_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.year_1_button = tk.Radiobutton(master, text="First", variable=self.selected_year, value="First Year")
        self.year_1_button.grid(row=2, column=1)

        self.year_2_button = tk.Radiobutton(master, text="Second", variable=self.selected_year, value="Second Year")
        self.year_2_button.grid(row=3, column=1, padx=10, pady=10)

        self.year_3_button = tk.Radiobutton(master, text="Third", variable=self.selected_year, value="Third Year")
        self.year_3_button.grid(row=4, column=1, padx=10, pady=10)

        self.year_4_button = tk.Radiobutton(master, text="Fourth", variable=self.selected_year, value="Fourth Year")
        self.year_4_button.grid(row=5, column=1, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add", command=self.add_student)
        self.add_button.grid(row=6, column=1)

        self.students_listbox = tk.Listbox(master)
        self.students_listbox.grid(row=1, column=3, columnspan=5,rowspan= 10, padx=10, pady=10, sticky="nsew")
        self.list_label = tk.Label(master, text="Recorded Students:")
        self.list_label.grid(row=0, column=3, columnspan=5, pady=5)

        self.students_list = []

    def add_student(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        year = self.selected_year.get()

        if name and age and year:
            student_obj = Student(name, age, year)
            self.students_list.append(student_obj)

            # Update listbox
            self.students_listbox.insert(tk.END, f"{name} - {age} years old - {year}")
            print(f"Student added: {name}, {age} years old, {year}")
        else:
            print("Please fill in all fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
