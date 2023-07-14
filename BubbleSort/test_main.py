from unittest import TestCase
# import random
from numpy import random
import numpy as np
import main

class TestBubbleSort(TestCase):

    def test_size_1(self, size=1):
        print()
        arr = random.randint(low=-100000000, high=100000000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(main.bubble_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())

    def test_size_10(self, size=10):
        print()
        arr = random.randint(low=-100000000, high=100000000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(main.bubble_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())
    def test_size_100(self, size=100):
        print()
        arr = random.randint(low=-100000000, high=100000000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(main.bubble_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())

    def test_size_1000(self, size=1000):
        print()
        arr = random.randint(low=-100000000, high=100000000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(main.bubble_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())

    def test_size_10000(self, size=10000):
        print()
        arr = random.randint(low=-100000000, high=100000000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(main.bubble_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())