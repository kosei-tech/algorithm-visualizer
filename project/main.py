from algorithms.sort.quicksort import QuickSort
from algorithms.sort.mergesort import MergeSort
from services.algorithm_service import SortService

data = input("データを入力してください: ").split()
data = list(map(lambda v1:int(v1),data))
algorithm = input("アルゴリズムを選択してください(quick or merge): ")
algorithm = algorithm.lower()

service = SortService()
print(f"ソート前: {data}")
data = service.sort(data,algorithm)
print(f'ソート後: {data}')