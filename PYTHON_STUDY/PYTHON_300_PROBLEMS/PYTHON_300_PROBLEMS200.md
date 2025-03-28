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

