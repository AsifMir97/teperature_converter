import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_to_fahrenheit():
    try:
        celsius = float(temperature_entry.get())
        fahrenheit = celsius_to_fahrenheit(celsius)
        fahrenheit_label.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        fahrenheit_label.config(text="Invalid input")

def convert_to_celsius():
    try:
        fahrenheit = float(temperature_entry.get())
        celsius = fahrenheit_to_celsius(fahrenheit)
        celsius_label.config(text=f"{celsius:.2f} °C")
    except ValueError:
        celsius_label.config(text="Invalid input")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")
root.minsize(250, 150)  # Set a minimum size to prevent too small resizing

# Create and place widgets
tk.Label(root, text="Temperature:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
temperature_entry = tk.Entry(root)
temperature_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

tk.Button(root, text="Convert to Fahrenheit", command=convert_to_fahrenheit).grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
fahrenheit_label = tk.Label(root, text="")
fahrenheit_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

tk.Button(root, text="Convert to Celsius", command=convert_to_celsius).grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
celsius_label = tk.Label(root, text="")
celsius_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Configure grid weights to make the window responsive
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)
root.grid_rowconfigure(3, weight=0)
root.grid_rowconfigure(4, weight=1)

root.mainloop()