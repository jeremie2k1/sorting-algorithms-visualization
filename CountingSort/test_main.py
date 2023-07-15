from unittest import TestCase
from numpy import random
import numpy as np
from CountingSort.main import counting_sort

class TestCountingSort(TestCase):
    def test_size_1(self, size=1):
        print()
        arr = random.randint(low=-100000, high=100000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(counting_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())

    def test_size_10(self, size=10):
        print()
        arr = random.randint(low=-100000, high=100000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(counting_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())
    def test_size_100(self, size=100):
        print()
        arr = random.randint(low=-100000, high=100000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(counting_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())

    def test_size_1000(self, size=1000):
        print()
        arr = random.randint(low=-100000, high=100000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(counting_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())

    def test_size_10000(self, size=10000):
        print()
        arr = random.randint(low=-100000, high=100000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(counting_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())

    def test_size_100000(self, size=100000):
        print()
        arr = random.randint(low=-100000, high=100000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(counting_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())

    def test_size_1mil(self, size=1000000):
        print()
        arr = random.randint(low=-100000, high=100000, size=size)

        arr_cp = arr.copy()
        # get bubble sort result
        arr = list(arr)
        arr = np.array(counting_sort(arr))

        # compare with numpy sort lib
        # print(np.sort(arr_cp))
        # assert arr == np.sort(arr_cp)
        self.assertTrue((arr == np.sort(arr_cp)).all())
