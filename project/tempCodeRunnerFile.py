from algorithms.sort.quicksort import QuickSort
from algorithms.sort.mergesort import MergeSort
from services.algorithm_service import SortService

data = list(input("データを入力してください: "))
algorithm = input("アルゴリズムを選択してください(quick or merge): ")

service = SortService()
print(f"ソート前: {data}")
data = service.sort(data,algorithm)
print(f'ソート後: {data}')