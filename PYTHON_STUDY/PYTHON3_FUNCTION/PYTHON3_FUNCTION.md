# 파이썬의 함수?

## 우선 정리에 대해서 생각해볼까?
- 연관된 물건을 모아서, 이름을 붙이는 행위다!

- 복잡한 것을 단순화시키고, 단순해진만큼 더 복잡한 일을 할 수 있음. 
- 정리정돈이란 단순화의 연속이라고 생각하면 편할 것이다. 

## 함수를 이용하기
- 연관된 코드를 모아서, 이름을 붙이자! 
- 함수의 입력값에 따라서, 다르게 출력값을 내놓는 함수를 만들자 

```py
def get_vat():
    price = 10000
    vat_rate = 0.1
    print(price*vat_rate)
```

- 변수의 값을 하드코딩 한 경우

```py
def get_vat(price): # <- 매개변수
    vat_rate = 0.1 
    print(price*vat_rate)

get_vat(10000) # <- 인자
```

```py
def get_vat(price,vat_rate):
    print(price*vat_rate)

get_vat(20000,0.3)
```

- 함수가 받을 변수를 함수에 미리 지정하여 둔 경우. (매개변수)
- 함수가 받을 변수 (인자)를 제공하여 함수를 사용. 

```py
def get_vat(price, vat_rate = 0.1):
    print (price*vat_rate)

get_vat(20000)
```

- 내가 사용할 매개변수를 미리 지정할 수도 있음.

```py
def get_vat(price, vat_rate=0.1):
    return price*vat_rate

print(get_vat(10000))
```

- 함수는 가급적 하나의 기능을 가지는 것이 좋다. 
- 재활용성을 생각하자. 값을 입력받고, 하나의 기능을 수행하고, 하나의 값을 내놓으면, 다양한 부분에서 DRY(Do Not Repeat Yourself) 한 코드를 만들 수 있을 것이다.

# 배운 점

- 코드들을 묶어, 이름을 붙이는 방법을 배웠다.
- 매개변수의 개념과, 인자의 개념을 배웠다. 
- 이렇게 잘 정리된 코드들을 통해, 단순화를 적용시키고, 더 복잡하고 어려운 문제를 해결할 수 있는 사람이 되었다!
