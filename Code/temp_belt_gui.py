import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass

@dataclass
class Belt:
    belt_type: str
    width: float
    tension: float

    density: float

# Dictionary to store belt specifications
belt_specs = {
    'GT2': {
        6.0: {'tension': 50.0, 'density': 1.2},
        9.0: {'tension': 55.0, 'density': 1.25},
        12.0: {'tension': 60.0, 'density': 1.3},
    },
    'GT3': {
        6.0: {'tension': 60.0, 'density': 1.3},
        9.0: {'tension': 65.0, 'density': 1.35},
        12.0: {'tension': 70.0, 'density': 1.4},
    }
}

def create_belt(belt_type: str, width: float) -> Belt:
    if belt_type in belt_specs and width in belt_specs[belt_type]:
        specs = belt_specs[belt_type][width]
        return Belt(belt_type=belt_type, width=width, tension=specs['tension'], density=specs['density'])
    else:
        raise ValueError("Invalid belt type or width")

def on_submit():
    belt_type = belt_type_var.get()
    width = float(width_var.get())
    try:
        belt = create_belt(belt_type, width)
        result_var.set(f"Tension: {belt.tension} N, Density: {belt.density} g/cm³")
    except ValueError as e:
        result_var.set(str(e))

# Creating the main window
root = tk.Tk()
root.title("Belt Specifications")

# Creating input fields
belt_type_var = tk.StringVar()
width_var = tk.StringVar()
result_var = tk.StringVar()

ttk.Label(root, text="Belt Type:").grid(column=0, row=0, padx=10, pady=10)
belt_type_combobox = ttk.Combobox(root, textvariable=belt_type_var)
belt_type_combobox['values'] = list(belt_specs.keys())
belt_type_combobox.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Width (mm):").grid(column=0, row=1, padx=10, pady=10)
width_combobox = ttk.Combobox(root, textvariable=width_var)
width_combobox['values'] = [6.0, 9.0, 12.0]
width_combobox.grid(column=1, row=1, padx=10, pady=10)

# Submit button
submit_button = ttk.Button(root, text="Submit", command=on_submit)
submit_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

# Result display
result_label = ttk.Label(root, textvariable=result_var)
result_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Run the GUI loop
root.mainloop()
