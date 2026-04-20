from algorithms.sort.quicksort import QuickSort
from algorithms.sort.mergesort import MergeSort
from services.algorithm_service import SortService
import time

data = input("データを入力してください: ").split()
data = list(map(lambda v1:int(v1),data))
algorithm = input("アルゴリズムを選択してください(quick or merge): ")
algorithm = algorithm.lower()

service = SortService()
print(f"ソート前: {data}")
start = time.time()
data = service.sort(data,algorithm)
end = time.time()
print(f'ソート後: {data}')
print(f'実行時間{end-start}秒')
