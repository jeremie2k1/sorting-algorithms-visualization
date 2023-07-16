# This is a sample Python script.
from Visual.colors import *
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def heapify(arr, N, i):
    max_idx = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[max_idx] < arr[l]:
        max_idx = l

    if r < N and arr[max_idx] < arr[r]:
        max_idx = r

    if max_idx != i:
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

        heapify(arr, N, max_idx)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    print(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def heap_sort_visual(data, drawData, timeTick):
    gradient = generate_gradient(len(data))
    start = time.process_time()

    n = len(data)
    for i in range(n // 2, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
        drawData(data, [YELLOW if x == i else gradient[x] for x in range(n)])
        time.sleep(timeTick)


    elapsed_time = time.process_time() - start
    drawData(data, [gradient[x] for x in range(len(data))])
    # result
    print('Sorted array: ', data)
    # time
    print('Execution time: ', elapsed_time)

    return data


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Heap Sort')
    arr = [0, 34, 64, -10, -22]
    print(heap_sort(arr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
