names = ["hebu", "Heaven", "HeaveKK"]
numbers = [1, 2, 3]

print("names[0]: ", names[0]) # 0번째 리스트를 출력 
print("len(names): ",len(names)) # 리스트의 개수를 확인

print("min(numbers): ", min(numbers)) # 최솟값과 최댓값 
print("max(numbers): ", max(numbers))

import statistics # 통계와 관련된 모듈
print("statistics.mean(numbers): ", statistics.mean(numbers)) # 평균값을 구하는 펑션

import random
print("random.choice(names): ", random.choice(names)) # 랜덤 선택

