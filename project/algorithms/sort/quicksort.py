from .sorter import Sorter
class quick_sort(Sorter):
    
    def partiton(self,data:list[int],p:int,r:int)->int:
            i = p
            j = r
            x = data[p]
            while True:
                while data[j] > x:
                    j -= 1
                    
                while data[i] < x:
                    i += 1
                    
                if i < j:
                    tmp = data[i]
                    data[i] = data[j]
                    data[j] = tmp
                
                else:
                    break
            return j

    
    def sort(self,data:list[int],p:int,r:int)->list[int]:
        if p < r:
            q = self.partiton(data,p,r)
            self.quick_sort(data,p,q)
            self.quick_sort(data,q+1,r)