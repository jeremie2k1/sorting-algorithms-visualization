# This is a sample Python script.
from Visual.colors import *
import time
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def counting_sort_visual(data, drawData, timeTick):

    gradient = generate_gradient(len(data))
    start = time.process_time()

    n = max(data)
    count_pos = [0] * (n + 1)

    m = min(data)
    count_neg = [0]
    if m < 0:
        count_neg = [0] * (-m + 1)

    num_neg = 0
    for x in data:
        if x >= 0:
            count_pos[x] += 1
        else:
            count_neg[-x] += 1
            num_neg += 1

    for i in range(1, n + 1):
        count_pos[i] += count_pos[i - 1]
    if m < 0:
        for i in range(1, -m + 1):
            count_neg[i] += count_neg[i - 1]
    # print(count_neg)
    output = [0 for i in range(len(data))]
    for i in range(len(data)):
        if data[i] >= 0:
            output[num_neg + count_pos[data[i]] - 1] = data[i]
            count_pos[data[i]] -= 1
        else:
            output[count_neg[-data[i]] - 1] = data[i]
            count_neg[-data[i]] -= 1
        drawData(output, [gradient[x] for x in range(len(data))])
        time.sleep(timeTick)

    # print(output)
    output[:num_neg] = output[:num_neg][::-1]
    drawData(output, [gradient[x] for x in range(len(data))])

    # for i in range(n):
    #     for j in range(count[i]):
    #         data[k] = i
    #         drawData(data, [gradient[x] for x in range(len(data))])
    #         time.sleep(timeTick)
    #         k += 1

    elapsed_time = time.process_time() - start
    drawData(output, [gradient[x] for x in range(len(data))])
    # result
    print('Sorted array: ', output)
    # time
    print('Execution time: ', elapsed_time)


def counting_sort(arr):
    n = max(arr)
    count_pos = [0] * (n + 1)

    m = min(arr)
    count_neg = [0]
    if m < 0:
        count_neg = [0] * (-m + 1)

    num_neg = 0
    for x in arr:
        if x >= 0:
            count_pos[x] += 1
        else:
            count_neg[-x] += 1
            num_neg += 1

    for i in range(1, n + 1):
        count_pos[i] += count_pos[i - 1]
    if m < 0:
        for i in range(1, -m + 1):
            count_neg[i] += count_neg[i - 1]
    # print(count_neg)
    output = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        if arr[i] >= 0:
            output[num_neg + count_pos[arr[i]] - 1] = arr[i]
            count_pos[arr[i]] -= 1
        else:
            output[count_neg[-arr[i]] - 1] = arr[i]
            count_neg[-arr[i]] -= 1

    # print(output)
    output[:num_neg] = output[:num_neg][::-1]
    return output
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Counting Sort')
    arr = [64, 34, 0, 25, -10, -22, 12, -33, 22, 11, 90]
    print(counting_sort(arr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
