from ..algorithms.sort.quicksort import QuickSort
from ..algorithms.sort.mergesort import MergeSort

class SortService:
    def __init__(self):
        self.q = QuickSort()
        self.m = MergeSort()
        
    def sort(self,data:list[int],algorithm:str)->list[int]:
        if algorithm == 'quick':
            return self.q.sort(data)
        elif algorithm == 'merge':
            return self.m.sort(data)
        else:
            raise ValueError