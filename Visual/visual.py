from tkinter import *
from tkinter import ttk
import random

from colors import *

from BubbleSort.main import bubble_sort_visual
from QuickSort.main import call_quick_sort_visual
from CountingSort.main import counting_sort_visual
from InsertSort.main import insert_sort_visual
from SelectionSort.main import selection_sort_visual
from MergeSort.main import merge_sort_visual
# Main window
window = Tk()
window.title("Sorting Algorithms Visual")
window.maxsize(1000, 800)
window.config(bg=WHITE)


algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
speed_list = ['Fast', 'Medium', 'Slow']

# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 200
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 190
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()



# Randomly generate array
def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(-100, 100)
        data.append(random_value)

    Gradient = generate_gradient(100)
    drawData(data, [Gradient[x] for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.01
    else:
        return 0.0001


def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort_visual(data, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        call_quick_sort_visual(data, drawData, timeTick)
    elif algo_menu.get() == 'Counting Sort':
        counting_sort_visual(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insert_sort_visual(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort_visual(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort_visual(data, 0, len(data) - 1, drawData, timeTick)
    else:
        return

### User interface ###
UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)

b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)


window.mainloop()