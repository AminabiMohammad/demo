import tkinter as tk
from tkinter import messagebox

class HealthTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Health Tracker App")
        self.master.geometry("400x400")
        self.master.configure(bg="#f0f0f0")

        self.height_label = tk.Label(master, text="Enter Height (cm):", bg="#f0f0f0")
        self.height_label.pack(pady=10)

        self.height_entry = tk.Entry(master)
        self.height_entry.pack()

        self.weight_label = tk.Label(master, text="Enter Weight (kg):", bg="#f0f0f0")
        self.weight_label.pack(pady=10)

        self.weight_entry = tk.Entry(master)
        self.weight_entry.pack()

        self.activity_label = tk.Label(master, text="Select Daily Activity Level:", bg="#f0f0f0")
        self.activity_label.pack(pady=10)

        self.activity_var = tk.StringVar()
        self.activity_var.set("Moderate")  # Default value

        activity_options = ["Sedentary", "Light", "Moderate", "Active", "Very Active"]
        for option in activity_options:
            rb = tk.Radiobutton(master, text=option, variable=self.activity_var, value=option, bg="#f0f0f0")
            rb.pack(anchor=tk.W)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_health, bg="#4CAF50", fg="white")
        self.calculate_button.pack(pady=20)

    def calculate_health(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            activity_level = self.activity_var.get()

            bmi = weight / ((height / 100) ** 2)
            calories_burned = self.calculate_calories_burned(weight, height, activity_level)

            messagebox.showinfo("Health Details", f"BMI: {bmi:.2f}\nEstimated Calories Burned: {calories_burned:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid height and weight!")

    def calculate_calories_burned(self, weight, height, activity_level):
        # Assuming a simplified calculation for calories burned based on activity level
        activity_levels = {
            "Sedentary": 1.2,
            "Light": 1.375,
            "Moderate": 1.55,
            "Active": 1.725,
            "Very Active": 1.9
        }
        basal_metabolic_rate = 10 * weight + 6.25 * height - 5 * 25 + 5  # Simplified BMR calculation for a 25-year-old person
        calories_burned = basal_metabolic_rate * activity_levels[activity_level]
        return calories_burned

def main():
    root = tk.Tk()
    app = HealthTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
