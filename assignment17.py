import tkinter as tk
from tkinter import messagebox

# Function
def show_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name!")
    else:
        # Dummy Weather Data
        result.config(
            text=f"Weather Report\n\n"
                 f"City : {city}\n"
                 f"Temperature : 30°C\n"
                 f"Condition : Sunny"
        )

# Main Window
root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")
root.resizable(False, False)

# Heading
title = tk.Label(root, text="Weather App", font=("Arial", 18, "bold"))
title.pack(pady=10)

# City Label
label = tk.Label(root, text="Enter City Name:")
label.pack()

# Entry Box
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Button
btn = tk.Button(root, text="Get Weather", command=show_weather)
btn.pack(pady=10)

# Result Label
result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=10)

# Run
root.mainloop()
