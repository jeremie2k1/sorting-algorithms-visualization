# This is a sample Python script.
from Visual.colors import *
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def selection_sort_visual(data, drawData, timeTick):
    gradient = generate_gradient(len(data))
    start = time.process_time()

    for i in range(len(data) - 1):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        drawData(data, [YELLOW if x == min_idx or x == i else gradient[x] for x in range(len(data))])
        time.sleep(timeTick)

    elapsed_time = time.process_time() - start
    drawData(data, [gradient[x] for x in range(len(data))])

    # result
    print('Sorted array: ', data)
    # time
    print('Execution time: ', elapsed_time)


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Selection Sort')
    arr = [64, 34, 25, 12, 22, 11, 90]
    selection_sort(arr)
    print(arr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
