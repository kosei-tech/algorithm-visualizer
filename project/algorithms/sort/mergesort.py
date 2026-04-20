from .sorter import Sorter
class MergeSort(Sorter):
    def merge(self,data:list[int],p:int,q:int,r:int)->None:
            i = p
            j = q+1
            sub_data = []
            while i <= q and j <= r:
                if data[i] <= data[j]:
                    sub_data.append(data[i])
                    i += 1
                    
                else: 
                    sub_data.append(data[j])
                    j += 1
            
            if i <= q:
                for index in range(i,q+1):
                    sub_data.append(data[index])
                    
            if j <= r:
                for index in range(j,r+1):
                    sub_data.append(data[index])
                    
            data[p:r+1] = sub_data.copy()
            
    def sort(self,data:list[int])->list[int]:
        p = 0
        if len(data) <= 1:
            return data.copy()
        r = len(data)-1
        sub_data = data.copy() 
        self._merge_sort(sub_data,p,r)
        return sub_data
            
    def _merge_sort(self,data:list[int],p:int,r:int)->None:
        if p < r:
            q = (p+r)//2
            self._merge_sort(data,p,q)
            self._merge_sort(data,q+1,r)
            self.merge(data,p,q,r)