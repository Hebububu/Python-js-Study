# 파이썬 분기문

## 101번

```py
True or False
# Bool 값이다. 
```

## 102번

```py
print(3 == 5)
> False
```

## 103번

```py
print(3 < 5)
> True
```

## 104번

```py
x = 4
print(1 < x < 5)
> True
```

## 105번

```py
print ((3 == 3) and (4 != 3))
> True
```

## 106번

```py
print(3 => 4)
```

- 연산자를 잘못 썼음

## 107번

```py
if 4 < 3:
    print("Hello World")
```

- 아무런 일도 일어나지 않는다

## 108번

```py
if 4 < 3:
    print("Hello World")
else:
    print("Hi, there")
> Hi, there
```

## 109번

```py
if True:
    print("1")
    print("2")
else:
    print("3")
print("4")

> 1
> 2
> 4
```

## 110번

```py
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")

> 3
> 5
```

## 111번

```py
hi = input()
print(hi*2)
```

## 112번

```py
input = input("입력 :")
print(10 + int(input))
```

## 113번

```py
user = input("입력 :")

if int(user) % 2 == 0:
    print("짝수")
else:
    print("홀수")
```

- % 자꾸 까먹는다. 나머지를 계산하는거임. 

## 114번

```py
user = input("입력 :")
sum_user = int(user) + 20
if sum_user < 255:
    print(sum_user)
else:
    print(255)
```

## 115번

```py
user = input("입력 :")
num = int(user) - 20

if num < 0:
    print(0)
else:
    if num > 255:
        print(255)
    else:
        print(num)
```

- elif를 써도 됨

```py
user = input("입력 :")
num = int(user) - 20

if num > 255:
    print(255)
elif num < 0:
    print(0)
else:
    print(num)
```

## 116번

```py
user = input("현재시간:")
if user.endswith(":00"):
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")
```

## 117번

```py
user = input("좋아하는 과일은? ")
fruit = ["사과", "포도", "홍시"]

if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")
```

- in 키워드를 사용하여 포함된 문자열 확인

## 118번

```py
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input("입력 :")

if user in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")
```

## 119번

```py
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("입력 :")

if user in fruit.keys():
    print("정답입니다.")
else:
    print("오답입니다.")
```

- 답에선 keys를 안썼음. 
- 지피티한테 물어보니까 in fruit 해도 key를 검사하는거라 상관 없다고 함. 

## 120번

```py
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("입력 :")

if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
```

## 121번

```py
user = input("입력 :")
if user.islower():
    print(user.upper())
else:
    print(user.lower())
```

## 122번

```py
user = input("score: ")
score = int(user)
if score >= 81:
    print("grade is A")
elif score >= 61:
    print("grade is B")
elif score >= 41:
    print("grade is C")
elif score >= 21:
    print("grade is D")
else:
    print("grade is E")
```

## 123번

```py
curruncy = {
    '달러': 1167,
    '엔': 1.096,
    '유로': 1268,
    '위안': 171 
}
user = input("입력: ")
amout_str, unit = user.split()

if unit in curruncy:
    amount = float(amout_str)
    result = amount * curruncy[unit]
    print(f"{result:.2f} 원")
else:
    print("잘못된 입력입니다.")
```

## 124번

```py
number1 = int(input("입력: "))
number2 = int(input("입력: "))
number3 = int(input("입력: "))

num_list = [number1, number2, number3]
print(max(num_list))
```

## 125번

```py
telecom = {
    'SKT': 011,
    'KT': 016,
    'LGU': 019,
    '알수없음' : 010
}

user = input("휴대전화 번호 입력: ")
split_number = user.split("-")
head = split_number[0]                

if head == "011":
    print("당신은 SKT 사용자입니다.")
elif head == "016":
    print("당신은 KT 사용자입니다.")
elif head == "019":
    print("당신은 LGU 사용자입니다.")
else:
    print("당신은 알 수 없는 사용자입니다.")
```

