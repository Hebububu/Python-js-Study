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
