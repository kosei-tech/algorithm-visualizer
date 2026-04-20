from .sorter import Sorter
class QuickSort(Sorter):
    
    def partition(self,data:list[int],p:int,r:int)->int:
        left_idx = p
        right_idx = r
        pivot = data[(p+r)//2]
        while True:
            while right_idx >= p and data[right_idx] > pivot:
                right_idx -= 1
                    
            while left_idx <= r and data[left_idx] < pivot:
                left_idx += 1
                    
            if left_idx < right_idx:
                tmp = data[left_idx]
                data[left_idx] = data[right_idx]
                data[right_idx] = tmp
                left_idx += 1
                right_idx -= 1
                
            else:
                break
        return right_idx

    def sort(self,data:list[int])->list[int]:
        p = 0
        if len(data) <= 1:
            return data.copy()
        r = len(data)-1
        sub_data = data.copy() 
        self._quick_sort(sub_data,p,r)
        return sub_data
        
    def _quick_sort(self,data:list[int],p:int,r:int)->None:
        if p < r:
            q = self.partition(data,p,r)
            self._quick_sort(data,p,q)
            self._quick_sort(data,q+1,r)
            