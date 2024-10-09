import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# File to store user BMI data
DATA_FILE = "bmi_data.csv"

# Function to calculate BMI and display the result
def calculate_bmi():
    try:
        # Get user input
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters

        # Calculate BMI
        bmi = round(weight / (height ** 2), 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        # Display BMI and category
        result_label.config(text=f"BMI: {bmi} ({category})")
        save_bmi_data(weight, height * 100, bmi, category)

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric values for weight and height.")

# Function to save the calculated BMI to a CSV file
def save_bmi_data(weight, height, bmi, category):
    # Get the user's name and current date
    name = name_entry.get()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a DataFrame for the new entry
    new_entry = pd.DataFrame([[name, date, weight, height, bmi, category]],
                             columns=["Name", "Date", "Weight (kg)", "Height (cm)", "BMI", "Category"])

    try:
        # Append new entry to the existing CSV file or create a new one
        with open(DATA_FILE, 'a') as f:
            new_entry.to_csv(f, header=f.tell() == 0, index=False)
        messagebox.showinfo("Success", "BMI data saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

# Function to view historical BMI data for the entered user
def view_history():
    try:
        name = name_entry.get()
        if not name:
            messagebox.showwarning("Warning", "Please enter a name to view history.")
            return

        # Read data from CSV
        df = pd.read_csv(DATA_FILE)

        # Filter data for the given name
        user_data = df[df["Name"] == name]

        if user_data.empty:
            messagebox.showinfo("No data", f"No historical data found for {name}.")
            return

        # Display historical data in a new window
        history_window = tk.Toplevel(root)
        history_window.title(f"{name}'s BMI History")

        text = tk.Text(history_window)
        text.insert(tk.END, user_data.to_string(index=False))
        text.pack()

    except FileNotFoundError:
        messagebox.showerror("Error", "No historical data file found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read data: {e}")

# Function to display BMI trend graph for the entered user
def view_trend():
    try:
        name = name_entry.get()
        if not name:
            messagebox.showwarning("Warning", "Please enter a name to view trend.")
            return

        # Read data from CSV
        df = pd.read_csv(DATA_FILE)

        # Filter data for the given name
        user_data = df[df["Name"] == name]

        if user_data.empty:
            messagebox.showinfo("No data", f"No historical data found for {name}.")
            return

        # Plot BMI trend over time
        plt.figure(figsize=(10, 5))
        plt.plot(pd.to_datetime(user_data["Date"]), user_data["BMI"], marker='o', linestyle='-')
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.title(f"BMI Trend for {name}")
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        messagebox.showerror("Error", "No historical data file found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to plot data: {e}")

# Initialize main application window
root = tk.Tk()
root.title("BMI Calculator with Data Storage and Analysis")
root.geometry("500x400")

# User input fields for weight, height, and name
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root, width=30)
weight_entry.pack(pady=5)

tk.Label(root, text="Height (cm):").pack(pady=5)
height_entry = tk.Entry(root, width=30)
height_entry.pack(pady=5)

# Button to calculate BMI
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Button to view history and trend
tk.Button(root, text="View History", command=view_history).pack(pady=5)
tk.Button(root, text="View BMI Trend", command=view_trend).pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
