import tkinter as tk
from tkinter import ttk
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Sorting Algorithms with Visualization
def bubble_sort(arr, canvas, bars):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                update_bars(canvas, bars, arr)

def merge_sort(arr, canvas, bars):
    def merge(left, right):
        sorted_arr = []
        while left and right:
            if left[0] < right[0]:
                sorted_arr.append(left.pop(0))
            else:
                sorted_arr.append(right.pop(0))
        return sorted_arr + left + right
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid], canvas, bars)
        right = merge_sort(arr[mid:], canvas, bars)
        return merge(left, right)
    return arr

def quick_sort(arr, canvas, bars):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left, canvas, bars) + middle + quick_sort(right, canvas, bars)

# Update bars for visualization
def update_bars(canvas, bars, arr):
    canvas.delete("all")
    bar_width = 600 // len(arr)
    for i, value in enumerate(arr):
        x0 = i * bar_width
        y0 = 300 - (value * 3)
        x1 = (i + 1) * bar_width
        y1 = 300
        canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
    canvas.update()

def generate_array(size):
    arr = list(range(1, size + 1))
    random.shuffle(arr)
    return arr

# Data Collection for ML
data_sizes = []
data_times = []

def analyze_time():
    size = int(size_var.get())
    algorithm = algo_var.get()
    arr = generate_array(size)
    canvas.delete("all")
    bars = arr.copy()
    update_bars(canvas, bars, arr)
    start_time = time.time()
    if algorithm == "Bubble Sort":
        bubble_sort(arr, canvas, bars)
    elif algorithm == "Merge Sort":
        arr = merge_sort(arr, canvas, bars)
    elif algorithm == "Quick Sort":
        arr = quick_sort(arr, canvas, bars)
    end_time = time.time()
    time_taken = end_time - start_time
    result_var.set(f"Time Taken: {time_taken:.6f} sec")
    data_sizes.append(size)
    data_times.append(time_taken)

def train_and_plot():
    if len(data_sizes) < 3:
        result_var.set("Need more data to train!")
        return
    X = np.array(data_sizes).reshape(-1, 1)
    y = np.array(data_times)
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)
    X_pred = np.linspace(min(data_sizes), max(data_sizes), 100).reshape(-1, 1)
    y_pred = model.predict(poly.transform(X_pred))
    fig, ax = plt.subplots()
    ax.scatter(data_sizes, data_times, color='blue', label='Actual')
    ax.plot(X_pred, y_pred, color='red', label='Predicted')
    ax.set_xlabel("Array Size")
    ax.set_ylabel("Time Taken (sec)")
    ax.set_title("Sorting Time Prediction (Polynomial Regression)")
    ax.legend()
    canvas_plot = FigureCanvasTkAgg(fig, master=root)
    canvas_plot.get_tk_widget().pack()
    canvas_plot.draw()

# GUI Setup
root = tk.Tk()
root.title("Sorting Algorithm Analyzer")
root.geometry("700x600")
style = ttk.Style()
style.theme_use("clam")

size_var = tk.StringVar(value="50")
algo_var = tk.StringVar(value="Bubble Sort")
result_var = tk.StringVar()

canvas = tk.Canvas(root, width=600, height=300, bg="white")
canvas.pack()

frame_controls = tk.Frame(root)
frame_controls.pack()

ttk.Label(frame_controls, text="Array Size:").grid(row=0, column=0)
ttk.Entry(frame_controls, textvariable=size_var).grid(row=0, column=1)

ttk.Label(frame_controls, text="Algorithm:").grid(row=1, column=0)
ttk.Combobox(frame_controls, textvariable=algo_var, values=["Bubble Sort", "Merge Sort", "Quick Sort"]).grid(row=1, column=1)

ttk.Button(frame_controls, text="Analyze", command=analyze_time).grid(row=2, column=0, columnspan=2)
ttk.Button(frame_controls, text="Train & Predict", command=train_and_plot).grid(row=3, column=0, columnspan=2)

ttk.Label(root, textvariable=result_var).pack()
root.mainloop()
