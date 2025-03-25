# 파이썬 300제 시작.
- 따로 파일을 만들지는 않고, 문제를 풀고 풀이를 보고 진행하자. 
- 어려운 문제의 경우 파일을 만들어서 실제로 실행시켜볼 것. 


# 파이썬 시작하기 문제

## 1번 print 기초
```py
print("Hello World")
```

## 2번 print 기초
```py
print("Mary's cosmetics")
```

- 작은따음표가 들어가 있음으로 큰따음표로 처리.

## 3번 print 기초

```py
print('신씨가 소리질렀다. "도둑이야".')
```

## 4번 문제 print 기초
```py
print("C:\\Windows")
```

- 백슬래시의 경우 두번 적어야 제대로 문자열로 출력된다. 

## 5번 문제
```py
print("안녕하세요.\n만나서\t\t반갑습니다.")
```

- 백슬래시n (\n)은 줄바꿈, 백슬래시t (\t)의 경우 탭이 된다. 

## 6번 문제 print 여러 데이터 출력

```py
print("오늘은", "일요일")
```

- 여러 값을 출력할때는 쉼표로 구분하여 출력한다. 

## 7번 문제 print 기초

```py
print("naver","kakao","sk","samsung", sep=";")
```

- sep= 라는 옵션을 사용해서 쉼표 사이사이에 넣을 걸 지정할 수 있다. 

## 8번 문제 print 기초

```py
print("naver","kakao","sk","samsung", sep="/")
```

- 똑같이 sep= 옵션을 사용한다. 

## 9번 문제 print 줄바꿈
```py
print("first", end=""); print("second")
```

- 줄바꿈 없이 출력하는 것. end의 기본값이 \n으로 되어있는걸 공란으로 바꾸면 된다. 

## 10번 문제 연산 결과 출력
```py
print(5/3)
```

- 5/3의 결과를 출력하기

# 파이썬 변수

## 11번 문제 변수 사용하기

```py
삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)
```

- 변수애 값을 바인딩해보기기

## 12번 문제 변수 사용하기

```py
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print("시가총액 :", int(시가총액))
print("현재가 :", int(현재가))
print("PER: ", float(PER))
```

- 변수의 type을 정의하는 부분

## 13번 문제 문자열 출력

```py
s = "hello"
t = "python"

print(f"{s}! {t}")
```

## 14번 문제 파이썬을 이용한 값 계산

```py
print(2 + 2 * 3)
```

- 8의 값이 나온다

## 15번 문제 type 함수

```py
a = 128
print(type(a))
<class 'int'>

a = "132" #의 타입 값은?
> str 이다. 
```

- 따옴표로 감싸진 숫자는 문자열. 

## 16번 문제 문자열을 정수로 변환

```py
num_str = "720"
num_int = int(num_str)
print(num_int+1, type(num_int))
```

- int() 에 넣어서 바꿀 수 있다. 

## 17번 문제 정수를 문자열 100으로 변환

```py
num = 100
num_str = str(num)
print(num_str, type(num_str))
```

- str()에 넣어서 바꿀 수 있다. 

## 18번 문제 문자열을 정수로 변환

```py
string = 15.79
float_string = float(string)
print(float_string, type(float_string))
```

- float()에 넣어서 바꿀 수 있다. 

## 19번 문제 문자열을 정수로 변환

```py
year = "2020"
year_int = int(year)
print(year_int)
print(year_int-1)
print(year_int-2)
```

- int 로 변환 후 연산자로 계산 

## 20번 문제 파이썬 계산

```py
monthly_price = 48584
total_month = 36
total_price = monthly_price * total_month
print(total_price)
```

# 파이썬 문자열

## 21번 문제 문자열 인덱싱

```py
letters = 'python'
print(letters[0],letters[2])
```

- 변수명[0] 등으로 인덱싱을 할 수 있다. 0부터 시작하는 것을 기억하자. 

## 22번 문제 문자열 슬라이싱

```py
license_plate = "24가 2210"
print(license_plate[4:8])
```

- 변수명[0:0] 등으로 슬라이싱을 할 수 있다. 0부터 시작하는 것을 기억하자.

## 23번 문제 문자열 인덱싱

```py
string = "홀짝홀짝홀짝"
print(string[::2])
```

- 처음 보는 기능이라 이해가 잘 안됐음. 
- 슬라이싱은 **start:stop:step** 순서로 진행된다고 함.
- start는 시작 인덱스 (생략하면 0부터 시작함)
- stop은 끝 인덱스 (생략하면 끝까지 진행함)
- step은 몇칸씩 건너뛰면서 가져올지 (여기서는 2)

- 따라서 값은 처음부터 끝까지 가져오되, 두칸씩 건너뛰면서 가져오기 떄문에
> 홀홀홀
- 이라는 결과값이 나오게 된다.

## 24번 문제 문자열 인덱싱

```py
string = "PYTHON"
print(string[::-1])
```

- 이 역시도 답안을 보고 알았다. 
- 슬라이싱에 음수값을 넣으면 역순으로 가져오게 됨. -1 값을 넣었기 때문에 맨 뒤에서부터 가져온다. 

## 25번 문제 문자열 치환

```py
phone_number = "010-1234-5678"
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)
```

- 답안을 보고 알았다.
- 그냥 인덱싱으로 010 부분이랑 1234 부분이랑 5678을 잘라서 하려고 했음 (바보..)
- replace() 함수를 사용해서 하이폰을 공백으로 교체하면 편하게 할 수 있다. 

## 26번 문제 문자열 다루기

```py
phone_number = "010-1234-5678"
phone_number1 = phone_number.replace("-","")
print(phone_number1)
```

- 같은 원리로 replace() 함수를 사용하면 된다.

## 27번 문제 문자열 다루기 (kr 부분 추출하기기)

```py
url = "http://sharebook.kr"
print(url[17:19])
```

- 내가 푼 답변

```py
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])
```

- 실제 답안에서는 split() 함수를 사용했다.
- 왜 -1을 사용하는지 잘 모르겠어서 GPT에게 물어봤다.

```md
왜 -1을 사용하는지?
split() 함수는 문자열을 나누면 리스트로 반환되는데, 각 부분이 점(.)을 기준으로 나눠지므로 마지막 부분은 'kr'가 됩니다.
[-1]은 이 리스트에서 가장 마지막 원소를 가져오는 방법입니다. 그래서 kr이 출력됩니다.
```

- 마지막 원소를 가져올때 -1 을 사용하는는걸 알았다. 

## 28번 문자열은 immutable

```py
lang = 'python'
lang[0] = "P"
print(lang)
```

- 문자열은 수정할 수 없기 때문에 (assignment 메서드를 지원하지 않는다.) 결과값은 그냥 python이 나오게 된다.. 

## 29번 replace 메서드

```py
string = 'abcdfe2a354a32a'
edited_string = string.replace('a', 'A')
print(edited_string)
```

- replace() 메서드를 사용하는 간단한 변경 문제였다.

## 30번 replace 메서드

```py
string = 'abcd'
string.replace('b','B')
print(string)
> abcd
```

- 문자열은 변경 불가능한 데이터 타입이다.

```py
string = 'abcd'
new_string = string.replace('b','B')
print(new_string)
> aBcd
```

- 만약 바꾸고 싶다면 이런 방식을 사용해야 할 것. 