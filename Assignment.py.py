Assignment.py
    import tkinter as tk
import random
import time

# Create window
root = tk.Tk()
root.title("Sorting Algorithm Visualization")
root.geometry("800x500")

# Canvas
canvas = tk.Canvas(root, width=800, height=400, bg="white")
canvas.pack()

# Generate random numbers
arr = [random.randint(20, 350) for _ in range(20)]


def draw_array():
    canvas.delete("all")

    bar_width = 800 / len(arr)

    for i in range(len(arr)):
        x1 = i * bar_width
        y1 = 400 - arr[i]
        x2 = (i + 1) * bar_width - 2
        y2 = 400

        canvas.create_rectangle(
            x1, y1, x2, y2,
            fill="skyblue"
        )

    root.update()


def bubble_sort():
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            # Highlight the two bars being compared
            canvas.delete("all")
            bar_width = 800 / len(arr)

            for k in range(n):
                x1 = k * bar_width
                y1 = 400 - arr[k]
                x2 = (k + 1) * bar_width - 2
                y2 = 400

                if k == j or k == j + 1:
                    color = "red"
                else:
                    color = "skyblue"

                canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color
                )

            root.update()
            time.sleep(0.1)

            # Swap
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    draw_array()


def generate_array():
    global arr
    arr = [random.randint(20, 350) for _ in range(20)]
    draw_array()


# Buttons
tk.Button(
    root,
    text="Generate New Array",
    command=generate_array
).pack(side=tk.LEFT, padx=20)

tk.Button(
    root,
    text="Start Bubble Sort",
    command=bubble_sort
).pack(side=tk.RIGHT, padx=20)


# Initial display
draw_array()

root.mainloop()