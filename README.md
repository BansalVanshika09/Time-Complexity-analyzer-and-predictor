# Sorting Algorithm Analyzer with Machine Learning

This project is a simple yet powerful tool to analyze and visualize the performance of popular sorting algorithms — Bubble Sort, Merge Sort, and Quick Sort. It includes a graphical user interface and integrates Machine Learning to predict time complexity based on input size.

## Features

- Visualizes sorting process using animated bar charts
- Measures actual time taken for sorting arrays of different sizes
- Allows users to select array type: Random, Sorted, or Reversed
- Trains a Polynomial Regression model to predict sorting time
- Compares actual vs. predicted performance on a graph
- Clean and interactive GUI built with Tkinter

## Technologies Used

- Python 3
- Tkinter for GUI
- Matplotlib for plotting and animation
- NumPy and Scikit-learn for Machine Learning

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/sorting-analyzer.git
cd sorting-analyzer


How It Works
Choose an algorithm and array configuration.

Click "Analyze" to view the sorting process and execution time.

After multiple runs, click “Train ML Model & Plot” to see how ML predicts sorting time based on your data.

The model uses Polynomial Regression for better accuracy on non-linear trends.

What I Learned
Visualizing algorithms helped solidify my understanding of how they work.

Integrated a basic machine learning model into a practical tool.

Gained hands-on experience in GUI development and data visualization.

Future Improvements
Add more sorting algorithms like Heap Sort, Insertion Sort, etc.

Enable export of performance data

Include sorting complexity comparison charts
