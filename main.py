from ttkbootstrap import Window, Style
from ttkbootstrap.widgets import Entry, Label, Button, Progressbar
from tkinter import messagebox
from pymongo import MongoClient
from datetime import date

# MongoDB setup
client = MongoClient("localhost", 27017)
db = client["superhuman"]
diet_collection = db["diet"]
exercise_collection = db["exercise"]
sleep_collection = db["sleep"]

# Tkinter Window with Modern Theme
app = Window(title="Superhuman Tracker", themename="cosmo")
app.geometry("500x600")
app.resizable(False, False)
app.iconbitmap("D:\Coding\superhuman\man.ico")


# Clear current UI
def clear_ui():
    for widget in app.winfo_children():
        widget.destroy()

# Show loading bar
def show_loading(duration=1000, callback=None):
    progress = Progressbar(app, mode='indeterminate', length=200, bootstyle="info")
    progress.pack(pady=10)
    progress.start()

    def stop_and_continue():
        progress.stop()
        progress.destroy()
        if callback:
            callback()
    app.after(duration, stop_and_continue)

# --- Main Menu ---
def main_menu():
    clear_ui()
    Label(app, text="Superhuman Tracker", font=("Helvetica", 18, "bold")).pack(pady=20)

    Button(app, text="Log Diet 🥗", bootstyle="success", width=30, command=show_diet_form).pack(pady=10)
    Button(app, text="Log Exercise 💪", bootstyle="warning", width=30, command=show_exercise_form).pack(pady=10)
    Button(app, text="Log Sleep 😴", bootstyle="primary", width=30, command=show_sleep_form).pack(pady=10)

# --- Diet Form ---
def show_diet_form():
    clear_ui()
    Label(app, text="🥗 Diet Data", font=("Helvetica", 16)).pack(pady=10)

    fields = ["Calories", "Protein", "Carbs", "Fiber", "Fat"]
    entries = {}

    for field in fields:
        Label(app, text=field).pack()
        ent = Entry(app)
        ent.pack()
        entries[field.lower()] = ent

    def submit_diet():
        try:
            diet_doc = {key: int(ent.get()) for key, ent in entries.items()}
            diet_doc["date"] = date.today().isoformat()
            show_loading(callback=lambda: finish_insert(diet_collection, diet_doc))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    Button(app, text="Submit", bootstyle="success", command=submit_diet).pack(pady=10)
    Button(app, text="⬅ Back", bootstyle="secondary", command=main_menu).pack()

# --- Exercise Form ---
def show_exercise_form():
    clear_ui()
    Label(app, text="💪 Exercise Data", font=("Helvetica", 16)).pack(pady=10)

    fields = ["Face Ice (min)", "Pushups", "Pullups", "Plank", "Reverse Plank", "Calf Raises", "Squats"]
    keys = ["face_ice", "pushup", "pullup", "plank", "reverse_plank", "calf_raises", "squat"]
    entries = {}

    for field, key in zip(fields, keys):
        Label(app, text=field).pack()
        ent = Entry(app)
        ent.pack()
        entries[key] = ent

    def submit_exercise():
        try:
            exercise_doc = {key: int(ent.get()) for key, ent in entries.items()}
            exercise_doc["date"] = date.today().isoformat()
            show_loading(callback=lambda: finish_insert(exercise_collection, exercise_doc))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    Button(app, text="Submit", bootstyle="success", command=submit_exercise).pack(pady=10)
    Button(app, text="⬅ Back", bootstyle="secondary", command=main_menu).pack()

# --- Sleep Form ---
def show_sleep_form():
    clear_ui()
    Label(app, text="😴 Sleep Data", font=("Helvetica", 16)).pack(pady=10)
    Label(app, text="Hours of Sleep").pack()
    sleep_entry = Entry(app)
    sleep_entry.pack()

    def submit_sleep():
        try:
            hours = float(sleep_entry.get())
            sleep_doc = {"hours": hours, "date": date.today().isoformat()}
            show_loading(callback=lambda: finish_insert(sleep_collection, sleep_doc))
        except ValueError:
            messagebox.showerror("Error", "Enter a valid float for sleep hours.")

    Button(app, text="Submit", bootstyle="success", command=submit_sleep).pack(pady=10)
    Button(app, text="⬅ Back", bootstyle="secondary", command=main_menu).pack()

# --- Success Handler ---
def finish_insert(collection, doc):
    collection.insert_one(doc)
    messagebox.showinfo("Success", "✅ Data inserted successfully!")
    main_menu()

# Start App
main_menu()
app.mainloop()
