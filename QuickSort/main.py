# This is a sample Python script.
import sys
sys.path.append('../Visual/colors.py')
from Visual.colors import *
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def partition(arr, low, high):
    # rightmost element is pivot
    pivot = arr[high]

    # pointer
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # swap greater than pivot to right side
            arr[i], arr[j] = arr[j], arr[i]

    # swap greater with pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # return position that is done
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        # recursive qsort for left side
        quick_sort(arr, low, pi - 1)
        # recursive qsort for right side
        quick_sort(arr, pi + 1, high)
def quick_sort_visual(arr, low, high, drawData, timeTick):
    n = len(arr)
    # create list gradient colors hex code
    gradient = generate_gradient(n)
    if low < high:
        pi = partition(arr, low, high)

        # recursive qsort for left side
        quick_sort_visual(arr, low, pi - 1, drawData, timeTick)
        # recursive qsort for right side
        quick_sort_visual(arr, pi + 1, high, drawData, timeTick)

        drawData(arr, [PURPLE if low <= x < pi else YELLOW if x == pi
                        else DARK_BLUE if pi < x <= high else gradient[x] for x in range(n)])
        time.sleep(timeTick)

    drawData(arr, [gradient[x] for x in range(n)])

def call_quick_sort_visual(arr, drawData, timeTick):
    start = time.process_time()
    quick_sort_visual(arr, 0, len(arr) - 1, drawData, timeTick)
    elapsed_time = time.process_time() - start
    # result
    print('Sorted array: ', arr)
    # time
    print('Execution time: ', elapsed_time)

    return arr

def call_quick_sort(arr):
    start = time.process_time()
    quick_sort(arr, 0, len(arr) - 1)
    return arr


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Quick Sort')
    arr = [64, 34, 25, 12, 22, 11, 90]
    call_quick_sort(arr)
    print(arr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
