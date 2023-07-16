# This is a sample Python script.
from Visual.colors import *
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def merge_sort_visual(data, begin, end, drawData, timeTick):
    gradient = generate_gradient(len(data))
    start = time.process_time()

    if begin < end:
        mid = (begin + end) // 2

        merge_sort_visual(data, begin, mid, drawData, timeTick)
        merge_sort_visual(data, mid + 1, end, drawData, timeTick)

        merge_sort(data, begin, mid, end)
        drawData(data, [PURPLE if x >= begin and x < mid else YELLOW if x == mid
                        else DARK_BLUE if x > mid and x <= end else gradient[x] for x in range(len(data))])
        time.sleep(timeTick)

    elapsed_time = time.process_time() - start
    drawData(data, [gradient[x] for x in range(len(data))])

    # result
    print('Sorted array: ', data)
    # time
    print('Execution time: ', elapsed_time)

def merge_sort(arr, begin, mid, end):
    left = begin
    right = mid + 1
    sub_merged_arr = []

    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            sub_merged_arr.append(arr[left])
            left += 1
        else:
            sub_merged_arr.append(arr[right])
            right += 1

    while left <= mid:
        sub_merged_arr.append(arr[left])
        left += 1
    while right < end:
        sub_merged_arr.append(arr[right])
        right += 1

    # assign to data
    for i in range(len(sub_merged_arr)):
        arr[begin] = sub_merged_arr[i]
        begin += 1


def call_merge_sort(arr, begin, end):
    if begin < end:
        mid = (begin + end) // 2

        call_merge_sort(arr, begin, mid)
        call_merge_sort(arr, mid+1, end)

        merge_sort(arr, begin, mid, end)

    return arr
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Merge Sort')
    arr = [64, 34, 0, 25, -10, -22, 12, -33, 22, 11, 90]
    print(call_merge_sort(arr, 0, len(arr) - 1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
