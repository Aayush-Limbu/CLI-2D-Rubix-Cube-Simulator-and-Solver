import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def plot_in_tkinter(x, y):
    # Create a matplotlib figure
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(x, y, marker='o')
    ax.set_title("User Input Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    
    # Embed the figure in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def get_user_input():
    # Ask the user for X and Y values through Tkinter dialogs
    x_values = simpledialog.askstring("Input", "Enter X values separated by commas:")
    y_values = simpledialog.askstring("Input", "Enter Y values separated by commas:")
    
    # Convert the string input into lists of floats
    x = list(map(float, x_values.split(',')))
    y = list(map(float, y_values.split(',')))
    
    # Clear previous plots
    for widget in window.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()
    
    # Plot the new data
    plot_in_tkinter(x, y)

# Create the main Tkinter window
window = tk.Tk()
window.title("Matplotlib in Tkinter")

# Add a button to allow user input and trigger plotting
input_button = tk.Button(window, text="Enter Data and Plot", command=get_user_input)
input_button.pack(side=tk.BOTTOM)

# Run the Tkinter event loop
window.mainloop()
