# This is a sample Python script.
from Visual.colors import *
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def insert_sort_visual(data, drawData, timeTick):
    gradient = generate_gradient(len(data))
    start = time.process_time()

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        drawData(data, [YELLOW if x == j or x == i else gradient[x] for x in range(len(data))])
        time.sleep(timeTick)

    elapsed_time = time.process_time() - start
    drawData(data, [gradient[x] for x in range(len(data))])

    # result
    print('Sorted array: ', data)
    # time
    print('Execution time: ', elapsed_time)


def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Insert Sort')
    arr = [64, 34, 0, 25, -10, -22, 12, -33, 22, 11, 90]
    print(insert_sort(arr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
