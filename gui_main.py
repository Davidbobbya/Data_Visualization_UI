import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
import numpy as np
import matplotlib.figure

def plot():
    ax.clear()
    x = np.random.randint(0, 10, 10)
    y = np.random.randint(0, 10, 10)
    ax.plot(x, y)
    canvas.draw()

# Initialize Tkinter and Matplotlib Figure
root = tk.Tk()
fig = plt.Figure()  # Use plt.Figure instead of matplotlib.figure.Figure
ax = fig.add_subplot()

# Tkinter Application
frame = tk.Frame(root)
label = tk.Label(text="Matplotlib + Tkinter!")
label.config(font=("Courier", 32))
label.pack()

# Create Canvas
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, frame)
toolbar.update()
toolbar.pack(anchor="w", fill=tk.X)

frame.pack()

tk.Button(frame, text="Plot Graph", command=plot).pack(pady=10)

root.mainloop()
