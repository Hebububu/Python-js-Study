import pandas
house = pandas.read_csv('PYTHON3\class\9. pypi pip\house.csv')
print(house)
print(house.head(2)) # 앞의 2가지 정보만 보기
print(house.describe()) # 데이터를 묘사해 줌.