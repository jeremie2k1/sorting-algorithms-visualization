import time
from colors import *

def merge(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1

def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data, mid+1, end, drawData, timeTick)

        merge(data, start, mid, end, drawData, timeTick)

        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid
                        else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])

    # Heap sort
    import time
    from colors import *

    def heapify(data, n, i, drawData, timeTick):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[i] < data[left]:
            largest = left

        if right < n and data[largest] < data[right]:
            largest = right

        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            heapify(data, n, largest, drawData, timeTick)

    def heap_sort(data, drawData, timeTick):
        n = len(data)

        for i in range(n - 1, -1, -1):
            heapify(data, n, i, drawData, timeTick)

        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            heapify(data, i, 0, drawData, timeTick)
            drawData(data, [YELLOW if x == i else BLUE for x in range(n)])
            time.sleep(timeTick)

        drawData(data, [BLUE for x in range(len(data))])
