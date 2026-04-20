from .sorter import Sorter
class merge_sort(Sorter):
    def sort(self,data:list[int],p:int,r:int)->list[int]:
        def merge(self,data:list[int],p:int,q:int,r:int)->None:
            i = p
            j = q+1
            k = p
            sub_data = []
            while i <= q or j <= r:
                if data[i] <= data[j]:
                    sub_data[k].append(data[i])
                    i += 1
                    
                else: 
                    sub_data[k].append(data[j])
                    j += 1
                k += 1
            
            if i <= q:
                for index in range(p,q):
                    sub_data[index].appned(data[index])
                    
            elif j <= r:
                for index in range(q+1,r):
                    sub_data[index].append(data[index])
                    
            data = sub_data.copy()

        if p < r:
            q = (p+r)/2
            merge_sort(data,p,q)
            merge_sort(data,q+1,r)
            merge(data,p,q,r)