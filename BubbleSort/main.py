# This is a sample Python script.
from Visual.colors import *
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped == False:
            break

    return arr

def bubble_sort_visual(arr, drawArr, timeTick):
    n = len(arr)
    # create list gradient colors hex code
    gradient = generate_gradient(n)
    start = time.process_time()

    # main idea
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                # visual sort
                drawArr(arr, [PINK if x == j or x == j + 1 else gradient[x] for x in range(n)])
                time.sleep(timeTick)

        if swapped == False:
            break
    elapsed_time = time.process_time() - start
    drawArr(arr, [gradient[x] for x in range(n)])

    # result
    print('Sorted array: ', arr)
    # time
    print('Execution time: ', elapsed_time)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Bubble Sort')
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(arr))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
