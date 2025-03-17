# 제어문
- 다른 조건마다 다른 일을 시킬 순 없을까? 혹은 반복되는 일을 하게 할 순 없을까?
- 이런 생각에 탄생한 것이 바로 조건문과 반복문. (Flow Control - 실행되는 흐름을 제어한다).

## 그렇다면 어떤 조건을 걸어야 할까?
- 조건을 비교할 수 있다면 선택이 쉬워질 것이다.
- 그것을 비교할 수 있게 만들어 둔 연산자가 바로 **'비교연산자'** 라는 것이다.

- 그 비교의 결과를 표현해주는 data type이 필요한데, 거기서 사용하는 것이 바로 **Boolean**, 참과 거짓을 표현하는 비교연산자이다.

## Boolean 

- 현재까지 배운 데이터 타입?
- 숫자열, 문자열 등등 

- Boolean 데이터 타입은 단 두가지밖에 없다. True, False.

## 비교연산자 

```py
print('1 == 1', 1 == 1) # 같냐
print('1 == 2', 2 == 1) 
print('1 < 2', 1 < 2 ) # 크냐
print('1 > 2', 1 > 2) 
print('1 >= 1', 1 >= 1) # 크거나 같냐
print('2 >= 1', 2 >= 1) 
print('1 != 1', 1 != 1) # != 다르냐?
print('2 != 1', 2 != 1)
```

```py
1 == 1 # 같은가?
1 < 2, 1 > 2 # 크거나 작은가?
1 >= 1, 2 >= 1 # 크거나 같은가?
1 != 1, 2 != 1 # 다른가?
```

## 조건문의 기본 형식

- 조건문을 사용하면 하나의 프로그램으로 여러 행동을 할 수 있게 됩니다.
 
 ```py
# 012
print(0)
if True:
    print(1)
print(2)


print('------')

# 02
print(0)
if False:
    print(1)
print(2)
```

- True와 False Boolean 값에 따라서 달라지는 출력값을 확인했다. 

```py
input_id = input('id: ')
id = 'Hebu'

if input_id == id:
    print('Hello Hebu!')
```

- input_id가 Hebu 라면, 인사하는 간단한 어플리케이션. 

## else 

```py
#013
print(0)
if True:
    print(1)
else:
    print(2)
print(3)

print('----')

#023
print(0)
if False:
    print(1)
else:
    print(2)
print(3)
```


```py
input_id = input('id: ')
id = 'Hebu'

if input_id == id:
    print('Hello Hebu!')
else:
    print('Who are you?')
```

- input_id 가 Hebu가 아닌 경우, else가 실행.

## elif

```py
# 014 
print(0)
if True:
    print(1)
elif True:
    print(2)
else:
    print(3)
print(4)

print('----')

# 024
print(0)
if False:
    print(1)
elif True:
    print(2)
else:
    print(3)
print(4)

print('---')

# 034
print(0)
if False:
    print(1)
elif False:
    print(2)
else:
    print(3)
print(4)
```

- if가 True인 경우 if를 실행
- if가 False인 경우 그 다음 elif를 확인하여 실행
- 모든 elif가 False인 경우 최종적으로 else를 실행

```py
input_id = input('id: ')
id1 = 'Hebu'
id2 = 'admin'

if input_id == id1:
    print('Hello Hebu!')
elif input_id == id2:
    print('Hello admin!')
else:
    print('Who are you?')
```

- Hebu인 경우 Hebu에게 인사.
- admin인 경우 admin에게 인사. 
- 그 누구도 아닌 경우 누구냐고 되묻는 애플리케이션.


## 조건문의 중첩


```py
input_id = input('id: ')
id = 'Hebu'
input_password = input('password: ')
password = '1234'

if input_id == id:
    if input_password == password:
        print('Welcome!')
    else:
        print('Wrong Password!')
else: 
    print('wrong id')
```

- id와 비밀번호를 비교하는 중첩 조건문이다.


## 반복문 for 
```py
names = ['Hebu', 'HeaveKK', 'Heaven']

for name in names:
    print('hi, ' + name + '. Bye, ' + name + '.')
```

- for [변수명] in 리스트: 형식으로 작성할 수 있다. 리스트를 순환하며 [변수명]에 하나씩 할당하며 반복되는 반복문 for 이다.

## 다차원 리스트 

```py
lists = [
    ['hebu', 'seoul', 'vrchat'],
    ['heavekk', 'tokyo', 'artist'],
    ['heaven', 'nowhere', 'dream']
]
```

- 복잡하게 얽혀있는, 많은 정보가 담긴 리스트 자료형도 존재할 수 있다. (리스트 안에 리스트가 있는 경우.)

```py
for list in lists:
    print(list[0]+','+list[1]+','+list[2])
```

- 각 리스트의 1, 2 ,3 번째 요소를 출력

```py
persons = [
    ['hebu', 'seoul', 'vrchat'],
    ['heavekk', 'busan', 'game']
]

for name, address, interest in persons:
    print(name+','+address+','+interest)
```

- 각 변수에 이름을 붙여서, 좀 더 보기 좋게 정리할 수 있다. 

## 딕셔너리 + 루프 

```py
person = {'name':'Hebu', 'address': 'Seoul', 'interest': 'vrchat'}
```

- 딕셔너리의 기본 자료형 

```py
person = {'name':'Hebu', 'address': 'Seoul', 'interest': 'vrchat'}
print(person['name'])

for key in person:
    print(key, person[key])
```

- 딕셔너리에서 for 문으로 key당 데이터를 꺼내기. 

```py
persons = [
    {'name':'Hebu', 'address': 'Seoul', 'interest': 'vrchat'},
    {'name':'Heaven', 'address': 'nowhere', 'interest': 'dream'},
    {'name':'HeaveKK', 'address': 'tokyo', 'interest': 'artist'}
]


for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('-------------')
```

- 딕셔너리 자료형에서 for 문으로 한 객체를 꺼내고, 그 다음 객체의 데이터를 key를 활용하여 보기 좋게 정리하기. 


## 중첩 조건문 추가 배운 점
```py
if input_id == 'Hebu' and input_password == '1234':
    print('welcome')
```

- and를 통해서, 중첩된 조건문을 하나로 합칠 수 있다. 

```py
if input_id == 'hebu' or input_id == 'HeaveKK':
    print('welcome')
```

- or을 통해서, 중첩된 조건문을 하나로 합칠 수 있다.
- and, or **논리연산자** 를 이용해서, 복잡한 로직을 간단하게 표현할 수 있다. 


# 배운 점 

- Boolean을 익혔다. 
- 조건문을 사용하는 방법을 익혔다. 
- 반복문을 사용하는 방법을 익혔다. 
- 리스트, 딕셔너리 자료형을 더 명확하게 활용하는 방법을 배우게 되었다. 

